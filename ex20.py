#import the argv variable from the sys module
from sys import argv

#unpack argv into script and input_file variables (from the command line)
script, input_file = argv

#define a function print_all which takes the input f
def print_all(f):
	#prints the contents of the file specified by f
	print f.read()
	
#define a function rewind which also works on f
def rewind(f):
	#goes back to line zero in the file
	f.seek(0)
	
#define a function print_a_line which takes the arguments line_count and f
def print_a_line(line_count, f):
	#prints (the number specified in, then the contents of a line in the file)
	print line_count, f.readline()
	
#open the file (i.e. create a file object) which was specified at the command line, assign it to variable current_file
current_file = open(input_file)

#print statement plus a newline
print "First let's print the whole file:\n"

#call function print_all on current_file (prints all of the file)
print_all(current_file)

#print a statement
print "Now let's rewind, kind of like a tape."

#call function rewind, goes back to the beginning of the file
rewind(current_file)

print "Let's print three lines:"

#variable current_line set to one for the function
current_line = 1 
#calls print_a_line with the arguments current_line and current_file, prints 1 and a line
print_a_line(current_line, current_file) #current_line is 1; this is given to the function prints_a_line and thus becomes line_count (as the corresponding 1st argument) then is printed

#increment current_line
current_line += 1
#calling the function print_a_line, prints line number and the corresponding line
print_a_line(current_line, current_file) #current_line 2

#increment current_line
current_line += 1
#calling the function print_a_line, prints line number and the corresponding line
print_a_line(current_line, current_file) #current_line 3