#!/bin/bash

font='JetBrains Mono:size=10'
gray1='#3b4252'
gray2='#4c566a'
gray3='#d8dee9'
gray4='#3b4252'
cyan='#88c0d0'

action=$(echo -e "Suspend\nReboot\nShutdown" | dmenu -i -fn "$font" -nb "$gray1" -nf "$gray3" -sb "$cyan" -sf "$gray4")

if [[ "$action" = "Suspend" ]]; then
  systemctl suspend
elif [[ "$action" = "Reboot" ]]; then
  systemctl reboot
elif [[ "$action" = "Shutdown" ]]; then
  systemctl shutdown now
else
  exit 1
fi

exit 0
