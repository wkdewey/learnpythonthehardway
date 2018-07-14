#sets variable people
people = 2
#sets variable cars
cars = 4
#sets variable trucks
trucks = 5

#true if the number of cars (the value of variable "cars", whatever) is greater than number of people, then runs the "enclosed" instructions
if cars > people:
#prints if the above statement is true
	print "We should take the cars."
#true if the number of cars is less than number of people (only runs if the above statement wasn't true)
elif cars < people:
#prints if the above statement is true (and the if statement wasn't)
	print "We should not take the cars."
#if both the if and the elif were false (i.e. nothing was executed) this will run
else:
#prints a sentence of "last resort" if nothing ran before
	print "We can't decide."
	
#true if the number of trucks is greater than number of people, then runs the "enclosed" instructions
if trucks > cars:
#prints if the above statement is true
	print "That's too many trucks."
#true if the number of cars is less than number of people (only runs if the above statement wasn't true)
elif trucks < cars:
#prints if the above statement is true (and the if statement wasn't)
	print "Maybe we could take the trucks."
#goes to this if both the if and the elif were false
else:
	print "We still can't decide."
	
#true if the number of people is greater than number of trucks
if people > trucks
# prints if the above statement is ture
	print "Alright, let's just take the trucks."
#if the if statement was false
else:
#prints, if the if statement didn't run
	print "Fine, let's stay home then."