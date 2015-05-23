#!D:\python27\python
## this is a test python script

import sys, getopt, re
import getip
import random

line = []
result = []
file = open('ips.txt','r')
line = file.readlines()
#print line
for i in line:
    t = re.findall('\d{0,3}\.\d+\.\d+\.\d+',i)
    result.append(t)
open('ts.txt','w+').write(result)













"""
print str(random.randint(1289087,9289078))+'.txt'
"""
"""
if len(getip.opts) == 1:
        getip.usage()
        sys.exit()

getip.output = raw_input("outputfile:")
getip.env()
getip.clearip()



while 1:
    re = raw_input("plz input your string:")

    if re == 'stop':
        break
    print re.upper()

"""
