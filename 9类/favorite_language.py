from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['Ken'] = 'Python'
favorite_languages['Xuchuan'] = 'Java'
favorite_languages['Vivi'] = 'Scratch'
favorite_languages['Lu'] = 'C++'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
