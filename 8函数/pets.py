def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print('\nI have a ' + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# describe_pet('hamster', 'harry')
# describe_pet('Dog', 'Big Yellow')
# describe_pet('harry', 'hamster')
#
# describe_pet(animal_type='Hamster', pet_name='Harry')
describe_pet('wang', 'hamster')
