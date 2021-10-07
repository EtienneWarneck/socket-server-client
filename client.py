import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.4", 1234))

full_msg = ''
# while True:
msg = s.recv(1024)
# if len(msg) <= 0:
#     break
full_msg += msg.decode("utf-8")

print(full_msg)
