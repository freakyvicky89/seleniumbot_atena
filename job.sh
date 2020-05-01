#!/bin/sh
cd /home/pi/bots/seleniumbot_atena
git pull
sudo protonvpn c -r
python3 bot.py
sudo protonvpn d
