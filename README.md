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


## Material

### Material list
Table of contents for original prototype development:

|Amount|Name                          |buy-link   |price  |
|---|------------------------------|-----------|-------|
|1x |Raspberry Pi Pico WH          |[Electrokit](https://www.electrokit.com/raspberry-pi-pico-wh)|99,00 SEK|
|1x |DHT11                         |[Electrokit](https://www.electrokit.com/temp/fuktsensor-dht11)|39,00 SEK|
|1x |MCP9700 TO-92<sup>5</sup>                |[Electrokit](https://www.electrokit.com/mcp9700-to-92-temperaturgivare)|10,50 SEK|
|1x |Photoresistor CdS 4-7kΩ       |[Electrokit](https://www.electrokit.com/fotomotstand-cds-4-7-kohm)|9,50 SEK|
|1x |Yellow LED 5mm diffuse 1500mcd|[Electrokit](https://www.electrokit.com/led-5mm-gul-diffus-1500mcd)|5,00 SEK (min 2)|
|1x |Resistor 0.25W 10kΩ           |[Electrokit](https://www.electrokit.com/motstand-kolfilm-0.25w-10kohm-10k)|1,00 SEK (min 10)|
|1x |Resistor 0.25W 330Ω           |[Electrokit](https://www.electrokit.com/motstand-kolfilm-0.25w-330ohm-330r)|1,00 SEK (min 10)|
|1x |Breadboard                    |[Electrokit](https://www.electrokit.com/kopplingsdack-840-anslutningar)|69,00 SEK|
|1x |Wires (bundle)                |[Electrokit](https://www.electrokit.com/labbsladd-40-pin-30cm-hane/hane)|55,00 SEK|
|**Total:**|*(excluding some duplicates)*||**289,00 SEK**|

### Components
**The Raspberry Pi Pico WH** is a MCU unit with integrated WiFi support, and pre-soldered header pins. It is highly flexible, cost-efficient, and widely used in IoT devices across the world. It is also the MCU unit that I've used the most previously, and the one included in the package of recommended hardware for this course<sup>1</sup>. In this project, I also utilize it's on-board LED, and temperature sensors. The RPI Pico W has two cores, runs using the RP2040 chip, and has 2MB flash memory<sup>2</sup>.

**DHT11** is a digital temperature and humidity sensor, appreciated for it's operability and user-friendliness. It too was part of the recommended course hardware package, and I had previous experience using it. Boasting a precision of ±1°C the DHT11 is also quite precise for its cost.

**MCP9700 TO-92** is an analog alternative to the more complicated temperature sensors. Thanks to its structural simplicity it is much cheaper, but also comes with the reduced precision of "only" ±2°C in comparison with the DHT11. It also doesn't have an integrated humidity sensor, and the analog value has to be manually converted into a digital temperature reading.

**A photoresistor** such as the CdS 4-7kΩ, is a resistor that varies its resistance based on the surrounding light. The current is conducted over a light-sensitive membrane, increasing the resistance with surrounding brightness. 

**LEDs** light up, easily controlled via GPIO pins.

**Resistors** add resistance to the circuit, mostly to protect sensitive components.

**A breadboard** is used to attach components during prototype development, since it allows you to move them around while maintaining function.

**Wires**: everyone knows what a wire does.


## Software setup
I chose to use **Thonny** as my IDE for the software part of this project, looking for simplicity. To download and set up the IDE, follow these steps.

* Get the latest Thonny [download exe](https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe) for your computer's operating system.

* Open the .exe file, that most likely gets placed in your downloads folder.

![image](./img/thonny_exe.png)

* Get through the install wizard, and launch the program.

* Whilst holding down the bootsel button<sup>3</sup> on the RPI Pico, connect it to your computer.

* Then, install micropython on the RPI Pico, using the lower right menu. *(The text will look slightly different)*

![image](./img/thonny_menu.png)
* Choose the correct version of the micropython<sup>4</sup>. *(The current latest version is v1.25.0)*

![link](https://static1.xdaimages.com/wordpress/wp-content/uploads/2024/12/thonny-install-micropython-dialog.jpg?q=70&fit=crop&w=825&dpr=1)

* Click the stop button, and then (when the device is recognized) run the relevant file.

![image](./img/thonny_start.png)

* When you have a working file, save **main.py** to the RPI Pico, it has to be named that for micropython to recognize it on startup, and then simply plug the ClimateSensor into any usb power outlet. *(The WiFi-login credentials are stored in another file **keys.py** that you also have to upload to the RPI Pico before unplugging, see [Code](#code))*

![image](./img/board_save.png)

* *Note: you might have to unplug, and reconnect the device if the on-board LED hasn't lit up a few seconds after the yellow LED start-sequence is done. If the on-board LED is not lit, it means that the device hasn't successfully connected to WiFi yet. I had some issues with that, but reconnecting the power cable solved the issue.*

## Hardware setup
A diagram of the circuit *(with some components only labeled)*<sup>7</sup>:

![image](./img/circuit.png)

Image of the board setup *(notice the on-board LED being lit while the program is running)*:

![image](./img/board.jpg)

The slight mess of wiring could of course be improved greatly by simply soldering the project onto a perf board, maybe along the lines of the below image, a good first step if bringing the ClimateStation into a more industiral setting. By soldering onto a perf board, or even directly to the RPI Pico, a lot of space is saved making it possible to fit into a case of some kind.

![image](./img/board_solder.png)

### Calculations
Most sections of this project where quite straight forward, but especially the daylight sensor needed some calculations. Based on it's range (4-7kΩ), I opted for a 10kΩ resistor as comparison. This after recommendation<sup>6</sup>, lead to the photoresistor outputting a voltage range of around 0-3.2, based on the local surrounding brightness. This sensitivity range can be offset by changing the reference resistor.

Since the *ClimateStation* is supposed to be plugged into a power outlet, little detailed considerations on exact power consumption have been made, but it should be rather low. The program spends around 0.5 seconds measuring and transmitting data, and then 15 minutes in timer sleep. This means that the "efficient" uptime is only around 0.056%, and the remaining time spent waiting.


## Platform
Firstly, I chose to explore using WiFi to directly transfer the data over the internet. This choice was quite handy, seeing as my intended placement of the *ClimateStation* was in my office-like room, right by my router. This avoided the main downside of using WiFi, the limited range. And as previously mentioned, the project is at all times connected to a power outlet, meaning the higher energy consumption that comes from communication via WiFi, will not really affect it.

Then, as a data viewing platform, I chose datacake. Mostly for its simple interface, and due to previous experience with the program. There was also quite a bit of code examples of how to interface with datacake using http, instead of the more commonly used partner within IoT spaces, LoRaWAN. Datacake has a generous free-tier<sup>8</sup> of up to 5 connected devices, and a data retention of 7 days. This is all that is needed to create a proof of concept for this project, and to have basic every-day use of the device. You can then create dashboards of your device data, that in a simple and clear way convert the data to e.g. graphs. But the greatest benefit might very well be to not have to have a server device running constantly from home, seeing as datacake is a cloud service. 

*Device menu in datacake*
![image](./img/datacake_add_device.png)

*A dashboard in datacake<sup>9</sup>*
![image](./img/datacake-integration-dashboard-650x363-1413818344.png)

If this project was to be scaled, or simply more time invested into it, other platform compositions could be considered. The one I was most tempted by was using WiFi with a self-hosted ELK-stack<sup>10</sup>. This setup would have been way more scaleable, and given even more control to the backend owner (you). It would also have meant exploring a more complex and interesting option than datacake. By hosting the data storage server yourself, you would for example not necessarily have been limited to the 7 days of data retention, or set upload rate (500 uploads/day with free tier of datacake).


## Code
**Firstly**, for the code to work, you have to fill in your WiFi networks SSID and PASSWORD in [```keys.py```](./src/keys.py). The program was constructed this way as to in a simple manner retain the network privacy.

All of the required code is in the /src package, even the [micropython.uf2](https://micropython.org/resources/firmware/RPI_PICO-20250415-v1.25.0.uf2)-file<sup>11</sup> needed to run .py files *(most likely already installed via the Thonny IDE as per [above](#software-setup))*. So you could simply download the files [`keys.py`](./src/keys.py), [`main.py`](./src/main.py), and [`RPI_PICO-v1.25.0.uf2`](./src/RPI_PICO-v1.25.0.uf2), change the network credentials in `keys.py`, and then save them all on your RPI Pico. 

*In essence, the program consists of the following:*

![image](./img/class_diagram.png)

*Feel free to check out the code files, they are not that cumbersome.*

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

<sup>3</sup> https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf

<sup>4</sup> https://static1.xdaimages.com/wordpress/wp-content/uploads/2024/12/thonny-install-micropython-dialog.jpg?q=70&fit=crop&w=825&dpr=1

<sup>5</sup> https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP970X-Family-Data-Sheet-DS20001942.pdf

<sup>6</sup> Thanks to [Antrakasus](https://github.com/Antrakasus) for help with the photoresistor sensitivity offset issue.

<sup>7</sup> https://www.circuit-diagram.org/editor/

<sup>8</sup> https://datacake.co/pricing

<sup>9</sup> https://blog.golioth.io/wp-content/uploads/2022/03/datacake-integration-dashboard.png

<sup>10</sup> https://hackmd.io/q1u1hr45S-uvJCXz05aRLw

<sup>11</sup> https://micropython.org/download/RPI_PICO/