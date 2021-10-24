import time, sys, socket

s = socket.socket()
host = socket.gethostname()
print(host)
port= 8080
s.bind((host, port))
print("")
print('Waiting...')
print('')
s.listen(1)
conn, addr = s.accept()
print('')
print('Connected to ', addr)
print('')

while True:
    msg = input('You: ')
    msg = msg.encode()
    conn.send(msg)
    rec = conn.recv(1024)
    rec = rec.decode()
    print('')
    print('Another: ', rec)
    print('')

























