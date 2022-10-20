alien_color = input("Please input alien's color:")

if alien_color == "green":
    point = 5
elif alien_color == "yellow":
    point = 10
elif alien_color == "red":
    point = 15

print("Alien color is " + alien_color + " ,you got " + str(point) + " points.")
