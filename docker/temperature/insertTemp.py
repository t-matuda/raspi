import os
import smbus
import time
import pymongo
from datetime import datetime

i2c = smbus.SMBus(1)
address = 0x48
ip =os.getenv("MONGO_PORT_27017_TCP_ADDR", "172.17.0.2")
port =int(os.getenv("MONGO_PORT_27017_TCP_PORT", "27017"))
client = pymongo.MongoClient(ip, port)
db = client.tempdb
co = db.temperature

while True:
    block = i2c.read_i2c_block_data(address, 0x00, 12)
    temp = (block[0] << 8 | block[1]) >> 3
    if(temp >= 4096):
        temp -= 8192
	
    temp = temp / 16.0
    print("Temperature:%6.2f" % temp)
    co.insert_one({"time": datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "value": temp})

    time.sleep(900)
