age_input: int = int(input("Enter You age "))
day_of_week: str = str(
    input(
        "What day of  the week is it? "
    ).capitalize()
)
price: int = 12 if age_input >= 18 else 8
if day_of_week == "Wednesday":
    price -= 2
else:
    price = price
    print("Your Ticket if For $",price)
