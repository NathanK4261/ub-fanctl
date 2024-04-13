#!/usr/bin/bash

# Licensing for this software can be found
# In the working directory of this repository

sudo apt-get install -y stress-ng

max_cpu=$(nproc) # Maximum CPU cores
max_io=$(grep -c processor /proc/cpuinfo) # Maximum IO operations (number of CPUs)
max_vm=$(free -m | awk '/Mem:/{print $2}') # Maximum available memory in MB

# Run stress-ng with the maximum values
clear; echo "Running a stress test using all system rescources..."
sudo stress-ng --cpu $max_cpu --io $max_io --vm $max_vm --vm-bytes 1G --timeout 120s

sudo apt-get purge -y stress-ng
sudo apt autoremove -y