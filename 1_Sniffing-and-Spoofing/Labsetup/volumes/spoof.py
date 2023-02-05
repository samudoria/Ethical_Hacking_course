#!/usr/bin/env python3

from scapy.all import *

ip = IP()
ip.dst = "10.9.0.5"
ip.src = "1.2.3.4"
icmp = ip/ICMP()
received = send(icmp)
print(received is None)
