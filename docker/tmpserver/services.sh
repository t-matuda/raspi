#!/bin/bash
sudo mongod --fork --logpath /data/db/mongod.log --repair
sudo python raspi/temperature/insertTemp.py
