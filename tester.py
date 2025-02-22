import network
import urequests as request
import dht
from machine import Pin, ADC
import utime as time

# Connect to Wi-Fi
ssid = ""
password = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected to Wi-Fi!")

# Initiate DHT11 sensor on GPIO19
sensor = dht.DHT11(Pin(19))

# Initiate Light Sensor (LDR) on GPIO34 (ADC1)
# light_sensor = ADC(Pin(34))
# light_sensor.atten(ADC.ATTN_11DB)  # Set ADC range to 0-3.3V (ESP32)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Read light intensity (0-4095 for ESP32)
        # light_value = light_sensor.read()
        
        # Convert ADC value to percentage (0-100%)
        # light_percentage = (light_value / 4095) * 100
        
        data = {
            "temperature": temp,
            "humidity": hum,
            # "light_intensity": light_percentage
        }

        # Send data to Flask server
        response = request.post("http://192.168.1.100:7000/data", json=data)
        print(response.text)
        response.close()
    except Exception as e:
        print("Error:", e)
    
    time.sleep(7)
