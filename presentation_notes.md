5 mins, use report (https://github.com/ExtraSlowCode/ClimateStation/blob/main/README.md) as presentation slides.

Well hi there! 
I'm Noa, and for my project I created the ClimateStation
Whilst keeping the device and project simple, I wanted to compare temperature values from different sensors, try out using a photoresistor, and use the humidity data from a DHT11. All this pointed me towards making an indoor climate monitoring device, and that is also the intended use of the ClimateStation.

*show materials table*
To make this project I only needed hardware from the lnu starter kit from electrokit, as per the table. To a Raspberry Pi Pico, I connected a DHT11 humidity and temperature sensor, an MCP9700 temperature sensor, and a photoresistor circuit. I also connected an LED signaling when data is being uploaded to the cloud. 

*show breadboard setup*
As you can see the breadboard became quite messy with all these connections, but is fully functional as-is. But...

*show proposed soldering diagram*
Using the same hardware components with some soldering and more efficient wiring, it could be simplified down to this.

*scroll to Thonny*
I chose to use thonny as my IDE, since I've used it before and wouldn't need any of the fancy expansions VSCode offers. 

*scroll to photoresistor circuit*
Here I put in a 10k resistor as a reference point for comparison with the photoresistor. I chose 10k since it is slightly higher than the maximum load that the photoresistor can reach (7k). By changing the reference resistance, you could of course shift the output curve with the read voltages. The purpose was to make the output more readable than before, since I am only examining the wave formed from the readings, not their actual values.

*show daylight_graph.png*
like this. And yes, the notch in the graph increase shows when I go to bed and turn off my lamps, in reference to the setting sun. The sunrise gives a cleaner curve.

*class diagram*
Code-wise I basically have it all in a single file since it's not too complex on the software side. Except for the network credentials that I decided to have in a separate file for extra protections sake. Feel free to check out the github for the full code.

What the device basically does is:
*show call stack*
Firstly connect to WiFi

then,
Every 15 minutes:
- Read all the sensors (including the on-board temp sensor)
- make a json package with the data
- send it to datacake
- update the dashboard
- sleep until next cycle

All in all, I am quite happy with the results of the project, but would like to work further on it in the near future. I have plans for soldering it together to reduce the mess of wiring, and then 3d-print a case for it. Sadly I didn't have the time for that this time, so I'll pick it up during my free time. 

The dashboard can be seen on datacake. 

*show dashboard*

Feel free to ask any questions to Live me in the call!
