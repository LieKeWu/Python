# def make_shirt(shirt_size, shirt_word):
#     """T恤的尺码和字样"""
#     print('I Want a ' + shirt_size + ' shirt.')
#     print('Shirt have are words:' + shirt_word + ".")
#
#
# make_shirt('L', "I Love U")

"""
修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他
字样的T恤（尺码无关紧要）。”
"""


def make_shirt(shirt_size='L', shirt_word='I love Python'):
    """T恤的尺码和字样"""
    print('I Want a ' + shirt_size + ' shirt.')
    print('Shirt have are words:' + shirt_word + ".")


make_shirt()
make_shirt(shirt_word='I Love Jiying')
