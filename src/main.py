from machine import Pin, ADC
from time import sleep
from requests import post, Response
import dht
import network
import keys


# Pin definitions
    # Might change based on hardware setup
DHT_PIN = 0
MCP_PIN = 26 # requires an ADC pin
SEND_LED_PIN = 15
PHOTO_RES_PIN = 27 # requires an ADC pin


# Globals
dht11_temp = 0
dht11_humidity = 0
mcp_temp = 0
board_temp = 0
light_level = 0


# Pin configurations
    # LED (green)
send_led = Pin(SEND_LED_PIN, Pin.OUT)

# On-Board LED
    # https://forums.raspberrypi.com/viewtopic.php?t=336836
board_led = machine.Pin("LED", machine.Pin.OUT) 

# DHT-11 sensor
    # Temperature Celsius, Humidity %
dht_sensor = dht.DHT11(Pin(DHT_PIN))

# MCP9700 TO-92 sensor
    # Temperature analog
    # https://micropython.org/resources/docs/en/latest/library/machine.ADC.html
mcp_pin = machine.Pin(MCP_PIN)
mcp_sensor = ADC(mcp_pin)

# On-Boad Temperature sensor
    # (ADC4-diode), https://randomnerdtutorials.com/raspberry-pi-pico-internal-temperature-micropython/
board_temp_sensor = ADC(4)

# Photo Resistor PGM CdS-5mm sensor
    # Sunlight level analog
photo_res_pin = machine.Pin(PHOTO_RES_PIN)
photo_res = ADC(photo_res_pin)


# Switches pin status
    # made to change LED state
def lit(pin, status):
    pin.on() if status else pin.off()
    return not status
    
# Sends HTTP POST-request to datacake with data variables with updated values
    # requires http_post()
    # Blinks send_led while sending the request. Try to catch it if you're bored
    # slight modification of code from:
    # https://hackmd.io/@lnu-iot/HyU0e37Pn
def upload_data():
    global send_led
    data: dict[str, str|float] = {
        "device": "80ab0e6e-d021-46c8-affd-dfedd202365d",
        "Temperature_dht": dht11_temp,
        "Temperature_mcp": mcp_temp,
        "Temperature_board": board_temp,
        "Humidity": dht11_humidity,
        "Light_level": light_level
    }
    
    # uploading...
    lit(send_led, True)

    url: str = "https://api.datacake.co/integrations/api/5052959c-4f41-4e87-8f26-f3d39552c7bc/"

    http_post(url = "https://api.datacake.co/integrations/api/5052959c-4f41-4e87-8f26-f3d39552c7bc/",data = data)
    
    lit(send_led, False)

# Reads the DHT pin, and updates it's values
def dht_read():
    global dht11_temp, dht11_humidity, dht_sensor
    try:
        dht_sensor.measure()
        dht11_temp = dht_sensor.temperature()
        dht11_humidity = dht_sensor.humidity()
        
    except Exception as e:
        print("DHT11-read error: ", e)
        
# Reads the MCP pin, and updates it's values
    # https://micropython.org/resources/docs/en/latest/library/machine.ADC.html
    # https://hackmd.io/@V49fajJkS2upkw6dLgDslA/BkL-a4QJD
def mcp_read():
    global mcp_temp, mcp_sensor
    try:
        u16_in = mcp_sensor.read_u16()
        voltage = (u16_in/65535)*3.3*1000
        mcp_temp = (voltage - 500.0) / 10.0 # Converts millivolts to degrees celsius
        
    except Exception as e:
        print("MCP9700-read error: ", e)

# Reads the on-board temp sensor, and updates it's values
    # Rui Santos & Sara Santos - Random Nerd Tutorials
    # Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-internal-temperature-micropython/
def board_temp_read():
    global board_temp, board_temp_sensor
    try:
        u16_in = board_temp_sensor.read_u16()
        voltage = u16_in * (3.3/65535.0)
        board_temp = 27 - (voltage - 0.706) / 0.001721
    except Exception as e:
        print("On-Board Temperature-read error: ", e)

# Printout current values for all sensors
    # Only really used while writing this program.
def debug_print():
    print(f"\n\n"
        f"====================\n"
        f"CURRENT MEASUREMENTS\n"
        f"====================\n"
        f"DHT-11 Reading:\n"
        f"\tTemperature: {dht11_temp} degrees Celsius\n"
        f"\tHumidity: {dht11_humidity} %\n"
        f"MCP9700 Reading:\n"
        f"\tTemperature: {mcp_temp:.2f} degrees Celsius\n"
        f"Photo Resistor Reading:\n"
        f"\tVoltage difference: {light_level} volts\n"
        f"\tRelative brightness factor: {light_level} %\n"
        f"On-Board Temperature Reading:\n"
        f"\tTemperature: {board_temp:.2f} degrees Celsius\n"
        )

# Reads the photoresistor pin, and updates it's values
def light_level_read():
    global photo_res, light_level
    try:
        u16_in = photo_res.read_u16()
        voltage = ((u16_in)/65535)*3.3
        
        light_level = 3.3 - voltage
    except Exception as e:
        print("Photo Resistor-read error: ", e)
        
# Establishes a WiFi connection
    # requires network SSID and PSWD in the file keys.py
    # Method taken from a previous assignment of mine.
    # Remember to check the keys.py file.
def connect_wifi():
    wlan = network.WLAN(network.STA_IF) # (connect mode)
    wlan.active(True)
    wlan.connect(keys.SSID, keys.PSWD)
    while wlan.isconnected() is False:
        print("Connecting to wifi...")
        sleep(1)
    print("- Connected to:", keys.SSID)
    return wlan.ifconfig()[0] # device's own ip

# Taken from below, seems to for some reason be required for the wifi to properly connect
    # https://hackmd.io/@lnu-iot/rJVQizwUh
def http_get(url = 'http://detectportal.firefox.com/'):
    import socket                           # Used by HTML get request
    import time                             # Used for delay
    _, _, host, path = url.split('/', 3)    # Separate URL request
    addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
    s = socket.socket()                     # Initialise the socket
    s.connect(addr)                         # Try connecting to host address
    # Send HTTP request to the host with specific path
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))    
    time.sleep(1)                           # Sleep for a second
    rec_bytes = s.recv(10000)               # Receve response
    print(rec_bytes)                        # Print the response
    s.close()                               # Close connection

# Taken from below, required for upload_data()
    # https://hackmd.io/@lnu-iot/HyU0e37Pn
def http_post(url: str, data: dict[str, str|int]) -> None:
    response: Response = None
    try:
        response = post(url, json = data)
        print(response.content)
        
    except Exception as e:
        print(e)

# Startup
def startup():
    # led state reset
    lit(send_led, False)
    lit(board_led, False)
    
    # start signal, used for visual debugging on-device
    print("Starting...")
    for i in range(6):
        lit(send_led, i % 2 == 0)
        sleep(0.5)
    
    # establish connection
    connect_wifi()
    
    # keep on-board LED as sign that connection to wifi is up
    lit(board_led, True)

# main
startup()
http_get() # for some reason required for the wifi to connect?
while(True):
    dht_read()
    mcp_read()
    board_temp_read()
    light_level_read()
    upload_data() # send to datacake
    debug_print() # optional
    sleep(3)
    # comment out below line if debugging, and upload_data() is paused. meant to not overload datacake.
    sleep(897) # update freq in s (currently at 30min cooldown)
