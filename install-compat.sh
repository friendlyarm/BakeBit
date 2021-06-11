#!/bin/bash
set -o errexit -o nounset

echo ""
echo "Welcome to BakeBit Installer."
echo ""
echo "Requirements:"
echo "1) Must be connected to the internet"
echo "2) This script must be run as root user"
echo " "
echo "Steps:"
echo "Installs package dependencies:"
echo "   - i2c-tools        This Python module allows SMBus access through the I2C /dev"
echo "   - libi2c-dev       userspace I2C programming library development files"
echo "   - minicom          friendly menu driven serial communication program"
echo "   - git              fast, scalable, distributed revision control system"
echo "   - python3          interactive high-level object-oriented language, Python3 version"
echo "   - python3-dev      header files and a static library for Python3"
echo "   - python3-pip      alternative Python3 package installer"
#echo "   - python3-smbus    Python3 bindings for Linux SMBus access through i2c-dev"
#echo "   - python3-rpi.gpio Module to control Raspberry Pi GPIO channels for Python3"
echo "   - python3-serial   pyserial - module encapsulating access for the serial port"
echo "   - python3-psutil   a cross-platform process and system utilities module for Python3"
echo "   - python3-pil      Python Imaging Library (Python3)"
echo "   - WiringNP         a GPIO access library for NanoPi NEO/NEO2"
echo ""
echo " NanoPi will reboot after completion."
echo ""
sleep 5

echo ""
echo "Checking Internet Connectivity..."
echo "================================="
wget -q --tries=2 --timeout=100 http://www.baidu.com -O /dev/null
if [ $? -eq 0 ];then
    echo "Connected"
else
    echo "Unable to Connect, try again !!!"
    exit 0
fi

USER_ID=$(id -u)
USER_NAME=$(whoami)
REAL_PATH=$(realpath $(dirname $0))

echo ""
echo "Checking User ID..."
echo "==================="
if [ ${USER_ID} -ne 0 ]; then
    echo "Please run this script as root, try 'sudo ./install.sh'"
    exit 1
fi
echo ""
echo "Checking for Updates..."
echo "======================="
sudo apt-get update --yes

echo ""
echo "Installing Dependencies"
echo "======================="
sudo apt-get install i2c-tools libi2c-dev minicom git -y
#sudo apt-get install python3 python3-dev python3-smbus python3-serial python3-rpi.gpio python3-psutil python3-pil -y
sudo apt-get install python3 python3-dev python3-pip python3-serial python3-psutil python3-pil -y
yes | sudo pip3 install smbus
yes | sudo pip3 install RPi.GPIO
echo "Dependencies installed"

echo ""
echo "Installing WiringNP..."
echo "======================="
if [ ! -d WiringNP ]; then
    git clone --depth=1 https://github.com/friendlyarm/WiringNP.git
fi

pushd WiringNP
git pull

if [ ! -f build ]; then
    echo "No module WiringNP, exiting."
    popd && exit 1
fi

sudo ./build
RET=$?

if [ $RET -ne 0 ]; then
    echo "Something wrong when building/installing WiringNP, exiting."
    popd && exit 1
fi

popd
echo "WiringNP Installed"

sudo adduser ${USER_NAME} i2c

echo " "
echo "Making libraries global..."
echo "=========================="
if [ -d /usr/lib/python3/dist-packages ]; then
    sudo echo "${REAL_PATH}/Software/Python/" > /usr/lib/python3/dist-packages/bakebit.pth
else
    echo "/usr/lib/python3/dist-packages not found, exiting"
    exit 1
fi

echo " "
echo "Please restart to implement changes!"
echo "  _____  ______  _____ _______       _____ _______ "
echo " |  __ \|  ____|/ ____|__   __|/\   |  __ \__   __|"
echo " | |__) | |__  | (___    | |  /  \  | |__) | | |   "
echo " |  _  /|  __|  \___ \   | | / /\ \ |  _  /  | |   "
echo " | | \ \| |____ ____) |  | |/ ____ \| | \ \  | |   "
echo " |_|  \_\______|_____/   |_/_/    \_\_|  \_\ |_|   "
echo " "
echo "Please restart to implement changes!"
echo "To Restart type sudo reboot"

echo "To finish changes, we will reboot the Pi."
echo "Pi must reboot for changes and updates to take effect."
echo "If you need to abort the reboot, press Ctrl+C.  Otherwise, reboot!"
echo "Rebooting in 5 seconds!"
sleep 1
echo "Rebooting in 4 seconds!"
sleep 1
echo "Rebooting in 3 seconds!"
sleep 1
echo "Rebooting in 2 seconds!"
sleep 1
echo "Rebooting in 1 seconds!"
sleep 1
echo "Rebooting now!  "
sleep 1
sudo reboot
