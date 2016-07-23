import song

class MusicPlayer:

    def __init__(self):
        self.__playlist = []
        self.__current_track_index = 0
        self.__current_track = None

    def __str__(self):
        if self.__current_track == None:
            return '{} tracks. Currently playing...{}'.format(len(self.__playlist), self.__current_track)
        else:
            return '{} tracks. Currently playing...{}'.format(len(self.__playlist), self.__current_track)

    def add_to_playlist(self, song):
        self.__playlist.append(song)

    def play(self):
        if self.__current_track_index >= 0 and self.__current_track_index < len(self.__playlist):
            self.__current_track = self.__playlist[self.__current_track_index]
            self.__current_track.play()
            print('Currently playing...{}'.format(self.__current_track))
        else:
            print('{} is not a valid track number'.format(self.__current_track))

        
    def prev(self):
        self.__current_track_index -= 1
        if self.__current_track_index < 0:
            self.__current_track_index = len(self.__playlist) - 1
        self.play()

    def next(self):
        self.__current_track_index += 1
        if self.__current_track_index == len(self.__playlist):
            self.__current_track_index = 0
        self.play()

    def find(self, search):
        signal = False
        for s in range(len(self.__playlist)):
            if self.__playlist[s].get_title() == search or self.__playlist[s].get_artist() == search:
                print('Found track {}...{}'.format(s, self.__playlist[s]))
                signal = True
        if signal == False:
            print('No matching Songs found for {}'.format(search))
            

    
        
