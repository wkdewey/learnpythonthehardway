cities = {
	'Punjab': 'Amritsar',
	'Uttar Pradesh': 'Lucknow',
	'Tamil Nadu': 'Chennai'
}

cities['West Bengal'] = 'Kolkata'
cities['Telangana'] = 'Hyderabad'

print "Punjab has: ", cities['Punjab']
print "West Bengal has: ", cities['West Bengal']

for state, city in cities.items():
	print "%s state has the city %s" % (state, city)
	
city = cities.get('Kerala')
if not city:
	print "Sorry, no Kerala"
	
city = cities.get('Kerala', 'Does Not Exist')
print "The city for state Kerala is: %s" % city
cities.clear()
print cities
citylist = [('Punjab', 'Amritsar'), ('Uttar Pradesh', 'Lucknow'), ('Tamil Nadu', 'Chennai')]
cities = dict(citylist)
print cities
