import keystoneclient.v2_0.client as ksclient 
import glanceclient.v2.client as glclient
import novaclient.v1_1.client as nvclient
import time
import os
import subprocess
import random
from credentials import get_nova_creds

def Create():
	creds = get_nova_creds()
	nova = nvclient.Client(**creds)
	from credentials import get_keystone_creds
	creds = get_keystone_creds()
	keystone = ksclient.Client(**creds)
	auth_token=keystone.auth_token
	i=1
	nlist=[]
	for image in nova.images.list():
		#print i ,".", str(image)[8:-1]
		nlist.append(str(image)[8:-1])
		
		i+=1
	#print nlist
	#image = raw_input("Enter the desired Image you want to use: ")
	#image = nova.images.list()[int(image)-1]
	print "Creating an Instance"
	image = nova.images.list()[0]
	print "Done"
	i=1
	for flavor in nova.flavors.list():
		#print i,".", str(flavor)[8:-1]
		i+=1
	#flavor = raw_input("Enter the Flavor you wish to use: ")
	#flavor = nova.flavors.list()[int(flavor)-1]
	print"Assigining Flavour"
	flavor = nova.flavors.list()[2]
	print "Done"
	i=1
	for keypair in nova.keypairs.list():
		#print i,".",str(keypair)[9:-1]
		i+=1
	#keypair = raw_input("Enter the Keypair you wish to use: ")
	#keypair = str(str(nova.keypairs.list()[int(keypair)-1]))[10:-1]
	print "Assigining Keypair"
	keypair = str(str(nova.keypairs.list()[0]))[10:-1]
	print "Done"
	#print random.randint(0,100)
	#print random.random()*100
	#insname=raw_input("Enter the name of the Instance: ")
	print "Assigining a name to the Instance: "
	insname="Instance" + str(random.randint(0,100))
	print "Creating instance:",insname
	print "Image:",str(image)[8:-1]
	print "Flavor:",str(flavor)[8:-1]
	print "Keypair:",keypair
	instance = nova.servers.create(name=insname, image=image, flavor=flavor, key_name=keypair)
	print "Status:",instance.status 
        print "Creating Floating Ip"
	os.system("nova floating-ip-create > abc.txt")
        os.system("grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' abc.txt > ip.txt")
	xyz=open('ip.txt','r+')
	ip=xyz.read()
	print "Floating Ip is:",ip
        print "Assigining Floating Ip"
	time.sleep(10)
	x="nova floating-ip-associate "+str(insname)+" "+str(ip)
	os.system(x)
        xyz.close()
	print "Instance is Running"
