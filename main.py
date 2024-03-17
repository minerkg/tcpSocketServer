import socket
import threading

PORT = 5588
IP = "192.168.0.242"


def tcp_server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((IP, PORT))
    serv.listen(10)
    return serv


def send_message(client_socket):
    while True:
        message = input("Your message to client: ")
        client_socket.send(message.encode("utf-8"))


def recv_message(client_socket):
    while True:
        message = client_socket.recv(5000)
        print(f"{message.decode('utf-8')}")


server = tcp_server()
connection, address = server.accept()
thread_recv = threading.Thread(target=recv_message, args=(connection,))
thread_send = threading.Thread(target=send_message, args=(connection,))
thread_recv.start()
thread_send.start()
