from sys import exit


def delhiairport(list):	
	print "%r" % list
	print "You have landed at Delhi Airport for your great Indian adventure."
	print "After clearing customs, you open up your guidebook to the 'Delhi' bookmark"
	print "where 'Hotel Asoka' is circled"
	print "As you do this, ten men surround you, all asking 'Rickshaw? Where going?'"
	print "Do you: 1. Get in a rickshaw"
	print "2. follow the signs to the Delhi Metro"
	#make user pick an option, rickshaw or metro
	transitmode = raw_input("> ")
	if transitmode == "1":
		delhirickshaw(list)
	elif transitmode == "2":
		delhimetro(list)
	else:
		dead("You wander around the airport, until the customs guys deport you.")
	
def delhirickshaw(list):
	print "%r" % list
	#user should choose whether to take rickshaw driver's advice, or insist on right hotel
	print "You get in and tell the rickshaw driver, 'Please go to Hotel Ashoka'"
	print "He looks puzzled, and insists on looking at your guidebook"
	print "Then he says, 'Oh, Hotel Asoka has been closed for two months'"
	print "'But you can go to my brother's place, Hotel Ashoka'"
	print "What do you tell him?"
	#open ended response, either leads to your hotel or tout's hotel
	driver = raw_input("> ")
	#you have to say 'Asoka'
	if 'Asoka' in driver:
		goodhotel(list)
	elif 'Ashoka' in driver or 'brother' in driver:
		touthotel(list)
	else:
		print "The driver says 'No good english'. You decide to leave."
		delhiairport(list)

def delhimetro(list):
	print "%r" % list
	print "You squeeze yourself and your luggage into a very crowded subway train"
	print "There is scarecely enough room to breathe"
	print "Suddenly you notice you are standing next to a masked man whose belly seems oddly fat"
	print "There is a wire hanging out of his shirt on his neck"
	print "What do you do?"
	#open ended response
	terrorist = raw_input("> ")
	if 'wire' in terrorist:
		print "He says (in perfect English) 'What's your problem' and gets off at the next stop"
		print "The next morning you read the headline 'Attempted suicide bomber caught in Delhi Metro'"
		goodhotel(list)
	else:
		dead("The man pushes a button and blows you and everyone else in the train to bits.")

def touthotel(list):
	print "%r" % list
	print "You arrive at Hotel Ashoka. Something looks wrong about this place. It is much more ramshackle than the pictures on Tripadvisor."
	print "You begin to check in anyway. The reception guy gives the rickshaw driver a couple of banknote."
	print "Then he launches into a long sales pitch about tours to Kashmir, pashmina shawls, and hash. As he enters your information into the guestbook, he demands to see your passport."
	#three options
	print "1. Give him the passport. You are tired and can find another hotel later."
	print "2. Refuse. leave and try to find another rickshaw."
	print "3. Argue with your rickshaw driver and try to convince him to go to the address listed in your guidebook."
	passport = raw_input("> ")
	#only option 3 will lead to the right hotel 2 will get you lost 1 will make you a prisoner
	if passport == "1":
		print "Bad move. After an hour passes, they insist you have an expired passport and threaten to turn you in."
		print "After stealing all your money (and your credit card numbers) they allow you to return to the airport, emptyhanded"
		delhiairportend(list)
	elif passport == "2":
		print "There are no rickshaws on the street at this hour. You wander around Delhi until you collapse from exhaustion."
		dead("Since it is January (cold, even in India) you are found the next morning on the pavement, dead from exposure.")
	elif passport == "3":
		print "After much cajoing, bribery and threats, he drives to Hotel Asoka (the hotel you actually intended in the first place)"
		goodhotel(list)
	else:
		print "that wasn't an option"
		touthotel(list)

def goodhotel(list):
	print "%r" % list
	print "You arrive at Hotel Asoka. The receptionist is polite and bring up the reservation without issue."
	print "As you arrive in your room, you feel incredibly tired. But your friend advised staying up all night."
	print "The room is clean and has all the usual amenities. But the decor looks hastily put together."
	print "The picture frame above the bed seems oddly placed, and is hanging at a slight tilt."
	#open-ended, chance to find something
	sleep = raw_input("> ")
	if 'picture' in sleep:
		print "You knock down the picture, revealing Narendra Modi's original RSS membership papers."
		if "Modi RSS papers" not in list:
			list.append("Modi RSS papers")
		sleep = sleep + raw_input("What about sleeping?")
	if 'sleep' in sleep:
		print "That was a good decision. You manage to sleep about four hours. You are bleary eyed, but functional."
		print "After a little breakfast you exit your hotel."
		paharganj(list)
	elif 'stay' in sleep or 'awake' in sleep:
		print "For about half an hour you find it difficult to lift your eyelids, but then it is possible."
		print "But by morning time you are absolutely crazy from sleep deprivation."
		print "You wander the city aimlessly and find yourself in a shop"
		fakeemporium(list)
	else:
		print "Wow, traveling has really taken a toll on you. That made no sense at all."
		goodhotel(list)

