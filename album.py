def make_album(artistname, albumtitle):
    artistname=input("Enter the name of the artist: ")
    albumtitle=input("Enter the title of the album: ")
    album={'artist': artistname, 'title': albumtitle}
    print(album)

n=0
while n<3:
    make_album(None, None)
