#!/usr/bin/python
#
#This is a volume restore script. The purpose of this script is to restore the :
 
 
 
import subprocess
import re
from sys import argv
 
 
print "This command will restore all of the boot volumes in the (bfs) file"
 
 
before = open('bf','r')
after = open('af','r')
 
for line in before and after:
	command = "ssh pureuser@cloud-demo-bfs-fa320-1 purevol {0}{1} " .format(before,after)
	subprocess.call(command.split())
