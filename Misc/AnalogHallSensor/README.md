# 49E Linear Hall Sensor with ADS7830 ADC 

![image](https://github.com/user-attachments/assets/392debb1-253a-48f6-a2e7-f722c3ead351)

## Overview

This project reads analog voltage from a 49E linear Hall effect sensor using an ADS7830 I²C analog-to-digital converter (ADC) connected to a Raspberry Pi. It converts the analog reading into a voltage and logs the output to the console.

The setup is suitable for measuring magnetic field strength variations as voltage changes and is ideal for educational demonstrations, testing analog sensors, or interfacing Hall effect sensors with I²C-only systems like the Raspberry Pi.

## Pinout

### 49E Hall Effect Sensor

| Pin | Label | Description                                 |
|-----|-------|---------------------------------------------|
| 1   | VCC   | Power supply (3.3V or 5V)                   |
| 2   | GND   | Ground                                      |
| 3   | OUT   | Analog signal out (connect to A0-A7 on ADC) |

See this image below to better understand the pinout:

![image](https://github.com/user-attachments/assets/e7d05e30-0e40-4d89-afd6-e644100e6063)

### ADS7830 ADC

Refer to your module's datasheet or the ADC lab handout. Most I²C ADS7830 boards use the address 0x4B, including the one you received in your kit.

## How It Works

The 49E linear Hall effect sensor outputs a variable analog voltage based on the strength of the magnetic field detected. Unlike digital sensors that switch HIGH or LOW, this sensor provides continuous voltage readings that correspond to field strength and polarity.

- When no magnet is present, the output voltage hovers around half of the supply voltage (e.g., ~2.5V with a 5V supply).
- As a south pole of a magnet approaches, the output voltage increases.
- As a north pole of a magnet approaches, the output voltage decreases.

This allows you to measure not only the presence of a magnetic field but also its strength and polarity, making it suitable for analog magnetic field sensing, current sensing (with proper configuration), and linear position detection.
