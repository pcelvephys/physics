#!/bin/bash
pip install --upgrade pip
pip install pyusb
pip install python-usbtmc

addgroup usbtmc
usermod -a -G usbtmc lab
usermod -a -G usbtmc pi

echo SUBSYSTEMS=="usb", ACTION=="add", ATTRS{idVendor}=="05ff", ATTRS{idProduct}=="1023", GROUP="usbtmc", MODE="0660" >> /etc/udev/rules.d/usbtmc.rules

echo Edit file /etc/udev/rules.d/usbtmc.rules to set appropriate vendor and product ids
dmesg | tail
read
nano /etc/udev/rules.d/usbtmc.rules
