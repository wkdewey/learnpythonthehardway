def add (a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide (a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#35+74-180*100/2)
#(30+5)+(78-4)-(90*2)*((100/2)/2)

print "That becomes: ", what, "Can you do it by hand?"

def circle(a):
	print "the area of a circle with radius %f" % a
	return 3.1415926*a*a
radius = 2
print circle(radius)
formula = subtract(add(24, divide(34, 100)), 1023)
print formula