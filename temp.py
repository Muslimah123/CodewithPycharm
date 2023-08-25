def main():
    temperature_in_celsius=float(input("what's the temperature in degree celsius?  "))
    temperature_fahrenheit=( temperature_in_celsius *1.8 ) +32
    print(f'the temperature in degree celsius {temperature_in_celsius} is equivalent to {temperature_fahrenheit} in degree fahrenheit')

if __name__ == '__main__':
    main()