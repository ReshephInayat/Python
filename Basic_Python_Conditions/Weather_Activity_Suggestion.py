weather_list: list[str] = ["1.Sunny", "2.Rainy","3.Snowy"]
for list in weather_list:
    print(list)
weather: str = input("What's the Weather outside: ").capitalize()
if weather == "Sunny":
    print("Go for a walk")
elif weather == "Rainy":
    print("Read a Book")
elif weather == "Snowy":
    print("Build a Snowman")
else:
    print("Please select the weather from the list above!")
