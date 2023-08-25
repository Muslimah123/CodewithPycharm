 # often used to make decisions and comparision
is_raining = True
is_sunny = False

age = 25
is_adult = age >= 18  # This will be True because 25 is greater than or equal to 18

has_apple = True
has_orange = False

# Using logical AND operator
both_fruits = has_apple and has_orange  # This will be False

# Using logical OR operator
either_fruit = has_apple or has_orange  # This will be True

# Using logical NOT operator
no_apple = not has_apple  # This will be False

temperature = 28

if temperature > 30:
    print("It's a hot day!")
else:
    print("It's a pleasant day.")

name = "Alice"
is_long_name = len(name) > 5  # This will be True if name's length is greater than 5
