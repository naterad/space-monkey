# https://pypi.python.org/pypi/yahoo-finance/1.1.4

import httplib
import urllib
# import time
# from yahoo_finance import Share
# from lxml import html
# import requests
# from datetime import datetime, timedelta
# import re
# from sys import argv

def sendMessage( message ):
    # print(message)
    # conn = http.client.HTTPSConnection("api.pushover.net:443")
    # conn.request("POST", "/1/messages.json",
    #              urllib.parse.urlencode({
    #                  "token": "ardxcuep4y7ay39kpus4cgrvqx7rgh",
    #                  "user": "ux1if13ofopvk7u3k8w5q6d12uukfu",
    #                  "message": message
    #                  }), { "Content-type": "application/x-www-form-urlencoded" })
    # print (conn.getresponse())

    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
        "token": "ardxcuep4y7ay39kpus4cgrvqx7rgh",
        "user": "ux1if13ofopvk7u3k8w5q6d12uukfu",
        "message": message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    return

# def loadGainers():
# 	print "loadGainers"
# 	array = []
# 	gainerSet = set()
# 	url = "http://finance.yahoo.com/gainers"
# 	f = urllib.urlopen(url)
# 	html = f.read()
# 	gainers = [m.start() for m in re.finditer('"gainers":', html)]
# 	positions = [m.start() for m in re.finditer('"symbol":', html)]
# 	for p in positions:
# 		if p > gainers[2]:
# 			symbol_raw = html[p+10:p+19]
# 			parenth = [m.start() for m in re.finditer('"', symbol_raw)]
# 			#print symbol_raw[:parenth[0]]
# 			array.append(symbol_raw[:parenth[0]])
# 			gainerSet.add(symbol_raw[:parenth[0]])
#
# 	# print todays gainers into todays-gainers.txt
# 	fout = open('todays-gainers.txt', 'w')
# 	first = False
# 	for g in array:
# 		if first:
# 			fout.write('\n')
# 		fout.write(g)
# 		first = True
# 	fout.close()
#
# 	# adds all past gainers to set
# 	f = open("all-gainers.txt","r")
# 	for line in f:
# 		gainerSet.add(line.replace('\n', ''))
#
# 	# print all gainers (past and todays) into all-gainers.txt
# 	fout = open('all-gainers.txt', 'w')
# 	first = False
# 	for g in gainerSet:
# 		if first:
# 			fout.write('\n')
# 		fout.write(g)
# 		first = True
# 	fout.close()
#
# 	return array



sendMessage("this is working!")
