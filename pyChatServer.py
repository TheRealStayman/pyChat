import socket

s = socket.socket()
host = socket.gethostname()
port = 21218
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print "Connected to", addr
    c.send("Hello! Welcome to my server.")
    c.close()
