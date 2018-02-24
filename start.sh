#!/bin/bash

apt-get upgrade
apt-get install -y docker

docker build momma-dog:latest .
docker run -p 8000:8000 momma-dog