# https://pypi.python.org/pypi/yahoo-finance/1.1.4

import httplib, urllib, time
from yahoo_finance import Share
# from lxml import html
import requests
from datetime import datetime, timedelta
import re
from sys import argv


def strategy1():
	print "api info"

	potentials = []
	f = open("stocks.txt","r")
	for line in f:
		name = line.replace('\n', '')
		print name

		stock = Share(name)
        print "---------------"
        print name
        # print "open: "+stock.get_open()
        # print "high: "+stock.get_days_high()
        # print "low: "+stock.get_days_low()
        # print "curr: "+stock.get_price()
        print stock.get_price()
        print stock.get_change()
        print stock.get_percent_change()
        print stock.get_volume()
        print stock.get_prev_close()
        print stock.get_open()
        print stock.get_avg_daily_volume()
        print stock.get_stock_exchange()
        print stock.get_market_cap()
        print stock.get_book_value()
        # print stock.get_ebitda()
        # print stock.get_dividend_share()
        # print stock.get_dividend_yield()
        print stock.get_earnings_share()
        print stock.get_days_high()
        print stock.get_days_low()
        # print stock.get_year_high()
        # print stock.get_year_low()
        # print stock.get_50day_moving_avg()
        # print stock.get_200day_moving_avg()
        # print stock.get_price_earnings_ratio()
        # print stock.get_price_earnings_growth_ratio()
        # print stock.get_price_sales()
        print stock.get_price_book()
        print stock.get_short_ratio()
        # print stock.get_trade_datetime()
        # print stock.get_historical(start_date, end_date)
        # print stock.get_info()
        # print stock.get_name()
        # print stock.refresh()
        # print stock.get_percent_change_from_year_high()
        # print stock.get_percent_change_from_year_low()
        # print stock.get_change_from_year_low()
        # print stock.get_change_from_year_high()
        # print stock.get_percent_change_from_200_day_moving_average()
        # print stock.get_change_from_200_day_moving_average()
        # print stock.get_percent_change_from_50_day_moving_average()
        # print stock.get_change_from_50_day_moving_average()
        # print stock.get_EPS_estimate_next_quarter()
        # print stock.get_EPS_estimate_next_year()
        # print stock.get_ex_dividend_date()
        # print stock.get_EPS_estimate_current_year()
        # print stock.get_price_EPS_estimate_next_year()
        # print stock.get_price_EPS_estimate_current_year()
        # print stock.get_one_yr_target_price()
        print stock.get_change_percent_change()
        # print stock.get_dividend_pay_date()
        # print stock.get_currency()
        # print stock.get_last_trade_with_time()
        # print stock.get_days_range()
        # print stock.get_year_range()











        #   i <3 nate
        #   who is nate?
        #   you?
        #   Oh! :0
        #   :) do you love me?
        #   SIIIIIIIIIIIIIIIIIIIIIIIIIII
        #
        # print "---------------"
		# if stock.get_open() is not None:
		# 	oo = stock.get_open()
		# 	hh = stock.get_days_high()
		# 	cc = stock.get_price()


strategy1()
