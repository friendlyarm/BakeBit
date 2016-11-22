#! /bin/bash
echo "Welcome to BakeBit Installer."
echo " "
echo "Requirements:"
echo "1) Must be connected to the internet"
echo "2) This script must be run as root user"
echo " "
echo "Steps:"
echo "Installs package dependencies:"
echo "   - python2.7        python2.7"
echo "   - python-pip       alternative Python package installer"
echo "   - git              fast, scalable, distributed revision control system"
echo "   - libi2c-dev       userspace I2C programming library development files"
echo "   - python-serial    pyserial - module encapsulating access for the serial port"
echo "   - i2c-tools        This Python module allows SMBus access through the I2C /dev"
echo "   - python-smbus     Python bindings for Linux SMBus access through i2c-dev"
echo "   - minicom          friendly menu driven serial communication program"
echo "   - psutil           a cross-platform process and system utilities module for Python"
echo " "
echo " NanoPi will reboot after completion."
echo " "
echo " "
sleep 5

echo " "
echo "Check for internet connectivity..."
echo "=================================="
wget -q --tries=2 --timeout=100 http://www.baidu.com -O /dev/null
if [ $? -eq 0 ];then
	echo "Connected"
else
	echo "Unable to Connect, try again !!!"
	exit 0
fi

USER_ID=$(/usr/bin/id -u)
USER_NAME=$(/usr/bin/who am i | awk '{ print $1 }')
SCRIPT_PATH=$(/usr/bin/realpath $0)
DIR_PATH=$(/usr/bin/dirname ${SCRIPT_PATH} | sed 's/\/Script$//')

if [ ${USER_ID} -ne 0 ]; then
    echo "Please run this as root."
    exit 1
fi

echo " "
echo "Installing Dependencies"
echo "======================="
sudo apt-get install python2.7 -y
sudo apt-get install python-pip git libi2c-dev python-serial i2c-tools python-smbus minicom python-dev -y

if [ -d RPi.GPIO-0.5.11 ]; then
    cd RPi.GPIO-0.5.11
    python setup.py install
    cd ..
fi

if [ -d psutil-0.5.0 ]; then
    cd psutil-0.5.0
    python setup.py install
    cd ..
fi

echo "Dependencies installed"

if [ -d wiringPi ]; then
    cd wiringPi
    git pull
else
    git clone git://git.drogon.net/wiringPi
    cd wiringPi
fi

./build
RES=$?

if [ $RES -ne 0 ]; then
  echo "Something went wrong building/installing wiringPi, exiting."
  exit 1
fi

echo "wiringPi Installed"

sudo adduser ${USER_NAME} i2c

echo " "
echo "Install smbus for python"
sudo apt-get install python-smbus -y

echo " "
echo "Making libraries global . . ."
echo "============================="
if [ -d /usr/lib/python2.7/dist-packages ]; then
    sudo cp ${DIR_PATH}/Script/bakebit.pth /usr/lib/python2.7/dist-packages/bakebit.pth
else
    echo "/usr/lib/python2.7/dist-packages not found, exiting"
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
