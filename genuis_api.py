from lyricsgenius import Genius

genius = Genius("3JSEPRgsMwkZmuetLogJErAX0htagvbPrg4MtlRUVUUoULWihwTpV1SMpZVsEp-l")

def get_song_info(song_id, cover_art_id):

    song = genius.song(song_id)
    cover_art = genius.cover_arts(cover_art_id)

    print("Song details:")
    print(song['song']) 

    print("\nCover art details:")
    print(cover_art)  

get_song_info(6428196, 598308)