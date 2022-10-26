def city_country(city, country, popluation=''):
    """显示城市对应的国家"""
    city_country = city + ', ' + country + " - population=" + str(popluation)
    return city_country.title()
