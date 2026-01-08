class song_set:
    def __init__(self, artist: str, album: str, track: str, time: int):
        self.artist = artist
        self.album = album
        self.track = track
        self.time = time
    @property
    def time(self):
        return self._time
    @time.setter
    def time(self, value):
        if value < 0:
            self._time = 0
    def __str__(self):
        return f'''song {self.track} is from {self.album}, 
        it was created by {self.artist} and is {self._time} seconds long.'''
    
class rock(song_set):
    def __init__(self, artist, album, track, time, year: int): #jakie wlasnosci przyjmuje
        super().__init__(artist, album, track, time) #co jest dziedziczone
        self.year = year
    @property
    def time(self):
        raise NotImplementedError("enjoy the moment, stop living in the future!")
    @time.setter
    def time(self, value):
        pass
    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self, value):
        cool = ["Arctic Monkeys", "The Police", "Paramore", "Oasis"]
        if value not in cool:
            raise ValueError("nahh pick sth else hm?")
        self._artist = value

    def __str__(self):
        return f'''song {self.track} is from {self.album} album,
        it was created by {self.artist} in {self.year}'''
    
tryout = rock("Oasis", "Britpop", "Wonderwall", 258, 1995)
print(tryout)
#print(tryout.time)
