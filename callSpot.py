import usocket as socket
import utime

HOST = ""
PORT = 9099

def callSpot(command):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(command.encode("utf-8"))
    data = s.recv(1024)
    utime.sleep(1)