## Run docker

docker run -it --rm -v /mnt/data/supervisor/homeassistant/esphome:/esphome ubuntu:22.04 bash

## Install build tools

apt update && apt install -y build-essential cmake git python3

## Build tests
cd /esphome/Daikin-Rotex-HPSU-CAN/test/
mkdir build
cd build
cmake ..
make

## Run tests
./hpsu_tests_tests
