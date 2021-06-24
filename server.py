import socket

HOST=socket.gethostname()
PORT= 2523

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST,PORT)
    s.listen()
    



