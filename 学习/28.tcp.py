#!/bin/py
#   -*-coding:utf-8-*-
import socket,threading,time

n=2
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8800))
s.listen(n)
print("waiting for connection..")

def tcplink(sock, addr):
    global n
    n=n-1
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!\r\n')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!\r\n' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    n=n+1



while True:
    time.sleep(1)
    if n>0:
        sock,addr=s.accept()
        t=threading.Thread(target=tcplink,args=(sock,addr))
        t.start()

    else:
        print("已到连接上限，请稍后再试")
