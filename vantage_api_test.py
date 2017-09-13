import requests
import json
import urllib
import re




# r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=15min&outputsize=full&apikey=I6V26BU17WRH6Y2Y")
# # 3CKYXLMAE7B21YP0
# # print r.status_code
# # print r.headers
# print r.content
# res = json.loads(r.content)
# series = res['Time Series (15min)']
# # print series['2017-07-05 14:45:00']
# dates = []
# for s in series:
#     date = s.split()
#     # print date[0]
#     dates.append(date[0])

# print '-------'
# dates.sort(reverse=True)
# for d in dates:
#     print d
# print dates


loadGainers()
