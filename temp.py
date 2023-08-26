def main():
    #temperature_in_celsius=float(input("what's the temperature in degree celsius?  "))
    #temperature_fahrenheit=( temperature_in_celsius *1.8 ) +32
    #print(f'the temperature in degree celsius {temperature_in_celsius} is equivalent to {temperature_fahrenheit} in degree fahrenheit')

    horror_books=['Dracula','Carmilla','The Imago Sequence']
    print(horror_books)

    horror_books.append('The exorcist')
    print(horror_books)

    print(horror_books.pop())
    print(horror_books)

    print(range(10))
    print(list(range(10)))

    print(list(range(1,10,2)))

    random_numbers = [6, 1, 3, 8, 0, 9, 12, 3, 4, 0, 54, 8, 100, 55, 60, 70, 85]
    multiplied_list=[]
    print(dir(random_numbers))

    for number in random_numbers:
        multiplied_list.append(number * 2)
    print(multiplied_list)

    number=1
    tu_list=[]
    while number < 11:
        tu_list.append(number)

        number +=1
    print(tu_list)


    for x in range(1,6):
        print()
        for y in range(1,11):
            print(f'{x} * {y}  = {x * y }')


    x=1
    while x <6:
        y=1
        while y <11:
            print(f'{x} * {y}  = {x * y}')

            y +=1
        print()
        x += 1
        print()



if __name__ == '__main__':
    main()