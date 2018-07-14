#define the variable 'formatter' as a string with four arguments, printed using the "literal"/debugger character
formatter = "%r %r %r %r"

#print the arguments, the numerals 1-4
print formatter % (1, 2, 3, 4)
#print with the arguments being one through four written out, in quotes (quotes will print because of the %r)
print formatter % ("one", "two", "three", "four")
#print with some Boolean values as the arguments
print formatter % (True, False, False, True)
#print the formatter inside itself, this should print the whole string as typed (again because of the %r)
print formatter % (formatter, formatter, formatter, formatter)
#print with some strings as arguments, again the quotes will display because of the %r
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)