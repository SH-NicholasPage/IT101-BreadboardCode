# KY-008 Laser Transmitter + Laser Receiver

![KY-008 Laser Transmitter + Laser Receiver](https://content.instructables.com/FGZ/QTNT/I8WW0ND8/FGZQTNTI8WW0ND8.jpg?auto=webp&frame=1&fit=bounds&md=f07a04d7b6dc7613f864d187443afff6)

## Overview

The KY-008 Laser Transmitter module is a commonly used component in Arduino and Raspberry Pi projects for emitting a small laser beam. Paired with the Laser Receiver module, it enables the detection of this emitted laser beam. This combination is widely used in various DIY projects, including robotics, security systems, and interactive installations.

This repository provides basic information about the KY-008 Laser Transmitter + Laser Receiver module, including pinout, sample code, and external documentation.

**Note:**

The transmitter likely won't receive enough power from a GPIO or Arduino digital output pin alone. For consistent performance, it's recommended to use the 5V pin directly as the signal pin, effectively powering the laser continuously.

## Documentation

- [KY-008 Laser Transmitter Module Information](https://arduinomodules.info/ky-008-laser-transmitter-module/)
- [Instructables Guide on KY-008 Laser Module + Laser Detector](https://www.instructables.com/KY-008-Laser-Module-x-Laser-Detector-x-ISD1820-Voi/)

## Pinout

The KY-008 module typically has three pins:

- **S** (Signal): Connects to a digital pin on the Pi/Arduino for sending control signals. _(Or directly to 5V for continuous power.)_
- **+** (Power): Connects to the 5V pin on the Pi/Arduino for supplying power.
- **-** (Ground): Connects to the GND pin on the Pi/Arduino for grounding.

Note that the pinout for the receiver is the same as for the transmitter, making it easy to wire and swap between them if needed.
