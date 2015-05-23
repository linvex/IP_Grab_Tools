#!D:\python27\python
#-*-coding:utf-8-*-
## this python script is targeting to get the IP from Zoomeye.org
## author:linvex
## other:一边和老婆大人闹别扭一边完成的 :P 我保证以后再也不跟老婆大人闹别扭了

import urllib2,re
from time import sleep
import os
import os.path

if os.path.isfile('ips_fofa.txt'):
	os.remove('ips_fofa.txt')
if os.path.isfile('ips_fofa_final.txt'):
	os.remove('ips_fofa_final.txt')

def getip(r_a,r_b):
	for page in range(r_a,r_b):
		page_s =  str(page)
		print ('this is page'+page_s+':P')
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie', '_fofa_session=aWtraCs4RlhEZVN4NDZrTGtXajIyNURCWllGNlNLZTRZd0hIOW9hTFZKVlZlc0t2UlRmSlM5S3h5NGxsY2lmRTd5MDBQNnVsNm4rbGhGOTRYVzNjRklvbGlxNThORjEwTGtIOGhFUC9HZ0xOcllhN24wMzIzNUprN0J5dW54bDYyejVwcjArVTF5eWlsNGVyVXhpVzE0N0dLdktjWVQxQmVwd21iYjVDVHA4WTdpeisxNk5NRW00Z2laN0g4SnFMdHlibTB1Tm1HZWtxMExwSXhqUTdDVFc1MU1GUEVySnZ6Uk14WnRtb25ZU3B2UzUrUzZVY0pMcVp3andlYS8rQmVxcFlwSnpVWnBmclIxYVluakxwemM0aTJhRWVYYStydUIxS20vNmJYTXJpZ0VDaE1TZnQyWGdnV3ErNjUxN05nSWorK3l2Y1Y5dVphTWgrb29KdjFXTFpVNStVbzJycktpYzdqTFp5dGFxbWhRSzF2ZkhoZXZjZ1FBYXZ6VDczLS1ZYUtyTmhlS0p3Q2VCdG1aV3F4cWFRPT0%3D--fc43e42ef62a0435c44089a9f5cef12c75a78f26; _ga=GA1.2.121138911.1428314307; _gat=1;'))
		html = opener.open('http://fofa.so/search/result?page='+page_s+'&q=xmlrpc.php&qbase64=eG1scnBjLnBocA%3D%3D').read()
		ip_s = re.findall('(?isu)\d+\.\d+\.\d+\.\d+',html)
		if ip_s:
			open('ips_fofa.txt','a+').write('\r\n'+'\r\n'.join(ip_s))
#		sleep(3)#avoid to forbidden our IP
		
def clearip():
	a = []
	for line in open('ips_fofa.txt','r'):
		line_s = line.strip('\r\n')+'\n'
		if line_s not in a:
			a.append(line_s)
	del a[0]
	del a[-1]
	open('ips_fofa_final.txt','w+').writelines(a)

getip(1,101)
clearip()