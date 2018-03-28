# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 15:49:38 2018

@author: rajashekhar

con.txt file contain
raju
ammu
babu
himmu
ramu
"""

f1=open("raju.txt","w+")
f2=open("ramu.txt","w")
f3=open("babu.txt","w")
f4=open("ammu","w")
f5=open("himmu","w")
with open("con.txt") as fo:
    for rec in fo:
                
       
        if(rec.startswith("raju")):
            f1.write(rec)
        elif(rec.startswith("ammu")):
            f4.write(rec)
        elif(rec.startswith("ramu")):
            f2.write(rec)
        elif(rec.startswith("babu")):
            f3.write(rec)
        elif(rec.startswith("himmu")):
            f5.write(rec)
            
            