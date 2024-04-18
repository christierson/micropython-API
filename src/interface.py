import json
from src.init_network import SOCKET, HTTP_200
from src.init_dht import sensor_read

def run():
    SOCKET.listen(1)
    # Listen for connections, serve client
    while True:
        try:
            cl, addr = SOCKET.accept()
            print("client connected from", addr)
            request = cl.recv(102400)
            print("request:")
            print(request.decode())

            temp, hum = sensor_read()

            context = {"temperature": temp, "humidity": hum}

            cl.send(HTTP_200)
            cl.send(json.dumps(context))
            cl.close()

        except OSError as e:
            cl.close()
            print("connection closed")
