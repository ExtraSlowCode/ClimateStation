Note; keep below 25k characters pls

# ClimateStation

**Author: Noa Cluer, nc222iw**

### Table of Contents
- [ClimateStation](#climatestation)
  - [Overview](#overview)
  - [Time approximation](#time-approximation)
- [Objective](#objective)
- [Material](#material)
  - [Material List](#material-list)
  - [Components](#components)
- [Software setup](#software-setup)
- [Hardware setup](#hardware-setup)
- [Platform](#platform)
- [Code](#code)
- [Data transmission](#data-transmission)
- [Data presentation](#data-presentation)
- [Final result](#final-result)
- [Credit & Sources](#credits--sources)


### Overview
  This IoT project was made as part of the course **Applied Internet of Things 1DT305**, to explore the range of options for monitoring indoor climate. In this project I have connected a number of sensors to a measuring station, which is uploading data to an online viewing page, in order to get an overview of said climate.

### Time approximation
  To construct your own ClimateStation might take as little as **2 hours** if no problems occur. But, such a scenario is highly unlikely, so the **greater part of an afternoon** is a more realistic estimation. The process can be quickened when connecting multiple ClimateStations, since parts of the setup can be reused between the stations.

## Objective
The basis of the idea behind the project originated in me wanting to explore the limits of using very simple sensors to acquire relevant data. This, in combination with me having recently moved into a restored house, curious about the indoor climate here, resulted in the idea of this climate measurement device.

The **ClimateStation** measures the current relative light level of the area, the relative air humidity, and the ambient temperature using three different sensors (for the benefit of comparison). All the data is then uploaded to the cloud where it can be viewed in datacake, plotted in a graph with previous measurements. This way, the data can be easily analysed and taken upon consideration when making further restorations of the house, or simply be noted for peace of mind and everyday discussions.

~~Why you chose the project?~~

~~What does the project do? (measurements etc)~~

~~What will it give you?~~

## Material

### Material list
Table of contents for original prototype development:

|Amount|Name                          |buy-link   |price  |
|---|------------------------------|-----------|-------|
|1x |Raspberry Pi Pico WH          |[Electrokit](https://www.electrokit.com/raspberry-pi-pico-wh)|99,00 SEK|
|1x |DHT11                         |[Electrokit](https://www.electrokit.com/temp/fuktsensor-dht11)|39,00 SEK|
|1x |MCP9700 TO-92                 |[Electrokit](https://www.electrokit.com/mcp9700-to-92-temperaturgivare)|10,50 SEK|
|1x |Photoresistor CdS 4-7kΩ       |[Electrokit](https://www.electrokit.com/fotomotstand-cds-4-7-kohm)|9,50 SEK|
|1x |Yellow LED 5mm diffuse 1500mcd|[Electrokit](https://www.electrokit.com/led-5mm-gul-diffus-1500mcd)|5,00 SEK (min 2)|
|1x |Resistor 0.25W 330Ω           |[Electrokit](https://www.electrokit.com/motstand-kolfilm-0.25w-330ohm-330r)|1,00 SEK (min 10)|
|1x |Breadboard                    |[Electrokit](https://www.electrokit.com/kopplingsdack-840-anslutningar)|69,00 SEK|
|1x |Wires (bundle)                |[Electrokit](https://www.electrokit.com/labbsladd-40-pin-30cm-hane/hane)|55,00 SEK|
|Total:|||288,00 SEK|


~~Table of names, where I bought them, and what they cost~~

### Components
**The Raspberry Pi Pico WH** is a MCU unit with integrated WiFi support, and pre-soldered header pins. It is highly flexible, cost-efficient, and widely used in IoT devices across the world. It is also the MCU unit that I've used the most previously, and the one included in the package of recommended hardware for this course<sup>1</sup>. In this project, I also utilize it's on-board LED, and temperature sensors. The RPI Pico W has two cores, runs using the RP2040 chip, and has 2MB flash memory<sup>2</sup>.

**DHT11** is a digital temperature and humidity sensor, appreciated for it's simplicity and usability. It too was part of the recommended course hardware package, and I had 

## Software setup
Chosen IDE
How to download the IDE
How to flash the MCU
How to upload code/testrun

## Hardware setup
Circuit diagram
Breadboard photo
Describe differences in version used in idustrial setting (soldered directly onto the MCU)
Electrical Calculations (power consumption?, discussion on power LED resistor preference?, on photoresistor sensitivity?) (optional point)

## Platform
Why datacake? Why WiFi? Any other simple options? Perks/downsides of free subsription (upload rate, data retention). Ease of connecting further devices. Why online data holding? (datacake) (difficulty of upholding a server for data display). Showcase example dashboard menu with it's functions. Explain how to configure device and input (fields ex.) (focus on platform simplicity and flexibility/function, not the actual data/layout)

## Code
Class diagram? (almost single file)
Pseudocode of event order
Define library functionalities
Doing anything fancy/unusual in the code? (small show off)
REMEMBER MENTIONING/LINKING SOURCES!

```python=
import whatever

def funct():
  test

s.send(p)

# test
```

Device deployment diagram

## Data transmission
Upload frequency (and how to tweak it in the code). And why it was set as such (datacake limits, and DHT read rate)
Data transmission type (html)

The transmission steps. Call stack order ig? (measurement, html constuction, package construction, post request, deconstructor, datacake field unpacking/management) (note utilization of WiFi, what transport protocol I'm using)

The up and downsides of these choices on device range and battery use.

## Data presentation
Screenshot of dashboard, with examples, circle zones etc
Note the current data retention (7 days?)
Note data update frequency, same as upload? (5mins?)

## Final Result
Image of final prototype, CAD and deployed?
My thoughts on the results (went well/not)
Things to improve

## Credits & Sources
Name the people writing the borrowed code. (HackMD repo owners?)

<sup>1</sup> https://www.electrokit.com/lnu-starter

<sup>2</sup> https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html
