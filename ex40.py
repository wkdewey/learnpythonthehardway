class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line,
		print
			
	def firstwords(self):
		for line in self.lyrics:
			print line.split()[0]
			
	def hashes(self):
		for line in self.lyrics:
			print hash(line)
			
	def selfdestruct(self):
		while len(self.lyrics) > 0:
			print self.lyrics.pop()
			
happy_bday = ["Happy birthday to you",
				"I don't want to get sued",
				"So I'll stop right there"]
					
bulls_on_parade = ["They rally around tha family",
					"With pockets full of shells"]
						
Song(happy_bday).sing_me_a_song()

Song(bulls_on_parade).sing_me_a_song()

losing_my_religion = ["That's me in the corner",
						"That's me in the spotlight",
						"Losing my religion",
						"Trying to keep up with you"]
							
water_fountain = ["No water in the water fountain",
					"No side in the sidewalk"]
						
Song(losing_my_religion).sing_me_a_song()
Song(water_fountain).sing_me_a_song()
Song(losing_my_religion).firstwords()
Song(water_fountain).hashes()
Song(happy_bday).selfdestruct()
print happy_bday
Song(happy_bday).sing_me_a_song()