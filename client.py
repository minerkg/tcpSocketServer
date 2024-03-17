import socket
import time

PORT = 5588
IP = "192.168.0.242"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

message = "Client connected.. "
client_socket.send(message.encode("utf-8"))

while True:
    time.sleep(5)
    resp = client_socket.recv(5000)
    print(resp.decode("utf-8"))
