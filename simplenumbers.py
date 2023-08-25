def main():
    num_1=15
    num_2=12

    print(f'the sum of {num_1} and {num_2} is : {num_1 + num_2}')
    print(f'the difference of {num_1} and {num_2} is : {num_1 - num_2}')
    print(f'product of {num_1} and {num_2} is: {num_1 * num_2}')
    print(f'quotient of {num_1} and {num_2} is: {int(num_1 / num_2)}')
    print(f'floored quotient of {num_1} and {num_2} is: {num_1 // num_2}')
    print(f'divison and modulus of {num_1} and {num_2} is : {divmod(num_1,num_2)}')


    x=2
    y=3
    print(f'{x} to the power {y} is {pow(x,y)}')

if __name__ == '__main__':
    main()

