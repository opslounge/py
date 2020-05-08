#
#    this for loop can be used for many things, here its used for ping
#
#    by andy parsons 8,5,2020   opslounge2019@gmail.com


import os



#this file contains a list of pwwns
pw=open("ping","r")


for line in pw:
        sc = line.strip()
	cmd = "ping -c 4 {0}" .format(sc)
        os.system(cmd)
