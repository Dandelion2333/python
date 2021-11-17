#!/usr/bin/env python2.7
#-*- coding: UTF-8 -*-

# 功能：多个客户端通过服务器获取编号，要求编号不重复且连续

import socket
import threading

number = 19010000

def new_number():
    global number
    number = number + 1

def tcplink(conn, addr):
    print("Accept new connection from %s:%s" % addr)
    conn.send(b"Welcome!\n")
    while True:
        data = conn.recv(1024).decode()
        if data == "exit":
            conn.send(b"recv_exit")
            break
        else:    
            new_number()    
            data1 = str(number)    
            conn.send(b"number is:%s\n" % data1.encode())
    conn.close()
    print("Connection from %s:%s is closed" % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 6000))
s.listen(5)
print("Waiting for connection...")

while True:
    conn, addr = s.accept()
    t = threading.Thread(target = tcplink, args = (conn, addr))
    t.start()        