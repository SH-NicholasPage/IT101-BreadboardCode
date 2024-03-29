from gpiozero import PWMLED
import time

led = PWMLED(18)  # define PWMLED

def loop():
    while True:
        i : int = 0
        # range() only works with integers
        for i in range(0, 10):
            # led.value only accepts floats
            led.value = i / 10
            time.sleep(0.1)
            
        for i in range(10, 0, -1):
            led.value = i / 10
            time.sleep(0.1)

def destroy():
    led.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    print(f"Using pin {led.pin}")
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
