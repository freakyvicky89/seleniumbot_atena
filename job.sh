#!/bin/sh
cd /home/pi/bots/seleniumbot_atena

until sudo protonvpn c -r
do
   sleep 1
done

python3 bot.py

sudo protonvpn d
