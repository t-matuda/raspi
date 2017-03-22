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

RUN apt-get install -y vim

RUN ln -sf  /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

ADD insertTemp.py /data/ 

# Define default command.
CMD ["python", "insertTemp.py"]
#CMD ["bash"]
