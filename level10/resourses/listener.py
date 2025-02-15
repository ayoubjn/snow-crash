import socket

HOST = '10.11.10.1'
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen(5)

print(f'Socket created and listening on {HOST}:{PORT}')

while 1:
    (conn, addr) = s.accept()
    print('Connected! ' + str(addr))
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    conn.close()
