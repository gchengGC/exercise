total_album = {}
def make_album(Singer, Album, Musics = None):
    Albums = {'Singer': Singer, 'Album': Album}
    if Musics:
        Albums['Musics'] = Musics
    total_album[Singer] = Albums
    return  Albums

while True:
    print("\nPlease input Singer、Albums、Music:")
    print("\nInput 'q' to stop")
    singer = input('\nInput Singer: ')
    if singer == 'q':
        break
    album = input('Input Album: ')
    if album == 'q':
        break
    musics = input('Input Musics: ')
    if musics == 'q':
        break
    albums = make_album(singer, album, musics)
    print(f"\nThe albums is {albums}")

for singer, album in total_album.items():
    print(f"\nThe {singer}'s album is {album}")