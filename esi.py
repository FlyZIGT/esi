import nmap
import os
import time
import colorama
from colorama import *
init(autoreset=True)

os.system("clear")
time.sleep(0.7)
os.system('figlet ESI v1')
time.sleep(0.3)
print('\nEasy Scan Ip\n\nDev: py#6650\n\nOpen-Source project\n\n')

ip=input(Fore.BLUE + "Type the target ip\n> ")
esi = nmap.PortScanner()
op=""
results = esi.scan(hosts=ip,arguments="-sT -n -Pn -T4")
count=0
print(Fore.RESET + "\nHost: %s" % ip)
print("State: %s" % esi[ip].state())
for proto in esi[ip].all_protocols():
	print("Protocol: %s" % proto)
	print()
	lport = esi[ip][proto].keys()
	sorted(lport)
	for port in lport:
		print ("port: %s\tstate : %s" % (port, esi[ip][proto][port]["state"]))
		if count==0:
			op=op+str(port)
			count=1
		else:
			op=op+", "+str(port)

print("\nOpen Pourts: "+ op +" "+str(ip))
