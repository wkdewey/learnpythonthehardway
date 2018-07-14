print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

name = raw_input('enter your name:')
print "hi %s, Let us be friends!" % name
number = raw_input ('give me a number')
print "your lucky number is: %d" % (int(number) % 4)