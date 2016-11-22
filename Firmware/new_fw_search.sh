#! /bin/bash
printf "Welcome to BakeBit Firmware Update Check.\n=========================================\nPlease ensure internet connectivity before running this script.\n"
echo "Must be running as Root user"
echo "Press any key to begin..."
read

echo "Check for internet connectivity..."
echo "=================================="
wget -q --tries=2 --timeout=20 --output-document=/dev/null http://baidu.com
if [[ $? -eq 0 ]];then
	echo "Connected"
else
	echo "Unable to Connect, try again !!!"
	exit 0
fi

wget http://wiki.friendlyarm.com/bakebit/Firmware/version.txt -O temp_f &>/dev/null
diff -q version.txt temp_f
if [[ $? == "0" ]]
then
  echo "You have the latest firmware"
else
  printf "\nNew firmware available. \n\nDownload the new version from BakeBit Github Repo.\n"  
  printf "\nTo download the latest firmware, simply open a terminal session, change directories to the Github on your NanoPi, and type 'git remote update'.  This will pull the latest files from Github.  Then run this script again."
fi
rm temp_f
