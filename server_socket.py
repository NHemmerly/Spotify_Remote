import socket
import select
# Host and port to use for server-side socket

def main():
    print("main")

if __name__ == "__main__":
    main()

def start():
    HEADER_LEN = 10
    HOST = "192.168.1.131" 
    PORT = 9099

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    server_socket.listen()
    conn, addr = server_socket.accept()

    print(f'Connected by {addr}')
    data = conn.recv(1024)
    command = data.decode("utf-8")
    print(command)
    conn.sendall(data)
    return command
