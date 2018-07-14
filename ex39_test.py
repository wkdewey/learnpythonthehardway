import hashmap

# create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# creates a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')


# print out some cities
print '-' * 10
assert hashmap.get(cities, 'NY') == 'New York'
assert hashmap.get(cities, 'OR') == 'Portland'

# print some states
print '-' * 10
assert hashmap.get(states, 'Michigan') == 'MI'
assert hashmap.get(states, 'Florida') == 'FL'

# do it by using the state then cities dict
print '-' * 10
assert hashmap.get(cities, hashmap.get(states, 'Michigan')) == 'Detroit'
assert hashmap.get(cities, hashmap.get(states, 'Florida')) == 'Jacksonville'

# print every state abbreviation
print '-' * 10
hashmap.list(states)
hashmap.dump(states)

# print every city in state
print '-' * 10
hashmap.list(cities)
hashmap.dump(cities)

print '-' * 10
assert hashmap.get(states, 'Texas') != 'TX', "Sorry, no Texas."

	
# default values using ||= with the nil result
# can you do this on one line?
assert hashmap.get(cities, 'TX') == 'Dallas', 'Does Not Exist'