def paharganj(list):
	print "%r" % list
	print "You are out on the main bazaar of Paharganj. From here you can walk to the train station,"
	print "or take the subway to the sights of Delhi such as Hauz Khas, the Old City, and Connaught Place."
	print "Or else you can return to the Delhi airport if you think you have seen enough."
	print "A funnily-dressed hippie is standing in the middle of the street, whispering 'coke, weed, hash'"
	direction = raw_input("> ")
	print direction
	if 'hauz' in direction or 'Hauz' in direction:
		hauzkhas(list)
		
	elif 'city' in direction or 'City' in direction:
		jamamasjid(list)
		
	elif 'connaught' in direction or 'Connaught' in direction:
		connaughtplace(list)
		
	elif 'station' in direction or 'Station' in direction:
		delhirailway(list)
		
	elif 'airport' in direction or 'Airport' in direction:
		delhiairportend(list)
		
	elif 'talk' in direction:
		print "You ask the hippie just exactly he thinks he's doing, selling drugs in the open air. He replies that the drug dealer thing is just an act."
		print "'Actually, I am a former disciple of the famous Yogi Gorakhnath Gordon Patanjali before we had a falling out."
		print "'Here is his specially blessed golden prayer beads, I no longer want them on my hands.'"
		if "Yogi's prayer beads" not in list:
			list.append("Yogi's prayer beads")
		paharganj(list)
	elif 'drugs' in direction or 'buy' in direction: 
		dead("A plain clothes cop instantly emerges from the crowd to arrest you. You spend 10 years in India prison before you are released.")
	else:
		print "Confused, you stroll up and back down the bazaar to collect your thoughts"
		paharganj(list)

	
def hauzkhas(list):
	print "%r" % list
	print "You arrive at Hauz Khas, then stroll through the street, lined with the sort of shops"
	print "You enter an antique store, filled with old Bollywood posters, books, and classic advertising signs."
	print "The woman in charge enquires, 'may I tell you about a special deal'?"
	antique = raw_input("> ")
	if "yes" in antique:
		print "'A long time ago, someone gave me old papers. They look important but I have no idea what they are."
		print "If you will buy my Raj Kumar posters, I will give them to you to.'"
		print "Since you can read old Persian, you see than this is the Mughals' original charter to the East India Company. Keeping your mouth shut, you agree."
		if "EIC Charter" not in list:
			list.append("EIC Charter")
	else:
		print "You eventually buy an Amitabh Bacchan poster from the film Sholay. After you get back to your hotel you realize it is a worthless photocopy, and toss it in the trash."
	paharganj(list)

def jamamasjid(list):
	print "%r" % list
	print "You wander through the narrow alleys of old Delhi until you reach the Jama Masjid, an impressive Mughal-era mosque"
	print "An man wearing a white lattice cap offers to show you around the mosque. also there are signs to climb a tower."
	print "Do you 1. take the tour 2. walk up the tower 3. go into the mosque yourself."
	mosque = raw_input("> ")
	if mosque == "1":
		print "He demands a little too much money, but after some haggling you agree on the price and he proceeds to show you all the mosque's architectural features."
		print "At the corner of the prayer room, he removes some excellent Mughal inlay, a trap door to a small chamber."
		print "In it are some of Akbar's prize manuscripts, outlining his radical religious ideas."
		print "'Here, have these, a gift!' the guide says."
		if "Akbar's manuscripts" not in list:
			list.append("Akbar's manuscripts")
		paharganj(list)
	elif mosque == "2":
		print "After an exhausting climb, you see a extraordinary view of Delhi "
		dead("But you slip on a wet surface and career over the balcony, plunging 250 feet to the ground.")
	elif mosque == "3":
		print "You look around yourself, but you (having no knowledge of mosques) have no idea what's what."
		print "A crowd begins to arrive for the noon prayer. Having a vague sense that you are likely to make a faux pas at this holy place, you decide to go home."
		paharganj(list)
	else:
		print "C'mon, make up your mind!"
		jamamasjid(list)


def delhirailway(list):
	print "%r" % list
	print "You are in the train station. you go to the counter and after a long wait, buy a ticket for Agra"
	print "The train should arrive in an hour, but the time keeps getting pushed back as you watch the signboard."
	print "Finally the delays cease, but the train never gets a platform number. Now it is 5:05 but the train is still scheduled for 5"
	print "Suddenly the train name vanishes from the signboard. There is an info booth but it is surrounded by a horde of people."
	print "What do you do?"
	train = raw_input("> ")
	if "platform" in train or "info" in train:
		print "You frantically ask the people in the info booth and other passengers where the Agra train is."
		print "Someone finally says, 'Platform 5', you run up and down the stairs and board the train,"
		print "ten seconds before it leaves the station"
		agrarailway(list)
	if "wait" in train:
		print "You stare at the signboard for about two hours. Finally you see what looks like your train, on platform 4."
		print "You board it, but it never reaches Agra. After two days you find yourself in Chennai, South India."
		print "Having not made any preparations to go this far, you have to sell all you own to get a hotel room, and a flight back."
		list = []
		delhiairportend(list)
	else:
		print "You are really confused."
		delhirailway(list)

