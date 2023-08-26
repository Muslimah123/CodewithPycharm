def main():
    question = "What's your name?"
    sentence='Harriet Jacobs writes,"she sat down,quivering in every limb"'

    print(question)
    print(sentence)

    a_string = 'Little Red Riding-Hood comes to me one Christmas Eve to give me information of the cruelty and ' \
               'treachery of that dissembling Wolf who ate her grandmother. '

    print('Red' in a_string)
    books = ['Dracula', 'Frankenstein', 'The Omen', 'The Exorcist', 'The Legend of Sleepy Hollow']
    movies = ('A Christmas Carol', 'The Sea Beast', 'Enchanted', 'Pinocchio', 'The Addams Family')
    numbers = range(10)

    print('A Christmas Carol' not in books)
    print('Enchanted' in movies)
    print(5 in numbers)

    random_numbers = [6, 1, 3, 8, 0]

    print(len(random_numbers))
    print(min(random_numbers))
    print(max(random_numbers))

    paragraph = '''At three in the morning the chief Sussex detective, obeying the urgent call from Sergeant Wilson of 
       Birlstone, arrived from headquarters in a light dog-cart behind a breathless trotter. By the five-forty train in 
       the morning he had sent his message to Scotland Yard, and he was at the Birlstone station at twelve o'clock to 
       welcome us. White Mason was a quiet, comfortable-looking person in a loose tweed suit, with a clean-shaved, 
       ruddy face, a stoutish body, and powerful bandy legs adorned with gaiters, looking like a small farmer, 
       a retired gamekeeper, or anything upon earth except a very favourable specimen of the provincial criminal 
       officer.'''

    substring = 'morning'

    print(f'The substring "{substring}" shows up {paragraph.count(substring)} times in the paragraph.')

    string = 'Holmes was certainly not a difficult man to live with'

    word_list = string.split()

    print(word_list)


if __name__ == '__main__':
    main()
