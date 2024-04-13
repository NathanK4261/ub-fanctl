#!/usr/bin/bash

# Licensing for this software can be found
# In the working directory of this repository

# Run this script to remove ub-fanctl from systemd
# NOTE: Run in directory "tools"

sudo systemctl disable ub-fanctl && sudo systemctl stop ub-fanctl

# Move service file out of systemd
sudo mv /etc/systemd/system/ub-fanctl.service .

# Reload daemon
sudo systemctl daemon-reload

clear

echo "Here are related symbolic links to ub-facntl that you might want to delete"
find / -type l -ls 2>/dev/null | grep ub-fanctl