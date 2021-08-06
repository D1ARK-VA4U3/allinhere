import os
while True:
	os.system("clear")
	print ("\033[32m")
	
	print("""
#------------------------------------------------#
#     	       A TO Z ALL TOOLS HERE  	  	 #
#             CODED BY : D1ARK-VA4U3             #
#------------------------------------------------#
#  Github  : https://github.com/D1ARK-VA4U3/     #
# Facebook: https://www.facebook.com/Arif.vau143 #
#  Telegram : https://t.me/D1arkva4u3 		 #
#------------------------------------------------#
#               【﻿ Its Me D1ARK-VA4U3】 	 #
#------------------------------------------------#

""")

	print ("\033[31m")
	print("#------------------------------------------------#")
	print("  		Thanks To Using My tools")
	print("#------------------------------------------------#")
	print ("\033[33m")
	print("[1]✓Mail Bomber\n[2]✓SMS Bomber\n[3]✓My Contact Information")
	a=str(input("[>]Select Your Option:"))
	if a=="1":
		os.system("python3 mailbomber.py")
		a=input()
	elif a=="2":
		os.system("python3 sms.py")
		a=input()
	elif a=="3":
		os.system("python3 Contac.py")
		a=input()
	else:
		print("[*] worng value Entered!")
		a=input()