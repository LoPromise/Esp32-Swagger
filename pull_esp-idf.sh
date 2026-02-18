#!/bin/bash
exec git clone -b v5.1.7 --recursive https://github.com/espressif/esp-idf.git esp-idf-v5.1.7
cd esp-idf*
./install.sh esp32
cp -r esp-idf*/examples/get-started/hello_world .