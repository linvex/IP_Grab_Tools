#!D:\python27\python
#-*-coding:utf-8-*-
## this python script is targeting to get the IP from Zoomeye.org
## author:linvex
## other:一边和老婆大人闹别扭一边完成的 :P 我保证以后再也不跟老婆大人闹别扭了

import urllib2,re
from time import sleep
import os
import os.path

if os.path.isfile('ips.txt'):
	os.remove('ips.txt')
if os.path.isfile('ips_final.txt'):
	os.remove('ips_final.txt')

def getip(r_a,r_b):
	for page in range(r_a,r_b):
		page_s =  str(page)
		print ('http://www.zoomeye.org/search?q=xmlrpc.php&p='+page_s+'&t=host')
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie', 'Hm_lvt_e58da53564b1ec3fb2539178e6db042e=1428309908; Hm_lpvt_e58da53564b1ec3fb2539178e6db042e=1428309936; csrftoken=pWFviP4Gacqe3jDCBXyovrLUN43RjtWl; sessionid=l9vwr9itbdt9ethpyr1pt7zw7zzkhwit'))
		html = opener.open('http://www.zoomeye.org/search?q=xmlrpc.php&p='+page_s+'&t=host').read()
		ip_s = re.findall('(?isu)\d+\.\d+\.\d+\.\d+',html)
		if ip_s:
			open('ips.txt','a+').write('\r\n'+'\r\n'.join(ip_s))
		sleep(5)#avoid to forbidden our IP
		
def clearip():
	a = []
	for line in open('ips.txt','r'):
		line_s = line.strip('\r\n')+'\n'
		if line_s not in a:
			a.append(line_s)
	del a[0]
	del a[-1]
	open('ips_final.txt','w+').writelines(a)

getip(1,30)
clearip()
print ('Just have a rest;)')
sleep(60)
t = urllib2.urlopen('http://www.zoomeye.org/').read()

getip(31,60)
clearip()
print ('Just have a rest;)')
sleep(60)
t = urllib2.urlopen('http://www.zoomeye.org/').read()

getip(61,90)
clearip()
print ('Just have a rest;)')
sleep(60)
t = urllib2.urlopen('http://www.zoomeye.org/').read()

getip(91,101)
clearip()