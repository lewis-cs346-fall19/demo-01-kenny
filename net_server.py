# Author: Kenny McLaren
# CSC 346, Fall 2019

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 51423)
sock.bind(addr)
sock.listen(5)
while True:
 (connectedSock, clientAddress) = sock.accept()
 try:
  msg = connectedSock.recv(1024).decode()
  print("Received Connection")
 except:
  connectedSock.close()
 first = msg[0]
 end = msg[1:]
 sending = "Starts with: " + first + " Ends with: " + end
 print("Sending Message: " + sending)
 connectedSock.sendall(sending.encode())
