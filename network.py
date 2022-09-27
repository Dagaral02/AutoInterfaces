#!/usr/bin/env python3
from collections import defaultdict
from os import system
import subprocess

 
    
me = subprocess.getoutput("whoami")
me = me.strip()

if(me == "frodo"):
    print("Hola frodo")
    root = input ("¿Quieres ser root y poder cambiar tu ip? ")
    
    if(root == "si"):
        system("su -")

elif(me == "root"):

    my_gateways =defaultdict(dict)
    my_gateways['192.168.58.1']="192.168.58.155/24"
    my_gateways['192.168.1.1']="192.168.1.10/24"

    def get_gateway():
        gws = netifaces.gateways()
        gws['default']
        return gws['default'][netifaces.AF_INET][0]

    def setIpAddr(iface, staticip,gateway):
        system("ip addr flush ens33")
        system(f"ip addr add {staticip} dev {iface}")
        system(f"ip route add default via {gateway}")

    def getipfromgateway(gateway):
        return my_gateways[gateway]

    gateway = get_gateway()

    if(my_gateways.__contains__(gateway)):
        print("Localizacion reconocida.")
        ip= getipfromgateway(gateway)
        print(f"Asignando IP: {ip}")
        setIpAddr('ens33', ip,gateway)
