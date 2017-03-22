# Pull base image.
FROM nonoroazoro/rpi-mongo

# Install python and some modules
RUN apt-get update && \
    apt-get install -y python && \
    apt-get install -y python-smbus && \
    apt-get install -y i2c-tools && \
    apt-get install -y git-core && \
    apt-get install -y wget 

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    python -m pip install pymongo==3.0.3

RUN git clone https://github.com/t-matuda/raspi.git

# Define default command.
#CMD ["", "python", "raspi/temperature/insertTemp.py"]
#CMD ["bash"]
#CMD mongod --fork --logpath /data/db/mongod.log --repair && python raspi/temperature/insertTemp.py
CMD mongod && bash

