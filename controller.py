# Licensing for this software can be found
# In the working directory of this repository

import lgpio, time
import threading

# Initialize the library
chip = lgpio.gpiochip_open(0)

# Globals
TEMP = None
RUN = True

# Config values
DATA_PIN = 14 # GPIO (DATA) pin of the fan, not power or ground!
TEMP_MAX = 70 # The temperature in which the fans will turn on
RETURN_TEMP = 40 # The temperature to which the computer will cool down to once fans are activated (fans turn off after "RETURN_TEMP" is reached)
INTERVAL = 3 # Ticks between each temperature measure (not very precise)

def get_temp():
    """Get the CPU temperature in Celsius."""

    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
        global TEMP
        try:
            TEMP = float(file.read().strip()) / 1000.0
        except:
            TEMP = None

def thermometer():
    global RUN
    while RUN:
        get_temp()
        time.sleep(INTERVAL)

# Run the thermometer in a thread
thread = threading.Thread(target=thermometer)
thread.start()

try:
    while True:

        # Temp debugger (keep commented out for normal use)
        #print(str(TEMP)+"°", end='\r')

        if TEMP is not None:
            if TEMP >= TEMP_MAX:
                
                # If max temperature reached, run fans until return temp. is reached
                if TEMP > RETURN_TEMP:
                    lgpio.gpio_write(chip, DATA_PIN, 1)
                else:
                    lgpio.gpio_write(chip, DATA_PIN, 0)
            else:
                lgpio.gpio_write(chip, DATA_PIN, 0)
except:
    RUN = False
    lgpio.gpiochip_close(chip)