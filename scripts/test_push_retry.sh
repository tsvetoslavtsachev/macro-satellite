#!/usr/bin/env bash
# Проби (G8, мутация) за push_retry.sh: втори опит минава; три падащи -> ненулев код.
D="$(cd "$(dirname "$0")" && pwd)"
T="$(mktemp -d)"; export T
cat > "$T/flaky.sh" <<'X'
#!/usr/bin/env bash
c=$(cat "$T/cnt" 2>/dev/null || echo 0); c=$((c+1)); echo $c > "$T/cnt"
[ "$c" -ge "${PASS_AT:-2}" ]
X
cat > "$T/pull.sh" <<'X'
#!/usr/bin/env bash
echo x >> "$T/pulls"
X
chmod +x "$T/flaky.sh" "$T/pull.sh"
export GIT_PUSH_CMD="$T/flaky.sh" GIT_PULL_CMD="$T/pull.sh"
fail=0
echo "--- проба 1: пада на 1-вия, минава на 2-рия"
PASS_AT=2 bash "$D/push_retry.sh" 3 1; rc=$?
echo "rc=$rc push_calls=$(cat $T/cnt) pulls=$(wc -l < $T/pulls)"
[ $rc -eq 0 ] && [ "$(cat $T/cnt)" = 2 ] && [ "$(wc -l < $T/pulls)" -eq 1 ] || fail=1
rm -f "$T/cnt" "$T/pulls"
echo "--- проба 2: и трите падат"
PASS_AT=99 bash "$D/push_retry.sh" 3 1; rc=$?
echo "rc=$rc push_calls=$(cat $T/cnt)"
[ $rc -ne 0 ] && [ "$(cat $T/cnt)" = 3 ] || fail=1
[ $fail -eq 0 ] && echo "ТЕСТОВЕТЕ ОК" || echo "ТЕСТОВЕТЕ ПАДНАХА"
rm -rf "$T"; exit $fail
