# Licensing for this software can be found
# In the working directory of this repository

import lgpio, time
import threading
import subprocess

# Initialize the library
chip = lgpio.gpiochip_open(0)

# Booleans
TEMP = None
RUN = True
FAN_RUNNING = None
TICKER = False

# Config values
DATA_PIN = 14 # GPIO (DATA) pin of the fan, not power or ground!
TEMP_MAX = 60 # The temperature in which the fans will turn on
RETURN_TEMP = 40 # The temperature to which the computer will cool down to once fans are activated (fans turn off after "RETURN_TEMP" is reached)
INTERVAL = 1 # Seconds between each temperature measure

# Get the state of the fan
state = lgpio.gpio_read(chip, DATA_PIN)

if state != 1:
    # If there is no signal from the fan pin, do not run
    print("[ub-fanctl] - ERROR: No signal from fan, check pin configuration")
    exit(1)

def ticker():
    '''Function for allowing print statements to be ran ona timed interval without threading'''

    global TICKER
    while RUN:
        TICKER = True
        time.sleep(3)

def thermometer():
    global TEMP

    while RUN:
        # Get the temperature of the computer
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            TEMP = int(float(file.read().strip()) / 1000.0)

        time.sleep(INTERVAL)

# Run the thermometer in a thread
thermometer_thread = threading.Thread(target=thermometer)
thermometer_thread.start()

ticker_thread = threading.Thread(target=ticker)
ticker_thread.start()

try:
    # Reset GPIO pin by turning the fan off
    lgpio.gpio_write(chip, DATA_PIN, 0)
    FAN_RUNNING = False

    while True:
        if TEMP is not None:
            if TEMP >= TEMP_MAX and not FAN_RUNNING:
                # If max temperature reached + fans not running, spin up fans
                lgpio.gpio_write(chip, DATA_PIN, 1)
                FAN_RUNNING = True

            elif TEMP <= RETURN_TEMP and FAN_RUNNING:
                # If fans are running and the return temp has been reached, stop spinning fans
                lgpio.gpio_write(chip, DATA_PIN, 0)
                FAN_RUNNING = False
            if TICKER:
                print(str(TEMP)+"° |", "Fan:", "On" if FAN_RUNNING else "Off")
                TICKER = False

except KeyboardInterrupt:
    pass
except Exception as e:
    print(e)
finally:
    RUN = False
    
    # Turn off fan and close chip
    lgpio.gpio_write(chip, DATA_PIN, 0)
    lgpio.gpiochip_close(chip)
