#!/bin/bash
mongod --fork --logpath /data/db/mongod.log --repair
python raspi/temperature/insertTemp.py
