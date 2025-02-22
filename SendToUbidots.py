import network
import urequests as request
import dht
from machine import Pin
import utime as time

# 🔹 Setup Wi-Fi According to your SSID and Password
SSID = ""
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    pass

print("Connected to Wi-Fi!")

# 🔹 Setup Sensor DHT11 ON GPIO19
sensor = dht.DHT11(Pin(19))

# 🔹 Ubidots API
UBIDOTS_URL = "http://industrial.api.ubidots.com/api/v1.6/devices/ESP32_Sensor"
UBIDOTS_TOKEN = ""  # Change according to your token

HEADERS = {
    "X-Auth-Token": UBIDOTS_TOKEN,
    "Content-Type": "application/json"
}

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()

        # 🔹 Data Format
        data = {
            "temperature": temp,
            "humidity": hum
        }

        # 🔹 Send Data to Ubidots
        response = request.post(UBIDOTS_URL, json=data, headers=HEADERS)
        print("✅ Data sent to Ubidots:", response.text)
        response.close()
    
    except Exception as e:
        print("❌ Error:", e)

    time.sleep(5)  # Delay 5s every request
