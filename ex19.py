#defines the function cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print number of cheeses with argument cheese_count
	print "You have %d cheeses!" % cheese_count
	# print number of cheese with argument boxes_of_crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#print a statement (doesn't depend on the arguments)
	print "Man that's enough for a party!"
	#print a statement plus a blank line
	print "Get a blanket.\n"
	
#explanatory statement
print "We can just give the function numbers directly:"
#call the function with arguments 20 and 30
cheese_and_crackers(20,30)

#prints an explanatory statement	
print "OR, we can use variables from our script:"
#define first variable which will be used in the function
amount_of_cheese = 10
#define second variable which will be used in the function
amount_of_crackers = 50
#call the function with the above variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#print a statement
print "We can even do math inside too:"
#calls the function by adding two numbers to determine each argument
cheese_and_crackers(10 + 20, 5 + 6)

#print a statement
print "And we can combine the two, variables and math:"
#call the function by adding the (previously assigned) variable to a number
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)