from collections import OrderedDict

my_glossary = OrderedDict()

my_glossary['mars'] = '火星'
my_glossary['earth'] = '地球'
my_glossary['sun'] = '太阳'
my_glossary['moon'] = '月球'

for key, value in my_glossary.items():
    print(key + '的中文含义是:' + value + '.')
