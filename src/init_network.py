import network
import socket

# Set up Wi-Fi connection
wifi_ssid = "dinmamma"
wifi_password = "chromecast"

# Configure Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(wifi_ssid, wifi_password)

# Wait until connected to Wi-Fi
while not wifi.isconnected():
    pass

# Print the IP address once connected
print("Connected to Wi-Fi")
print("IP Address:", wifi.ifconfig()[0])

# Set up socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
