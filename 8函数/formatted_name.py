def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name.title() + " " + middle_name + " " + last_name.title()
    else:
        full_name = first_name.title() + " " + last_name.title()
    return full_name.title()


musician = get_formatted_name("john", "lee", 'hooker')
print(musician)
musician = get_formatted_name("jimi", 'hendrix')
print(musician)
