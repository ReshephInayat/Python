age : int = int(input("Enter Your age: "))
if age < 13:
    print("Children")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
