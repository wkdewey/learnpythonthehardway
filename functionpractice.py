from sys import argv

script, original_width, original_length = argv
def area_of_rectangle(width, length):
	print "The area of the rectangle with sides %r and %r is %f.\n" % (width,length,width * length)
	
area_of_rectangle(20,30)

side_one = 2
side_two = 3

area_of_rectangle(side_one,side_two)

area_of_rectangle(side_one * 10,side_two * 10)

area_of_rectangle(side_one/side_two,side_two/side_one)

area_of_rectangle(side_one % side_two, side_two % side_one)

print "From your command line arguments:"
area_of_rectangle(float(original_width), float(original_length))
user_width = float(raw_input("New width: "))
user_length = float(raw_input("New length: "))
area_of_rectangle(user_width, user_length)
multiplier = float(raw_input("Multiplier: "))
area_of_rectangle(multiplier * user_width,multiplier * user_length)
print "all together now:"; area_of_rectangle(multiplier * user_width * float(original_width), multiplier * user_length * float(original_length))
print "Will this work?"
area_of_rectangle(int(raw_input("another width: ")),int(raw_input("another length: ")))