def connaughtplace(list):
	print "%r" % list
	print "You arrive in Connaught Place, Delhi's British-style downtown which is arranged in concentric circles"
	print "In your guidebook, you have marked 'Fabindia' as a place you must shop to get souvenirs."
	print "You are a bit disoriented, and a man asks you 'Where going?' You answer, 'Fabindia'."
	print "He says, that place is closed. But I can show you a similar place."
	print "Do you 1. follow the guide 2. try to find Fabindia yourself?"
	store = raw_input("> ")
	if store == "1":
		fakeemporium(list)
	elif store == "2":
		fabindia(list)
	else:
		print "Sensing your indecision, the guide demands you follow him. You don't resist."
		fakeemporium(list)
	 

def fabindia(list):
	print "%r" % list
	print "Ignoring the tout, you look at the guidebook again and try to find your bearings. You go around the corner and find Fabindia."
	print "Your mother asked you to look for a red sari. There doesn't seem to be anything in the main section. A sign saying 'kurtas' leads"
	print "back to a dingy room that you aren't sure is actually part of the store."
	kurta = raw_input("> ")
	if "kurtas" in kurta or "back" in kurta or "in" in kurta:
		print "You enter the room, and of course don't find any red Saris."
		print "However, you are instantly drawn to a plain white kurta that looks 100 years old."
		print "The salesman rings it up for a reasonable 600 Rs, on examining it you see that it was owned by one Mahatma Gandhi, the original receipt still lying in the pocket."
		if "Gandhi's kurta" not in list:
			list.append("Gandhi's kurta")
		paharganj(list)
	else:
		print "You finally buy some red Saris, which are in rather poor taste (even considering your lack of knowledge of Indian fashion)."
		print "You later decide to give them away, being too embarassed to show them to your mother."
		paharganj(list)

def fakeemporium(list):
	print "%r" % list
	print "Following the guide, you arrive at 'Central Cottage industries, ltd.'"
	print "After making you sit through a long sales pitch, you try to leave. They accuse you of shoplifting and strip you of your valuables."
	print "You head back toward your hotel."
	list = []
	paharganj(list)

def agrarailway(list):
	print "%r" % list
	print "After a long journey, you finally arrive in the Agra station. you head toward the rickshaw stand. Two beggars follow, saying 'one rupee, please'"
	print "A third bumps you from behind. You shake them off and continue toward the rickshaws, but you have a nagging feeling something has gone wrong. What do you do?"
	pickpocket = raw_input("> ")
	if "run" in pickpocket:
		print "That does no good, unfortunately they made off with all your possessions. But you decide to go to the Taj anyway, just to escape them."
		list = []
	elif "thief" in pickpocket:
		print "Alerting the crowd, you manage to start a small riot. The mob surrounds and beats the alleged thief to death, but they have the wrong man and he has none of your stolen property."
		dead("The beggar mafia quickly regroups for their revenge, and as you leave the station, you are knifed in the back.")
	elif "confront" in pickpocket:
		print "You grab the beggar who bumped you. He says, 'Here, you dropped this' and hands you back all the possessions he stole."
		print "not wanting to cause a scene, you continue on your way."
	else:
		print "Bewildered, you continue as if nothing has happened. Later you discover that all the treasure has been taken."
		list = []
	tajmahal(list)

def tajmahal(list):
	print "%r" % list
	print "your rickshaw drops you off in front of the Taj Mahal (somehow you have gotten the only honest rickshaw in Agra)"
	print "You buy your ticket and walk thorugh the gate. It is more impressive than the pictures, even though you expected to be disappointed."
	print "You enter the shrine room and notice that the coffin of Shah Jahan is slightly ajar. A guard looks at you watchfully."
	guard = raw_input("> ")
	if "open" in guard or "coffin" in guard:
		print "The guard arrests you on the spot"
		dead("you serve a five year sentence in an Indian prison, after which they finally let you out (confiscating all your treasure, of course).")
	elif "bribe" in guard:
		print "You hand the guard a couple Rs 1000 notes. Remarkably, it works."
		print "He looks the other way while you reach in and retrieve Mumtaz Mahal's emerald necklace."
		if "Mumtaz's necklace" not in list:
			list.append("Mumtaz's necklace")
	else:
		print "Losing your nerve, you decide to leave the coffin alone and exit the room."
	print "After leaving the Taj you make your way back to Delhi, without incident."
	paharganj(list)
	
def dead(why):
	#print a final message
	print why, "Your journey has now ended"
	print "Final score is zero"
	#end the program
	exit(0)
	
def delhiairportend(list):
	print "%r" % list
	print "You have returned to Delhi airport for your journey home."
	print "your score is: %d" % len(list)
	exit(0)

treasurelist = []
delhiairport(treasurelist)


dead("This program is really buggy, so")