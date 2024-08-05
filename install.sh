#!/bin/bash

user_id=$(id -u)

if [[ $user_id -eq 0 ]]; then

echo -e "\n[+] Verifying if the xclip dependency is installed.\n"

sleep 1

if which xclip > /dev/null 2>&1; then
    echo -e "\n[v] Dependency xclip is installed.\n"

    sleep 1
else
    echo -e "\n[X] The dependency xclip is not installed. Proceeding with the installation.\n"

    apt install xclip && echo -e "[v] xclip has been installed successfully."

fi

echo -e "\n[*] Installing getPorts...\n"

sleep 1

chmod +x ./getPorts.py

cp ./getPorts.py /usr/local/bin/getPorts

echo -e "\n[v] getPorts was successfully installed in '/usr/local/bin/'\n"

echo -e "\n[i] To use it, run 'getPorts' in your shell."

else
  
echo -e "\n[!] Root privileges are required to run this script and complete the installation.\n"

fi
