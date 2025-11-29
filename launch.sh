#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use
#polybar-msg cmd quit
# Otherwise you can use the nuclear option:
killall -q polybar
while pgrep -x polybar >/dev/null; do sleep 0.1; done

#Launch bar
#if type "xrandr"; then
#  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#    MONITOR=$m polybar --reload midbar &
#  done
#else
#  polybar --reload midbar &
#fi

polybar midbar &
polybar rightbar &
