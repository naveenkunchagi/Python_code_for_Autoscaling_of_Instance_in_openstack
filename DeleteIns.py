import keystoneclient.v2_0.client as ksclient 
import glanceclient.v2.client as glclient
import novaclient.v1_1.client as nvclient
import os
import pprint
import time
from credentials import get_nova_creds
def Delete():
	#os.system("nova floating-ip-list")
	creds = get_nova_creds()
	nova = nvclient.Client(**creds)
	#keystone = ksclient.Client(auth_url="http://127.0.0.1:5000/v2.0",username="admin",password="openstack",tenant_name="demo") 
	from credentials import get_keystone_creds
	creds = get_keystone_creds()
	keystone = ksclient.Client(**creds)
	auth_token=keystone.auth_token

	i=1
	for server in nova.servers.list():
		print i ,".", str(server)[9:-1]
		i+=1
	server = raw_input("Enter the instance you wish to delete: ")
	server = nova.servers.list()[int(server)-1]
	server.delete()
	time.sleep(5)

	i=1
	for server in nova.servers.list():
		print i ,".", str(server)[9:-1]
		i+=1
	os.system("nova floating-ip-list")

