from sys import argv

script, filename = argv
txt = open(filename)
print "contents of %s" % filename
print txt.read()