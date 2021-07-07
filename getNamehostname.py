import socket
import threading

#computer's name
print(socket.gethostname())

#computer's IP
SERVER =socket.gethostbyname(socket.gethostname())

# PRINT
print(SERVER)

