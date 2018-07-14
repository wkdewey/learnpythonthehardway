print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#space after a newline will mean the next line will start with a space

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#defines a function 'secret_formula' taking a starting number
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	#returns the variables jelly_beans, jars, crates from the above calcuations
	return jelly_beans, jars, crates
	
start_point = 10000
#calls the formula secret_formula with the variable start_point, then assigns the return variables
#to variables beans, jars, crates; corresponding variables as the arguments or return values do not need to have the same names
beans, jars, crates = secret_formula(start_point)

#prints the calculations we just made
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#runs the function with the start variable, prints the three return variables
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)