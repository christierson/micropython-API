import requests
import json
from subprocess import check_output
# curl -X POST http://192.168.0.102:8080/ -H "Content-Type: application/json" -d '{"key": "value"}


def send_data(data):
    headers = "Content-Type: application/json"
    url = "http://192.168.0.102:8080/"
    # data ='{"key": "value"}'
    data = json.dumps(data)
    command = ["curl", "-X", "POST", url, "-H", headers, "-d", data]
    print(" ".join(command))
    return check_output(command)


# print(json.dumps(data))
res = send_data(data)
print(res)
