# Author: Kenny McLaren
# CSC 346, Fall 2019

import socket

while True:
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 addr = ("localhost", 51423)
 sock.connect(addr)
 print("Please enter one word:")
 userInp = raw_input()
 print("Sending: " + userInp)
 sock.sendall(userInp.encode())
 recept = sock.recv(1024).decode()
 print("Received: " + recept)
 sock.close()

