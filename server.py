import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.4", 1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    client_socket.send(bytes("Welcome, message from server", "utf-8"))
    client_socket.close()
