# 3144E A3144 Hall Effect Sensor Module

This module uses the 3144E (A3144-compatible) Hall effect sensor to detect the presence of a magnetic field. It outputs a digital voltage signal that can be used in Arduino, PIC, AVR, and other microcontroller projects.

## Features

- **Sensor Type:** Hall Effect
- **Model:** 3144E (A3144-compatible)
- **Voltage:** 5V DC
- **Output Type:** Digital (High/Low)
- **Operating Principle:** Magnetic induction
- **Output:** Logic LOW when magnetic field is detected, HIGH when not detected
- **Interface:** 3-pin (VCC, GND, Signal)
- **Mounting:** DIN Rail Mount

## Pinout

| Pin | Label | Description        |
|-----|-------|--------------------|
| 1   | VCC   | Power supply (5V)  |
| 2   | GND   | Ground             |
| 3   | OUT   | Digital signal out |

## How It Works

The 3144E Hall effect sensor detects changes in magnetic field intensity. When a magnet is near the sensor:

- The **OUT** pin goes **LOW** (0V).
- When the magnet is removed, **OUT** goes **HIGH** (5V).

This allows you to detect magnetic proximity and create switches, counters, speed sensors, or rotational detectors.

## Notes

- Operates on 5V DC only
- Output is not analog, only digital HIGH/LOW