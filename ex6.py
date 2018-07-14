#define variable x as string and include an integer in it (will be printed with format specifier)
x = "There are %d types of people." % 10
# define variable 'binary' as string
binary = "binary"
# define variable 'do_not' as string
do_not = "don't"
# define variable y as string, including the strings binary and do_not. again uses format specifiers
y = "Those who know %s and those who %s." % (binary, do_not)

#display on screen the string 'x' as defined above
print x
#display on screen the string 'y'
print y

# using the %r character will display the quotes around the string
print "I said: %r." % x
# using the %s character will not display the quotes, so they have to be manually evaluated
print "I also said: '%s'." % y
#define variable 'hilarious' as string
hilarious = False
#define variable 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny?! %r"

#display joke_evaluation with 'hilarious" as the argument (it needs one because of the %r)
print joke_evaluation % hilarious
# define variable w as string
w = "This is the left side of..."
# define variable e as string
e = "a string with a right side."
# example of "adding" two strings together, it just puts one string after the other
print w + e