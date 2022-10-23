filenames = ['file_text/dogs.txt', 'cats.txt']

for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # 一言不发
        # pass
        # 友好消息
        print("\nFile not found error: " + filename)
    else:
        print("\nReading file:" + filename)
        print(contents)
