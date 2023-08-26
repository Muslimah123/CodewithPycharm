# so lemme try and explain the set and none type here with examples

# sets,just like list is a collection of unique element...

# Whereas lists are defined using brackets[],sets are defined using curly braces {}
# or by using the set constructor.. Sets are only used for storing distinct values ..

fruits = {'apple', 'banana', 'orange'}
print(fruits)

# Adding an element to the set
fruits.add('grape')
print(fruits)

#Removing an element from the set
fruits.remove('banana')
print(fruits)

#In python,None is a special constant often used to represent the absence of a value
# it's kinda similar to Null which also indicate that something is non existent

#you can set a variable with a none type;

def print_greeting(name):
    if name:
        print(f"Hello, {name}!")
        return f'greating for {name} printed'
    else:
        print("Hello, Guest!")

result = print_greeting("Alice")  # Output: Hello, Alice!
print(result)  # Output: None (because print_greeting doesn't return anything)
