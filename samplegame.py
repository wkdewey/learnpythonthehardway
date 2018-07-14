print "You are in front of a large console with 3 buttons and a large screen. Do you:"
print "1. Press the blue button."
print "2. Press the red button."
print "3. Press the green button."
print "4. Read the screen."

console = raw_input("c:\\")
console = float(console)
if not (1 <= console <= 4):
	print "That wasn't an option. The machine grows fangs and eats you."
else:
	if 1 <= console <= 3:
		if console == 1:
			print "The console and room disappear instantly. \nYou find yourself in the middle of the ocean, with no lifejacket and no land in sight."
		else:
			if console == 2:
				print "The console and room disappear instantly. \nYou find yourself on the surface of the sun, for a split second before you fry."
			else:
				if console == 3:
					print "The console and room disappear instantly. \nYou find yourself on the moon which is indeed made of green cheese. But you have no spacesuit, in fact you are naked."
				else:
					print "The machine does absolutely nothing. How disappointed. You get bored and leave."	
	else:
		print "You notice a message on the screen saying 'do not press any of the buttons. Or Else.'"
		if console == 4:
			print "You turn around and go home."
		else:
			print "Naturally, you press all three buttons at once."
			print "The room starts spinning."
			print "The console retracts into the floor."
			print "The room itself disappears."
			print "You find yourself in Lhasa, in front of the Potala. Do you:"
			print "1. Chant Om Mani Padme Hum."
			print "2. Yell 'Free Tibet!' (in Tibetan, of course)"
			tibet = raw_input("Mac-d0e1409e9ec4 yourname$")
			if tibet == "1":
				print "Congratulations, you have obtained enlightenment!"
			elif tibet == "2":
				print "You expect a bunch of Red Guards to show up."
				print "But instead a bunch of monks stare at you blankly. In fact it is 1653. The new Dalai Lama is being enthroned."
				print "Suddenly a voice says, 'He's the one! He's the missing lama!'"