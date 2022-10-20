def make_album(singer_name, album_name, song_number=None):
    info = {
        "singer_name": singer_name,
        "album_name": album_name,
    }
    if song_number:
        info["song_number"] = song_number
    return info


albums = make_album('Jay Chou', '夜曲', 9)
print(albums)

albums = make_album('王力宏', '你不知道的事')
print(albums)

albums = make_album('邓丽君', 'つぐない', 8)
print(albums)
