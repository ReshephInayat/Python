marks: int = int(input("Enter Your Marks: "))

if marks >=101:
    print("Please verify your age")
    exit()

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >=60:
    print("Grade D")
else:
    print("Fail")
