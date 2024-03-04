password: str = input("Enter Your Password: ")
pass_length = len(password)
if pass_length < 6:
    strength = "Weak"
elif pass_length < 10:
    strength = "Medium"
else:
    strength = "Strong"
print(f"Your Password Strength is {strength}")
