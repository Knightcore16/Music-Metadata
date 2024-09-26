import eyed3

audiofile = eyed3.load("song.mp3")

def add_metadata():
    audiofile.tag.artist = ""
    audiofile.tag.album = ""
    audiofile.tag.album_artist = ""
    audiofile.tag.title = ""
    audiofile.tag.track_num = 0
    audiofile.tag.genre = ""
    audiofile.tag.year = 2000

    audiofile.tag.save()