import socket
import threading



#PORT
PORT =5050
#HOST
SERVER =socket.gethostbyname(socket.gethostname())

ADDR=(SERVER,PORT)

#bytes
HEADER =64
#format
FORMAT ='utf-8'
#disconect mess
DISCONNECT_MESSAGE

# Create  the socket to the port
#                     family         type of scoket
_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

_server.bind(ADDR)

# all comunication betwenn server and client
def handle_client(conn,addr):

    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True 
    while connected:
        #how many bytes are want to recive
        msg_lengh=conn.recv(HEADER).decode(FORMAT)
        msg_lengh=int(msg_lengh)
        msg= conn.recv(msg_lengh).decode(FORMAT)
        print(f"[{addr}] {msg}")


        

def start():
    # listen for a incoming connections
    _server.listen()
    while True:
                 
        conn,addr =_server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        #how many proccess
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
        print("[starting] server is starting..")
start()

print(SERVER)