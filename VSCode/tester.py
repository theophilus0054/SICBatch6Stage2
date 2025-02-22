import network
import urequests as request
import dht
from machine import Pin
import utime as time

# Koneksi ke Wi-Fi
ssid = "WISMA BERIMAN 3"
password = "ALVIN0713"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected to WiFi!")

# Inisialisasi sensor DHT11 di GPIO4
sensor = dht.DHT11(Pin(19))
pir = Pin(14, Pin.IN)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        if (pir.value() == 1):
            motion = "Motion Detected!"
        else:
            motion = "No Motion"
        data = {"temperature": temp, "humidity": hum, "Motion": motion}

        # Kirim data ke server Flask
        response = request.post("http://192.168.1.52:7000/data", json=data)
        print(response.text)
        response.close()
    except Exception as e:
        print("Error:", e)
    time.sleep(7)

