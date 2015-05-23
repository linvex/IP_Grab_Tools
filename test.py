#!D:\python27\python
##this is test python file


import httplib
import urllib2

url = 'http://www.cnki.net/KCMS/download.aspx?filename=DSqpHUTVXdsd3ZnRnYIF1cMRjR1EUY1ZWYE9UMNpXYFJGWxgmRqRWYz5UOrR2bOhURwIkZ2x0QMpkQ=0TV6J2bkNDMPtScslkWThVN4oVeiF1K0QERygDUJV2cTZmMx1ERyplY5ZnU1lFdyQjcJp1bl5WNuV&dflag=nhdown&tablename=CMFD2009'

req = urllib2.Request(url)

req.add_header('Host', 'cnki.net')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
req.add_header('Referer', url)
req.add_header('Cookie', 'LID=WEEvREcwSlJHSldTTGJhYkg4bE9vMHdLYllXUU5kZWMvZzlCWkliMDV3Wkhib3ZGTitMQlhvMnhrenBWUDBnTytsZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; ASP.NET_SessionId=up1lvjb2iwma0o45ybylw145; SID_kcms=202122; SID=91001; UserSeesKcms=%u7F51%u7EDC%u534F%u8BAE%u7684%u81EA%u52A8%u5316%u6A21%u7CCA%u6D4B%u8BD5%u6F0F%u6D1E%u6316%u6398%u65B9%u6CD5%21cjfq%21cjfd2011%21jsjx201102007%7C; UserDownLoadsKcms=%u7F51%u7EDC%u534F%u8BAE%u7684%u81EA%u52A8%u5316%u6A21%u7CCA%u6D4B%u8BD5%u6F0F%u6D1E%u6316%u6398%u65B9%u6CD5%21cjfq%21cjfd2011%21jsjx201102007%7C; c_m_LinID=LinID=WEEvREcwSlJHSldTTGJhYkg4bE9vMHdLYllXUU5kZWMvZzlCWkliMDV3Wkhib3ZGTitMQlhvMnhrenBWUDBnTytsZz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=04/11/2015 16:37:00')
req.add_header('X-Forwarded-For', '166.111.4.12')
req.add_header('Connection', 'keep-alive')

res = urllib2.urlopen(req)

data = res.read()

with open('test5.caj','wb+') as i:
	i.write(data)


















"""
import cookielib  
import string
import re
import time

header = {
	'Host' : 'cnki.net',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
	'Referer': url,
#	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#	'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#	'Accept-Encoding' : 'gzip, deflate',
#    'Cookie': 'c_m_LinID=LinID=WEEvREcwSlJHSldTTGJhYlRaUVlZZXkxbzBhYk1zeXQxSTNpQm5pNGd0QVN6NmFpTHBUdVc4SUptT1hHZkNCOXJNcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=04/11/2015 15:42:21; LID=WEEvREcwSlJHSldTTGJhYlRaUVlZZXkxbzBhYk1zeXQxSTNpQm5pNGd0QVN6NmFpTHBUdVc4SUptT1hHZkNCOXJNcz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; ASP.NET_SessionId=up1lvjb2iwma0o45ybylw145; SID_kcms=202122; UserSeesKcms=%u7F51%u7EDC%u534F%u8BAE%u7684%u81EA%u52A8%u5316%u6A21%u7CCA%u6D4B%u8BD5%u6F0F%u6D1E%u6316%u6398%u65B9%u6CD5%21cjfq%21cjfd2011%21jsjx201102007%7C',
    'X-Forwarded-For' : '166.111.4.12',
	'Connection' : 'keep-alive'
}
r = urllib2.urlopen(urllib2.Request(url,headers = header))
print r.geturl()
r = urllib2.urlopen(urllib2.Request(r.geturl(),headers = header))
print r.geturl()
#r = urllib2.urlopen(urllib2.Request(r.geturl(),headers = header))
#print r.geturl()
#r = urllib2.urlopen(urllib2.Request(r.geturl(),headers = header))
#print r.geturl()

data = r.read()
with open('test3.pdf','w') as i:
	i.write(data)

"""









"""
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
	elif option in ('-i','--input'):
		input = value
	elif option in ('-o','--output'):
		output = value
"""
"""
if len(getip.opts) == 0:
	getip.usage()
	sys.exit(1)

print "hello!"
getip.clearip()
"""

"""
import sys,os,os.path
import getopt
import urllib2,re
from time import sleep

def usage():
	print '''test.py -h(--help) get the help
	-i(--input) inputfile, default is ips.txt
	-o(--output) outputfile, default is output.txt	
	'''
try:
	opts,args = getopt.getopt(sys.argv[1:],'hi:o:d',['input=','output=','help'])
except getopt.GetoptError:
	usage()
	sys.exit()
	
#if len(opts) == 0:
#	usage()
#	sys.exit()

input = 'ips.txt'
output = 'output.txt'

for option, value in opts:
	if option in ('-h','--help'):
		usage()
	elif option in ('-i','--input'):
		input = value
	elif option in ('-o','--output'):
		output = value
	elif option == '-d':
		print 'usage -d'

#if os.path.isfile(output)
#	os.remove(output)

def clearip():
	a = []
	for line in open(input,'r'):
		line_s = line.strip('\r\n')+'\n'
		if line_s not in a:
			a.append(line_s)
	del a[0]
	del a[-1]
	open(output,'w+').writelines(a)

clearip()
print "done!"
"""