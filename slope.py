# https://pypi.python.org/pypi/yahoo-finance/1.1.4

import httplib, urllib, time
from yahoo_finance import Share
# from lxml import html
import requests
from datetime import datetime, timedelta
import re
from sys import argv

def sendMessage( message ):
	conn = httplib.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
	  urllib.urlencode({
	    "token": "ardxcuep4y7ay39kpus4cgrvqx7rgh",
	    "user": "ux1if13ofopvk7u3k8w5q6d12uukfu",
	    "message": message,
	  }), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()
	return

def loadGainers():
	print "loadGainers"
	array = []
	gainerSet = set()
	url = "http://finance.yahoo.com/gainers"
	f = urllib.urlopen(url)
	html = f.read()
	gainers = [m.start() for m in re.finditer('"gainers":', html)]
	positions = [m.start() for m in re.finditer('"symbol":', html)]
	for p in positions:
		if p > gainers[2]:
			symbol_raw = html[p+10:p+19]
			parenth = [m.start() for m in re.finditer('"', symbol_raw)]
			#print symbol_raw[:parenth[0]]
			array.append(symbol_raw[:parenth[0]])
			gainerSet.add(symbol_raw[:parenth[0]])

	# print todays gainers into todays-gainers.txt
	fout = open('todays-gainers.txt', 'w')
	first = False
	for g in array:
		if first:
			fout.write('\n')
		fout.write(g)
		first = True
	fout.close()

	# adds all past gainers to set
	f = open("all-gainers.txt","r")
	for line in f:
		gainerSet.add(line.replace('\n', ''))

	# print all gainers (past and todays) into all-gainers.txt
	fout = open('all-gainers.txt', 'w')
	first = False
	for g in gainerSet:
		if first:
			fout.write('\n')
		fout.write(g)
		first = True
	fout.close()

	return array

def runAt(h, m, d, function):
	if h == 12 and d == "am":
		h = 0
	if d == 'pm':
		h = h+12

	if time.localtime().tm_hour == h and time.localtime().tm_min == m:
		# string = "it just turned "+str(h)+":"+str(m)+" "+d
		# print string
		function()
		time.sleep(60) # delays for 1 minute

def sendAt(h, m, d, string):
	if h == 12 and d == "am":
		h = 0
	if d == 'pm':
		h = h+12

	if time.localtime().tm_hour == h and time.localtime().tm_min == m:
		sendMessage(string)
		time.sleep(60) # delays for 1 minute

def printPotentials(potentials):
	message = ""
	for p in potentials:
		stock = Share(p)
		price = float(stock.get_price())
		o = float(stock.get_open())
		change = (1.0-(o/price))*100.0
		message += "______ "+p+" ______\nprice="+str(price)+"\nchange="+str(change)+"\n"
	# print message
	sendMessage(message)

def strategy1():
	print "strategy1"
	# the purpose of this strategy is to make sure the stock is progressing
	# upwords and has been gradually increasing. I don't want a stock that
	# isn't a somewhat straight line
	# potentials = set()
	potentials = []
	f = open("todays-gainers.txt","r")
	for line in f:
		name = line.replace('\n', '')
		# print name

		stock = Share(name)
		# print "open: "+stock.get_open()
		# print "high: "+stock.get_days_high()
		# print "low: "+stock.get_days_low()
		# print "curr: "+stock.get_price()
		if stock.get_open() is not None:
			oo = stock.get_open()
			hh = stock.get_days_high()
			cc = stock.get_price()
			if type(oo) is str and type(hh) is str and type(cc) is str:
				o = float(oo)
				h = float(hh)
				# l = float(stock.get_days_low())
				c = float(cc)
				delta_open_cur = c-o
				delta_high_cur = abs(h-c)
				# delta_low_open = abs(l-o)
				if delta_open_cur != 0.0 and delta_high_cur != 0.0:
					difference_high = delta_high_cur/delta_open_cur*100.0
				else:
					difference_high = 0
				# difference_low = delta_low_open/delta_open_cur*100.0
				if difference_high < 35 and difference_high > -1:
					# print "LOOK AT THIS ONE"
					potentials.append(name)
					print name
					change = (1.0-(o/c))*100.0
					print change
					print "---------------"
				# print "DIFFERENCE:  "+str(difference_high)
				# print "DIFFERENCE LOW:  "+str(difference_low)

	# message = "Strategy 1:\n"
	# message += "These are potentials\n"
	# message += str(potentials)
	# sendMessage(message)
	# printPotentials(potentials)
	return potentials

def strategy2(potentials):
	today = datetime.today()
	days_ago = datetime.today() - timedelta(days=5)
	for p in potentials:
		stock = Share(p)
		historical = stock.get_historical(str(days_ago.date()), str(today.date()))
		print "-------------------"
		print p
		for h in historical:
			print "date: "+h['Date']
			print "high: "+h['High']
			print "low: "+h['Low']
			print "close: "+h['Close']
			print "open: "+h['Open']
			o = float(h['Open'])
			c = float(h['Close'])
			print "change: "+str((1.0-(o/c))*100.0)



################################################

today = datetime.today()
days_ago = datetime.today() - timedelta(days=5)

f = open("stocks.txt","r")
for line in f:
	name = line.replace('\n', '')
	print "--------- " + name + " ---------"

	stock = Share(name)
# print stock.getinfo()
# print stock.get_price()
# print stock.get_open()
# print stock.get_price()
	historical = stock.get_historical(str(days_ago.date()), str(today.date()))
	for h in historical:
		print "date: "+h['Date']+", high: "+h['High']+", low: "+h['Low']+", close: "+h['Close']+", open: "+h['Open']
		o = float(h['Open'])
		c = float(h['Close'])
# 		print "change: "+str((1.0-(o/c))*100.0)
		change = (1-(float(h['Open'])/float(h['Close'])))*100
		print "      change: "+ str((1-float(h['Open'])/float(h['Close']))*100)

	print " "


# stock = Share(name)
# print "open: "+stock.get_open()
# print "high: "+stock.get_days_high()
# print "low: "+stock.get_days_low()
# print "curr: "+stock.get_price()






################################################

# today = datetime.today()
# days_ago = datetime.today() - timedelta(days=5)
# stock = Share('IOTS')
# print stock.getinfo()
# print stock.get_price()
# print stock.get_open()
# print stock.get_price()
# historical = stock.get_historical(str(days_ago.date()), str(today.date()))
# for h in historical:
# 	print "date: "+h['Date']
# 	print "high: "+h['High']
# 	print "low: "+h['Low']
# 	print "close: "+h['Close']
# 	print "open: "+h['Open']
# 	o = float(h['Open'])
# 	c = float(h['Close'])
# 	print "change: "+str((1.0-(o/c))*100.0)
	# change = (1-(float(h['Open'])/float(h['Close'])))*100
	# print "change: "+((1-float(h['Open'])/float(h['Close']))*100)

# print time.localtime().tm_hour
# print time.localtime().tm_min

  # 'Adj_Close':'35.830002',
  # 'High':'35.889999',
  # 'Low':'34.119999',
  # 'Date':'2014-04-29',
  # 'Close':'35.830002',
  # 'Open':'34.369999'
