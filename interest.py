

start1 = 1000000
start2 = 2000000
start3 = 3000000


for x in range(0,20):
	if x == 5 or x == 10 or x == 15:
		print '${:0,.0f}'.format(start1)
		print '${:0,.0f}'.format(start2)
		print '${:0,.0f}'.format(start3)
		print " "
	start1 = start1 * 1.1
	start2 = start2 * 1.1
	start3 = start3 * 1.1
		
print '${:0,.0f}'.format(start1)
print '${:0,.0f}'.format(start2)
print '${:0,.0f}'.format(start3)
