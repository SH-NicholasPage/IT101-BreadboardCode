from pathlib import Path
import sys
import time

HERE = Path(__file__).parent.parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC
ADC_REF_VOLTAGE = 5.0  # Adjust based on your ADC's actual reference voltage (3.3 or 5.0)

ADC = ADCDevice() # Define an ADCDevice class object

def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
    
def loop():
    while True:
        analogValue = ADC.analogRead(0)  # Read from analog channel 0
        voltage = analogValue / 255.0 * ADC_REF_VOLTAGE  # Convert to voltage
        print(f"Analog Value: {analogValue}, Voltage: {voltage:.2f}V")
        time.sleep(0.2)

def destroy():
    global ADC
    ADC.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        