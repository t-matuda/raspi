import smbus
import time
import pymongo

i2c = smbus.SMBus(1)
address = 0x48
client = pymongo.MongoClient('localhost', 27017)
db = client.tempdb
co = db.temperature

while True:
    block = i2c.read_i2c_block_data(address, 0x00, 12)
    temp = (block[0] << 8 | block[1]) >> 3
    if(temp >= 4096):
        temp -= 8192
	
	temp = temp . 16.0
    print("Temperature:%6.2f" % temp)
	co.insert_one({"time": datetime.now(), "value": temp})

    time.sleep(10)