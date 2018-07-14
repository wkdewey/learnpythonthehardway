#1 a list of subway stations along a certain line
# towns along a highway
# all the planets in order of distance from the sun
# cities in order of population (if you already know the population)
# a schedule
# the months of the year (if chronology is important)
# a best seller list
# parts in order of how you need to assemble them
# bridges in the Konigsberg bridge problem (this is more complex but the solutions need to be a list?)
# studio albums of a given artist in order of when they were released

albums = ['Murmur', 'Reckoning', 'Fables of the Reconstruction', 'Lifes Rich Pageant',
'Document', 'Green', 'Out Of Time', 'Automatic For The People', 'Monster', 
'New Adventures In Hi-Fi', 'Up', 'Reveal', 'Around The Sun', 'Accelerate', 'Last album whose name I can\'t remember']

albumindex = int(raw_input('which R.E.M. album (by number)?'))
print "R.E.M. studio album no.", albumindex, "is", albums[albumindex-1]

redline = ['Alewife', 'Davis', 'Porter', 'Harvard Square', 'Central', 'MIT', 'Boylston', 'Park Street']


def subway(station):
    print "You are at the station", redline[station], "on the Red Line"
    direction = raw_input("Do you want to go outbound or inbound?")
    distance = int(raw_input("How many stops do you want to travel?"))
   
    if direction == "outbound":
    	if station - distance > 7 or station - distance < 0:
    		print "that is not possible"
    		return station
    	station = station - distance
    elif direction == "inbound":
    	if station + distance > 7 or station + distance < 0:
    		print "that is not possible"
    		return station
    	station = station + distance
    return station
  
station = 3
x = True
while x == True:
    station=subway(station)
    if station == 7:
        x = False
print "You have arrived at", redline[station], "and exit the MBTA"