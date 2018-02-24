#!/bin/bash

apt-get upgrade
apt-get install -y docker

docker build momma-dog:latest .
docker run --device /dev/i2c-1 -p 8000:8000 momma-dog