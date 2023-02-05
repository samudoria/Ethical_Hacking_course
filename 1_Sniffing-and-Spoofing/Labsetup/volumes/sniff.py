#!/usr/bin/env python3

from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-9ee9c232b895', filter="icmp", prn=print_pkt)
