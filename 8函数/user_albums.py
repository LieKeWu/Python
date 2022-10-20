def make_album(singer_name, album_name, song_number=None):
    info = {
        "singer_name": singer_name,
        "album_name": album_name,
    }
    if song_number:
        info["song_number"] = song_number
    return info


while True:
    print('prompt:在任何地方输入q 即可退出程序.')

    singer_name = input('\n请输入歌手的名字：')
    if singer_name == 'q':
        break
    album_name = input('请输入专辑的名字：')
    if album_name == 'q':
        break
    song_number = input('请输入专辑的歌曲数(没有则不填)：')
    if song_number == 'q':
        break

    if song_number:
        albums = make_album(singer_name, album_name, int(song_number))
    else:
        albums = make_album(singer_name, album_name)

    print(albums)

print('退出程序成功！')
