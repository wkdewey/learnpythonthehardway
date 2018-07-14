from sys import argv

filename, first, second = argv

print "The script is called:", filename
print "Your first variable is:", first
print "Your second variable is:", second
third = raw_input("Complete the phrase: " )
print "%s %s %s" % (first, second, third)