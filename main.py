# from src.interface import run

# run()


import network
import socket
import ujson
from src.init_dht import sensor_read

HTTP_200 = b'HTTP/1.0 200 OK\r\nContent-Type: application/json\r\n\r\n'
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
server_socket.listen(1)

print("Waiting for connection...")

# Accept incoming connection
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

while True:
    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        
        # Check if data is received
        if data:
            # Decode received data as JSON
            try:
                control_data = ujson.loads(data)
                print("Received:", control_data)
                
                temp, hum = sensor_read()
                
                # Send response back to client
                response_data = {
                    "temperature": temp,
                    "humidity": hum,
                }
                print("Sensor Reading:",  response_data)
                response_json = ujson.dumps(response_data)
                client_socket.send(response_json.encode())
                
            except Exception as e:
                print("Error:", e)
        
    except KeyboardInterrupt:
        break

# Close sockets
client_socket.close()
server_socket.close()