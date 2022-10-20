responses = {}

poll_active = True

prompt_name = "What's your name?: "
prompt_place = "If you cloud visit one place in the world, where would you go?"
contiune_answer = "Do you want to answer other options?(Yes/ No)"

while poll_active:
    name = input(prompt_name)
    place = input(prompt_place)
    con_answer = input(contiune_answer)

    responses[name] = place

    if con_answer == 'no':
        poll_active = False

print("\n---Poll End---")

for name, place in responses.items():
    print(name.title() + 'Want to go to ' + place.title())
