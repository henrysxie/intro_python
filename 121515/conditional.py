

















first_name = input("What's your first name")
name_length = len(first_name)
if name_length > 10:
    print("That's a long name!")
elif name_length > 3:
    print("Nice, that's a name of medium length.")
elif name_length == 3:
    print("That's a short name.")
else:
    print("Are you sure those aren't your initials?")
