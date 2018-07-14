def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap = []
	for i in range(0, num_buckets): #creates num_buckets lists within the list
		aMap.append([]) #make a list (within aMap)
	return aMap
	
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to
	an index for the aMap's buckets."""
	return hash(key) % len(aMap) # unique identifier, modulus 256
	
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key) #this is a number between 0 and 256
	return aMap[bucket_id] #one of the lists, the "bucket"

def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key) # the bucket within the map
	
	for i, kv in enumerate(bucket): #goes thorugh the list but it should be empty intially
		k, v = kv #each list element will be a tuple
		if key == k: #sees if the key matches
			return i, k, v #exits the loop with item key and value
			
	return -1, key, default # returns -1, the key, and "None" or whatever alternate response was fed into the function
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default) #gets i, k and, v based on the key
	return v #returns the value, or "default" if not found
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key) #finds the particular bucket
	i, k, v = get_slot(aMap, key) #checks to find if the key is there; -1 for index if not
	
	if i>= 0:
		# the key exists, replace it
		bucket[i] = (key, value) # changes the list at the correct index, to the desired key and value
	else:
		# the key does not, append to create it
		bucket.append((key, value)) # adds the key value tuple to the bucket list
		
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key) #finds the bucket by number
	
	for i in xrange(len(bucket)): #len(bucket) is number of items in bucket; xrange is just a memory-efficient version of range
		k, v = bucket[i] # gets the key and value
		if key == k: #checks to see of the key is there
			del bucket[i] #then deletes the entry in the bucket (based on the index number, given by the for loop)
			break

def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap: #go through each bucket
		if bucket: #make sure the bucket isn't empty
			for k, v in bucket: #list of tuples
				print k, v #print the key and value
				
def dump(aMap):
	"""Prints contents of every bucket."""
	for bucket in aMap:
		print bucket,