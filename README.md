# ub-fanctl
Controll GPIO fans on a raspberry pi running Ubuntu

## System Requirements
* Ubuntu (currently tested on Ubuntu Server 22.04.4 LTS)
* lgpio (`sudo apt update && sudo apt install python3-lgpio`)

## Install
* Clone this repo into your home directory (`echo $HOME` if you dont know your home directory)
* Edit systemd file:
    - Open "ub-fanctl.service" in your text editor of choice
    - You will see some data values you need to fill in, fill these in according to your system.
        - Here is an example:
        - ```
            [Unit]
            Description=Ubuntu Fan Controller (Made By: Nathan D. Keidel)
            After=network.target
                        
            [Service]
            User=john
            Group=john

            WorkingDirectory=/home/john/ub-fanctl/
            ExecStart=/usr/bin/python3 /home/john/ub-fanctl/controller.py

            Restart=always
            RestartSec=5

            AmbientCapabilities=CAP_SYS_RAWIO CAP_SYS_ADMIN
            CapabilityBoundingSet=CAP_SYS_RAWIO CAP_SYS_ADMIN
                        
            [Install]
            WantedBy=multi-user.target
          ```
    - `cd` into the "tools" directory
    - Run these commands:
        - ```
            sudo chmod +x *
            ./install
          ```
    ub-fanctl should not be installed on your system. A reboot might be needed.

## Uninstall
To uninstall ub-fanctl:
* `cd` into the "tools" directory
* Run command: `./uninstall`
* RECOMMENDED: Remove symbolic links listed after uninstalling ub-fanctl

Now, delete the working directory (ub-fanctl) and you have completed the uninstallation.

## Stress Test
I provided a simple stress test script that:
1. Installs stress-ng
2. Runs a stress test using all system resources (computer might become unresponsive)
3. Purges stress-ng and its dependencies from your system

To run, navigate to the "tools" directory and run the stress test:
* `./stress-test`
