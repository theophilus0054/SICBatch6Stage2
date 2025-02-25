import network
import urequests as request
import dht
from machine import Pin, ADC
import utime as time

# Connect to Wi-Fi
# Set According to your Wi-Fi
ssid = "WISMA BERIMAN 3" 
password = "ALVIN0713"

# Set According to your Ubidots Token and label
ubidots_token = "BBUS-NfprmsxyEjByJaZEOJg9AfekxAkQmX"
device_label = "esp-32"

# Set According to your Flask Server
url_flask = "http://192.168.1.74:7000/data"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected to Wi-Fi!")

url_ubidots = "http://industrial.api.ubidots.com/api/v1.6/devices/" + device_label
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": ubidots_token
}

# Initiate DHT11 sensor on GPIO19
sensor = dht.DHT11(Pin(19))

# Initiate PIR sensor on GPIO5
pir_sensor = Pin(5, Pin.IN)

# Initiate LDR sensor on GPIO34
ldr_sensor = ADC(Pin(34))
ldr_sensor.atten(ADC.ATTN_11DB)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        motion = 1 if pir_sensor.value() == 1 else 0
        light = ldr_sensor.read()
        
        data = {
            "temperature": temp,
            "humidity": hum,
            "motion": motion,
            "light": light,
        }

        # Send data to Flask server
        # Set According to your Flask Server Url
        response = request.post(url_flask, json=data)
        print(response.text)
        response.close()
        
        # Send data to Ubidots
        response2 = request.post(url_ubidots, json=data, headers=headers)
        print(response2.text)
        response2.close()
        
    except Exception as e:
        print("Error:", e)
    
    time.sleep(8)
