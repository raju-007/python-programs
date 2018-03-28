"""
in remote system we have to type

sudo netcat -l 999
and password of that system
output:
hi bangalore message is printed in remote system  

"""




#!user/bin/python
import telnetlib
host="192.168.1.152"
tn=telnetlib.Telnet(host,"999")
tn.write("hi bangalore\n")
print tn.read_all()

