you_are_boy = True
you_are_gamer = False

if you_are_boy and you_are_gamer:
    print("You are a gamer boy")
elif you_are_boy and not(you_are_gamer):
    print("You are not a gamer boy")
elif not(you_are_boy) and not(you_are_gamer):
    print("You are gamer a gamer girl")
elif not(you_are_boy) and you_are_gamer:
    print("You are not a gamer girl")
