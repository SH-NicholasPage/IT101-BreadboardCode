from pathlib import Path
import sys
import time
import os

HERE = Path(__file__).parent.parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import *

USING_GRAVITECH_ADC = False  # Only modify this if you are using a Gravitech ADC

ADC = ADCDevice()  # Define an ADCDevice class object

ADC_REF_VOLTAGE = 5.0  # Sensor is powered by 5V

# Define thresholds from high to low; stronger fields = lower values
EMF_THRESHOLDS = [125, 118, 111, 103, 96, 89, 82, 74, 67, 60]

def clear_terminal():
    os.system('clear')

def setup():
    global ADC
    if ADC.detectI2C(0x48) and USING_GRAVITECH_ADC:
        ADC = GravitechADC()
    elif ADC.detectI2C(0x48):  # PCF8591
        ADC = PCF8591()
    elif ADC.detectI2C(0x4b):  # ADS7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found.\n"
              "Please use 'i2cdetect -y 1' to verify.\n"
              "Exiting.")
        exit(-1)

def emf_level(analog_value):
    """
    Maps the analog value (expected range ~60–130) to an EMF level between 0 and 10.
    Lower analog values indicate stronger magnetic fields.
    """
    for level, threshold in enumerate(EMF_THRESHOLDS):
        if analog_value >= threshold:
            return level
    return 10  # Strongest field (analog value < lowest threshold)


def display_emf_meter(level, analog_value):
    bar = "|" * level + "-" * (10 - level)
    print(f"[{bar}] EMF Level: {level}/10 | Raw: {analog_value}")

def loop():
    while True:
        analog_value = ADC.analogRead(0)
        level = emf_level(analog_value)

        clear_terminal()
        print("Very real EMF Detector\n")
        display_emf_meter(level, analog_value)

        if level >= 8:
            print("Warning: High electromagnetic activity!")
        elif level >= 5:
            print("Moderate field detected.")
        else:
            print("Normal ambient level.")
        
        time.sleep(0.3)

def destroy():
    global ADC
    ADC.close()

if __name__ == '__main__':
    print('Starting EMF Detector...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("\nExiting...")
