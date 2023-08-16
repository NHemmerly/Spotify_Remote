import socket
import select

def main():
    print("main")

if __name__ == "__main__":
    main()

def start():

    # Host and port to use for server-side socket

    HOST = "" 
    PORT = 9099
    
    # Declares socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Binds object to IP and Port
    server_socket.bind((HOST, PORT))

    # Listens for a connection from client
    server_socket.listen()

    # Saves client info as a conn# and IP address
    conn, addr = server_socket.accept()

    # Connected by device, decodes command, returns command
    print(f'Connected by {addr}')
    data = conn.recv(1024)
    command = data.decode("utf-8")
    print(command)
    conn.sendall(data)
    return command
