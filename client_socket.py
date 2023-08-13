import socket
import sys

# Client will connect to the server IP in practice

HOST = "127.0.0.1"
PORT = 9099

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    command = sys.argv[1]
    s.sendall(f'{command}'.encode("utf-8"))
    data = s.recv(1024)
    print(f"Received {data!r}")
