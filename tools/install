#!/usr/bin/bash

# Licensing for this software can be found
# In the working directory of this repository

# Run this script after setting up service file
# NOTE: Run in directory "tools"

# Install libraries and transfer service file
sudo apt-get python3-lgpio
sudo mv ub-fanctl.service /etc/systemd/system

# Reload daemon and print operation ststus
sudo systemctl daemon-reload && sudo systemctl enable ub-fanctl && sudo systemctl start ub-fanctl
sudo systemctl status ub-fanctl