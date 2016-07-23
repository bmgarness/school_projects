class song:

    def __init__(self, title, artist, album):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__times_played = 0

    def __str__(self):
        return '{} by {} from {} (played {} times)'.format(self.__title, self.__artist,
                                                           self.__album, self.__times_played)
    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_album(self):
        return self.__album

    def get_times_played(self):
        return self.__times_played

    def play(self):
        self.__times_played += 1
