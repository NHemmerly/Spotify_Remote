import socket
import select
# Host and port to use for server-side socket

HEADER_LEN = 10
HOST = "127.0.0.1" 
PORT = 9099

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()
conn, addr = server_socket.accept()

print(f'Connected by {addr}')
data = conn.recv(1024)
print(data.decode("utf-8"))
conn.sendall(data)


