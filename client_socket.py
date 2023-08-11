import socket

# Client will connect to the server IP in practice

HOST = "127.0.0.1"
PORT = 9099

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        command = input()
        s.sendall(b'{command}')
        data = s.recv(1024)
        print(f"Received {data!r}")
