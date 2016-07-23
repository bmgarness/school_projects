import song
import MusicPlayer

def main():
    Music = MusicPlayer.MusicPlayer()
    add_songs(Music)

    Music.play()
    Music.next()
    Music.next()
    Music.next()
    Music.next()
    Music.next()
    Music.prev()
    Music.prev()
    Music.find('Guns n\' Roses')
    Music.find('Times Like These')
    Music.find('Justin Bieber')

def add_songs(Music):
    s1 = song.song('Welcome to the Jungle', 'Guns n\' Roses', 'Appetit for Destruction')
    s2 = song.song('Smells Like Teen Spirit', 'Nirvana', 'Nevermind')
    s3 = song.song('Jeremy', 'Pearl Jam', 'Ten')
    s4 = song.song('Times Like These', 'Foo Fighters', 'One by One')
    s5 = song.song('Sweet Child of Mine', 'Guns n\' Roses', 'Appetite for Destruction')

    Music.add_to_playlist(s1)
    Music.add_to_playlist(s2)
    Music.add_to_playlist(s3)
    Music.add_to_playlist(s4)
    Music.add_to_playlist(s5)




main()
