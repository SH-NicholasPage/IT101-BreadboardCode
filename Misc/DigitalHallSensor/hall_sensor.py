import RPi.GPIO as GPIO
import time

HALL_PIN = 18  # GPIO18

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(HALL_PIN, GPIO.IN)
    print("Waiting for magnetic field...")
    
def loop():
    while True:
        if GPIO.input(HALL_PIN) == GPIO.LOW:
            print("Magnet detected!")
        else:
            print("No magnet.")
        time.sleep(0.5)
    
def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        destroy()
