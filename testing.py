
import socket
import json

server_ip = "192.168.1.100"  # Replace with the IP address of your Pico
server_port = 8080

# Control data to be sent to the server
control_data = {"lamp": 1, "fan": 0}

try:
    # Connect to the server
    print("Connecting to socket")
    client_socket = socket.socket()
    client_socket.connect(socket.getaddrinfo(server_ip, server_port)[0][-1])
    print("Socket connected, sending data:", control_data)
    # Send control data to the server
    client_socket.send(json.dumps(control_data).encode())
    print("Waiting for response")
    # Receive response from the server
    response_data = client_socket.recv(1024)
    response_json = response_data.decode()
    response = json.loads(response_json)

    # Print response from the server
    print("Received response:")
    print("Lamp state:", response.get("lamp"))
    print("Fan state:", response.get("fan"))
    print("Sensor reading:", response.get("sensor_reading"))

except Exception as e:
    print("Error:", e)

finally:
    # Close the socket
    client_socket.close()