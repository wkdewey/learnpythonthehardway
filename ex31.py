print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	else:
		print "Well, doing %s is probably better.  Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	elif insanity == "3":
		print "Colorless green ideas sleep furiously in Noam Chomsky's holiday in Cambodia. The last thing you see is Pol Pot approaching with a shovel."
	elif insanity == "Huh?":
		print "You realize Cthulhu is just a figment of your imagination. The room is entirely bare. You turn around and go home."
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"
		
else:
	print "It is pitch black. You are likely to be eaten by a grue. What do you do you?"
	print "1. Light a lantern"
	print "2. Fight the grue"
	
	grue = raw_input("> ")
	
	if grue == "1":
		print "The grue disappears, revealing a large spiral staircase. Your next move?"
		print "1. Go down"
		print "2. Go up"
		
		staircase = raw_input("> ")
		
		if staircase == "1":
			print "Abandon all hope, ye who enter here."
		elif staircase == "2":
			print "'And she's buying a staircase to heaven...' Unfortunately it doesn't go up all the way. You plunge 13859172810769103 feet to the ground."
		else:
			print "You are stuck in purgatory for eternity"
	elif grue == "2":
		print "Congratulations, you have discovered the secret to Zork! The grue dissolves into a puff of smoke at the touch, revealing an incredible precious gemstone. You win."
		
	else:
		print "The grue doesn't understand that answer. So he eats you."