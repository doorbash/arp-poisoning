# arp-poisoning
A simple Arp sniffing tool that uses Scapy to generate network packets

## Requirements:
   - [Pyhton](https://www.python.org/)
   - [Scappy](http://www.secdev.org/projects/scapy/)
   - [Wireshark](https://www.wireshark.org/)

## How to use:
   - Open Terminal with administrator privileges (Linux users type <b>sudo su</b> in terminal).
   - Make sure python is installed by typing <b>python --version</b>
   - Enable IP Forwarding in your Operating system.Linux users can type <b>echo 1 > /proc/sys/net/ipv4/ip_forward</b>
   - Download and setup Scapy python library from <a href="http://www.secdev.org/projects/scapy/">http://www.secdev.org/projects/scapy/</a>
   - Run program like this : python attack.py -v victimIP -r routerIP <b>Example: python attack.py -v 192.168.1.12 -r 192.168.1.1</b>
   - Run Wireshark then capture packets with this filter : <b>ip.addr eq victimIP and ip.addr eq routerIP</b>

<b>Please feel free to contribute!</b>
