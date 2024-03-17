import socket
import time
import threading


PORT = 5588
IP = "192.168.0.242"

def send_message(server_socket:socket.socket):
    while True:
        message = input("Your message to server: ")
        server_socket.send(message.encode('utf-8'))


def recv_message(server_socket:socket.socket):
    while True:
        time.sleep(2)
        message = server_socket.recv(5000).decode('utf-8')
        print(message)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

message = "Client connected.. "
client_socket.send(message.encode("utf-8"))

send_thread = threading.Thread(target=send_message, args=(client_socket,)).start()
recv_thread = threading.Thread(target=recv_message, args=(client_socket,)).start()