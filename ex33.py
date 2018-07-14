def whiletest(x, incr):
	
	max = range (0, x, incr)
	list = []
	for i in max:
		print "At the top i is %d" % i
		list.append(i)
	
		print "Numbers now: ", list
		print "At the bottom i is %d" % i
	return list
		

limit = 88
increment = 4

numbers = whiletest(limit, increment)

print "The numbers: "

for num in numbers:
	print num