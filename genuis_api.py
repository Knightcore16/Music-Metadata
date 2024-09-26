from lyricsgenius import Genius

genius = Genius("3JSEPRgsMwkZmuetLogJErAX0htagvbPrg4MtlRUVUUoULWihwTpV1SMpZVsEp-l")

def get_song_info(song_id, cover_art_id):

    song = genius.song(song_id)
    cover_art = genius.cover_arts(cover_art_id)

    print("Song details:")
    print(song['song']) 

    print("\nCover art details:")
    print(cover_art['cover_arts'][0]['image_url'])  

get_song_info(5601084, 713229)