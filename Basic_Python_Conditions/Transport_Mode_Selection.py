distance: int = int(input("Enter Distance: "))
if distance < 3:
    transport = "Go By Walking"
elif distance < 15:
    transport = "Use A Bike"
else:
    transport = "Use A Car"
print(f"Your Distance is {distance} Km I Suggest That You Should {transport}")
