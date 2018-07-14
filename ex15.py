#loads the agrv module so you can get arguments from the command line
from sys import argv
#"unpacks" from the argument line filename (and script which is the name of the python program)
script, filename = argv
#opens the file and assigns file to the variable txt (but opening just allows the file to be used, it's not like opening it in Word)
txt = open(filename)
#print name of file (from the argument provided at the command line)
print "Here's your file %r:" % filename
#reads the text into memory then displays it
print txt.read()
#print an explanation for the prompt below
print "Type the filename again:"
#gets the name of the file from user input, to variable file_again
file_again = raw_input("> ")
#"opens" the file to variable txt_again
txt_again = open(file_again)
#again reads and prints the text of the file
print txt_again.read()
close(txt_again)
close(txt)