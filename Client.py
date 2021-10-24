import time, sys, socket, os

s = socket.socket()
host = input('Enter Device Name: ')
port= 8080
s.connect((host, port))
print("")
print('connected..')
print('')

while True:
    rec = s.recv(1024)
    rec = rec.decode()
    print('')
    print('Another: ',rec)
    print('')
    msg = input('You: ')
    msg = msg.encode()
    s.send(msg)



















