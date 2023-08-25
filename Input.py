def main():
    name=input("what's your name?")
    age=int(input(f'How old are you {name}'))
    current_age=int(input("what year is this again"))
    print(f'Nice to meet you {name}')
    print(f'if my calculations are right,you were born in {current_age-age}')


if __name__ == '__main__':
    main()