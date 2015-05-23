#!D:\python27\python
#-*-coding:utf-8-*-
## this python script is targeting to get the IP from Zoomeye.org
## author:linvex
## other:一边和老婆大人闹别扭一边完成的 :P 我保证以后再也不跟老婆大人闹别扭了

import sys,getopt
import urllib2,re
from time import sleep
import os
import os.path

def usage():
	print '''getIP.py -h(--help)	get the help
	-u(--url)	the search url,default is http://fofa.so/search/result
	-c(--cookie) 	the login cookie, default is linvex
	-p(--page) 	page of result, default is 10
	-k(--keyword) 	keyword of search
	-i(--input)	inputfile, default is ips.txt
	-o(--output)	outputfile, default is output.txt	
	'''
try:
	opts,args = getopt.getopt(sys.argv[1:],'hu:c:p:k:i:o:',['help','cookie=','page=','keyword=','input=','output='])
except getopt.GetoptError:
	usage()
	sys.exit()
	
#if len(opts) == 0:
#	usage()
#	sys.exit()

url = 'http://fofa.so/search/result'
cookie = '_fofa_session=THR5VGhLb0tIeVNDVkNORS9Yb0g0dEYzY1RDNXVxWkNLaTdvT0g5YTdCSlR4bG14d2ZYaEc1TCtuQmJSL0VxWEJid0d4c3JpVkNNVmFTdnhxbVNMWnVLandDYTZGM3p5UUUrTFhVcVRjU3haNEoydVlaeUNZa1FwcVplU2UxMjJGUndzRUxSMGpMblpTY0wxby9aQ0d4UGgwZmp2MkZUdGtzWDltQ3hhR0VSS2N2VWR5eHd5aXRZL3hxU2lZSm1xSlkxUHMzOWZja0Nqbk0rZGhvdGRwZzhCL2pCbXQ1TXIyN05yK3lCMEZRaHhnWThRTUpmUjhBcjNYQ3pHQWdNc0JhUWw2bHhzQm1XajVjWU45T29KMnZmc1A0SXM2aDRmaWRBSjRmdXNmSEpRQll6bFpKeFFaMmtibjFPODl3alNzalZwb2ZDNG5vU0JacE04WjlqU2o0QTNBTUdIVGFmRXZmSUNjQk1ibmdxVjVPUVVSVUFkQlBxYWN1dGtIS08yakR1Yk1aNnVnZEFyeG5vaS80b0FSclVnRGcrc0ZkSXBWQWw5YkxpT1ZDZz0tLU45cG1XZmRWNnd0bGFXTW92bFdTekE9PQ%3D%3D--40a27f859668ee5b2124aa98e78e59f0b898cea8; _ga=GA1.2.1593831474.1428395883; _gat=1; remember_user_token=BAhbB1sGaQJgBUkiIiQyYSQxMCRYaFlGbllTZzVSR3dWUFR6MzBkZzQuBjoGRVQ%3D--fab55d2a2d19dc515d64f7b1e9906fd2127f5558; request_method=GE'
page = 11
keyword = 'xmlrpc.php'
input = 'ips_fofa_1.txt'
output = 'ips_fofa_final_1.txt'

for option, value in opts:
	if option in ('-h','--help'):
		usage()
	elif option in ('-u','--url'):
		url = value.strip("'")
	elif option in ('-c','--cookie'):
		cookie = value.strip("'")
	elif option in ('-p','--page'):
		page = int(value)+1
	elif option in ('-k','--keyword'):
		keyword = value
	elif option in ('-i','--input'):
		input = value
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
		ip_s = re.findall('\d+\.\d+\.\d+\.\d+',html)
		if ip_s:
			open(input,'a+').write('\r\n'+'\r\n'.join(ip_s))
#		sleep(3)#avoid to forbidden our IP
		
def clearip():
	a = []
	for line in open(input,'r'):
		line_s = line.strip('\r\n')+'\n'
		if line_s not in a:
			a.append(line_s)
	del a[0]
#	del a[-1]
	open(output,'w+').writelines(a)
	
if __name__ == '__main__':
	env()
	getip()
	clearip()