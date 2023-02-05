#!/usr/bin/python3

from scapy.all import *
import sys

a = IP()
if len(sys.argv) < 2:
    print("Usage: "+sys.argv[0] + " hostname")
    exit(1)
else:
   a.dst = socket.gethostbyname(sys.argv[1]) 
print("destination: "+ str(a.dst))
a.ttl = 1
b = ICMP()
MAX_TTL = 256

found = False
while a.ttl < MAX_TTL:
    received = sr1(a/b, verbose = 0, timeout = 2)
    if received is None:
        a.ttl += 1
        continue
    print("arrived at " + str(received.src) + " with " + str(a.ttl) + " hops")
    if received.src == a.dst:
        found = True
        break
    a.ttl += 1
if not found:
    print("not found")
else:
    print("arrived with "+ str(a.ttl) + " hops")
