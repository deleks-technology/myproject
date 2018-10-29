print("Welcome to our simple Calculator... ")
print("====================================================================")

# Prompt User for first number
# to convert a string to a number with use the int()/ float()
first_number = float(input("Please input your first number: "))
print("====================================================================")

# Prompt User for second number
second_number = float(input("Please input your second number: "))
print("====================================================================")

# Math Logic

# Logic for Addition
print(" The Sum of ", first_number, "and", second_number, "=", (first_number + second_number))
print("====================================================================")

# Logic for substraCTION
print(" The Substraction of ", first_number, "and", second_number, "=", (first_number - second_number))
print("====================================================================")

# Logic for division
print(" The division of ", first_number, "and", second_number, "=", round(first_number / second_number, 2))
print("====================================================================")

# Logic for multiplication
print(" The multiple of ", first_number, "and", second_number, "=", (first_number * second_number))
print("====================================================================")

# Logic for raise to power 2
print("The square of", first_number, "=", (first_number ** 2))
