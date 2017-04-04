import os
import string
import re
#Calculating Cpu Load using up command
#def Calculaotr():
os.system("uptime > a.txt")
os.system("uptime")
a=open('a.txt','r')
alist=[]
alist=re.findall(r"([0-9]\.\d+)", a.read())
a.close()
alist=map(float,alist)
print "Load Recorded at 1st Min, 5th Min, 15th Min: ",alist
total=(alist[0]+alist[1]+alist[2])/3
val=str(total)
print "Average load on CPU is: " +val+ " %"
print "done"

