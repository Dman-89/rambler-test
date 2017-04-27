# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 08:13:27 2017

@author: fialdm01
"""
from time import sleep
from itertools import islice

#creating file
with open('.\example.txt', 'w+') as txt:
    for i in range(3):
        txt.write('initial row '+ str(i) + '\n')

#opening file and printing ini rows
txt=open('.\example.txt', 'r')
file=txt.readlines()
for p in file: print (p)
ini_len=len(file)

#printing newly added rows
while 1:
    txt=open('.\example.txt', 'r')
    for line in islice(txt, ini_len, None):
        if line:
            print(line)
            ini_len+=1
    #just not to check file each&every moment
    sleep(5)  
