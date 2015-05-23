#!D:\python27\python
#-*-coding:utf-8-*-
## this python script is targeting to get the IP from Zoomeye.org
## author:linvex
## other:一边和老婆大人闹别扭一边完成的 :P 我保证以后再也不跟老婆大人闹别扭了

import sys,getopt
import urllib2,re
from time import sleep
import random
import os
import os.path

def usage():
	print '''getIP.py -h(--help)	get the help
	-u(--url)	the search url,default is http://fofa.so/search/result
	-c(--cookie) 	the login cookie, default is linvex
	-p(--page) 	page of result, default is 10
	-k(--keyword) 	keyword of search
	-o(--output)	outputfile, default is output.txt	
	'''
try:
	opts,args = getopt.getopt(sys.argv[1:],'hu:c:p:k:o:',['help','cookie=','page=','keyword=','output='])
except getopt.GetoptError:
	usage()
	sys.exit()
	
#if len(opts) == 0:
#	usage()
#	sys.exit()

url = 'http://fofa.so/search/result'
cookie = '_fofa_session=aWtraCs4RlhEZVN4NDZrTGtXajIyNURCWllGNlNLZTRZd0hIOW9hTFZKVlZlc0t2UlRmSlM5S3h5NGxsY2lmRTd5MDBQNnVsNm4rbGhGOTRYVzNjRklvbGlxNThORjEwTGtIOGhFUC9HZ0xOcllhN24wMzIzNUprN0J5dW54bDYyejVwcjArVTF5eWlsNGVyVXhpVzE0N0dLdktjWVQxQmVwd21iYjVDVHA4WTdpeisxNk5NRW00Z2laN0g4SnFMdHlibTB1Tm1HZWtxMExwSXhqUTdDVFc1MU1GUEVySnZ6Uk14WnRtb25ZU3B2UzUrUzZVY0pMcVp3andlYS8rQmVxcFlwSnpVWnBmclIxYVluakxwemM0aTJhRWVYYStydUIxS20vNmJYTXJpZ0VDaE1TZnQyWGdnV3ErNjUxN05nSWorK3l2Y1Y5dVphTWgrb29KdjFXTFpVNStVbzJycktpYzdqTFp5dGFxbWhRSzF2ZkhoZXZjZ1FBYXZ6VDczLS1ZYUtyTmhlS0p3Q2VCdG1aV3F4cWFRPT0%3D--fc43e42ef62a0435c44089a9f5cef12c75a78f26; _ga=GA1.2.121138911.1428314307; _gat=1;'
page = 11
keyword = 'xmlrpc.php'
input = str(random.randint(1289087,9289078))+'.txt'
output = 'ips_fofa_final_1.txt'

for option, value in opts:
	if option in ('-h','--help'):
		usage()
	elif option in ('-u','--url'):
		url = value.strip("'")
	elif option in ('-c','--cookie'):
		cookie = value
	elif option in ('-p','--page'):
		page = int(value)+1
	elif option in ('-k','--keyword'):
		keyword = value
#	elif option in ('-i','--input'):
#		input = value
	elif option in ('-o','--output'):
		output = value
	
def env():
	if os.path.isfile(input):
		os.remove(input)
	if os.path.isfile(output):
		os.remove(output)

def getip():
	for page_n in range(1,page):
		page_s =  str(page_n)
		print (url+'?page='+page_s+'&q='+keyword)
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie', cookie))
		html = opener.open(url+'?page='+page_s+'&q='+keyword).read()
#		ip_s = re.findall('(?isu)\d+\.\d+\.\d+\.\d+',html)
		ip_s = re.findall('(?isu)\d+\.\d+\.\d+\.\d+',html)
		if ip_s:
			open(input,'a+').write('\r\n'+'\r\n'.join(ip_s))
#		sleep(3)#avoid to forbidden our IP
		
def clearip():
	a = []
	for line in open(input,'r'):
		line_s = line.strip('\r\n')+'\n'
		if line_s not in a:
			a.append(line_s)
#	del a[0]
#	del a[-1]
	open(output,'w+').writelines(a)
	
if __name__ == '__main__':
	env()
	getip()
	clearip()