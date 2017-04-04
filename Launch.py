import os
from DeleteIns import Delete
from CreateInstance import Create

#os.system('source openrc')
if __name__ == '__main__':
	print "1.Create instances"
	print "2.Delete an instance"
	ch=raw_input("Enter your choice: ")
	if ch=='1':
		Create()
	elif ch=='2':
		Delete()
