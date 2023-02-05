#!/usr/bin/env python3

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-9ee9c232b895', filter='host 10.9.0.5 and tcp port 23', prn=print_pkt)
