fruit: str = input("Enter Fruit Name: ").capitalize()
color: str = input("What's Your Fruit Color: ").capitalize()
if color == "Green":
    print(f"Your {fruit} is Unripe")
elif color == "Yellow" or "Red" or "Orange" :
    print(f"Your {fruit} is Ripe")
elif color == "Brow":
    print(f"Your {fruit} is Overripe")
else:
    print("I dont have information about these colors!`")

