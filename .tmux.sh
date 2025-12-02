#!/usr/bin/env bash

set -euo pipefail
source .env

printf '\033]0;%s\033\\' ${PROJECT_NAME}
tmux new-session -d -s ${PROJECT_NAME} -n shell

tmux setw -t ${PROJECT_NAME} -g remain-on-exit on

tmux set -t ${PROJECT_NAME} status-bg '#deb777'
tmux set -t ${PROJECT_NAME} status-fg black

if [ -d .dev ]; then make -C .dev dev ROOT=$(pwd) SESSION=${PROJECT_NAME}; fi

tmux attach-session -t ${PROJECT_NAME}
