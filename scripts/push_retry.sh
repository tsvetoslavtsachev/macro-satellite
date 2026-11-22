#!/usr/bin/env bash
# ИЛЮ3 Ч3: git push с повторен опит при временна грешка на GitHub
# (напр. "GH009: Git LFS object integrity could not be checked", ход от 20.11.2026).
# Ползване: push_retry.sh [ОПИТИ=3] [ПАУЗА_СЕК=20]
# Пауза: ПАУЗА, после 2*ПАУЗА (20, 40 ...). Преди всеки повторен опит: git pull --rebase.
# GIT_PUSH_CMD / GIT_PULL_CMD позволяват подмяна в проба (по подразбиране истинските).
set -u
ATTEMPTS="${1:-3}"
PAUSE="${2:-20}"
PUSH_CMD="${GIT_PUSH_CMD:-git push}"
PULL_CMD="${GIT_PULL_CMD:-git pull --rebase}"
n=1
while true; do
  if $PUSH_CMD; then
    echo "push ok (опит $n/$ATTEMPTS)"
    exit 0
  fi
  if [ "$n" -ge "$ATTEMPTS" ]; then
    echo "push FAILED след $ATTEMPTS опита" >&2
    exit 1
  fi
  wait=$((PAUSE * n))
  echo "push падна (опит $n/$ATTEMPTS), пауза ${wait}s, после pull --rebase" >&2
  sleep "$wait"
  $PULL_CMD || echo "pull --rebase не успя, опитвам push така или иначе" >&2
  n=$((n + 1))
done
