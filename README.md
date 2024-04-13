# ub-fanctl
Controll GPIO fans on a raspberry pi running Ubuntu

## System Requirements
* Ubuntu (currently tested on Ubuntu Server 22.04.4 LTS)
* lgpio (`sudo apt update && sudo apt install python3-lgpio`)

## Setup
* Clone this repo into your home directory (`echo $HOME` if you dont know your home directory)
* Edit "rc.local" file and include this line (before the `exit 0` line:):
    - ~/ub-fanctl/controller.py&