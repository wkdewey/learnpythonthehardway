print True and False
global x 
x = 1
assert x == 1, "Error error error!"

def testfunction(somenumber):
	try:	
		somenumber = somenumber*somenumber
	except TypeError:
		print "somenumber isn't a number, resetting it"
		somenumber = 0
		print x
	finally:
		return somenumber
		
othernumber=testfunction(50)
print othernumber
fakenumber=testfunction('yes')
print fakenumber


with open("test.txt") as f:
	print f.read()
	
for i in range (0, 10):
	print i
	if i == 5:
		break

class MontyPython:
	kind = "Monty snake"
	
	def __init__(self, name):
		self.name = name
	
	def length(self, name):
		return len(name)
		
	def EmptyClass(self):
		pass
		
d = MontyPython("Terry")
print d.kind
print d.name
print d.length

y = True
while y == True:
	response = raw_input("True or False?")
	if response == "True":
		continue
	elif response == "False":
		 y = False
	else:
		print "not an option"
		continue
	
testlist = ['alpha', 'beta', 'gamma', 'delta']
print testlist
print "deleting.."
del testlist[3]
if "gamma" in testlist:
	print "yes"
else:
	print "no"
print testlist
exec raw_input("Give me a command:\n")
for i in testlist:
	print i
	print len(i)

from math import sin
print sin(3.14)
print x is y

def make_incrementor(n):
	return lambda x: x + n
	
f = make_incrementor(42)
print f(0)
print f(1)

print not (True or False)

def CreateGenerator():
	mylist = range(0, 3)
	for i in mylist:
		yield i*i
		
mygenerator = CreateGenerator()
print mygenerator
for i in mygenerator:
	print i
	
print "\\"
print '\''
print "\""