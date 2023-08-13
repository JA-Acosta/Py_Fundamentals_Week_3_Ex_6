'''
>>> JAAR
>>> 08/13/2023
>>> Practicing Fundamentals Program 18
>>> Version 1
'''

'''
>>> Generates a program that prints a story to the console then asks the user if they would like to search through the story for all occurrences of a word and/or if they would like to replace a single word in the story for another.
'''
import re

def user_response()->str :
    '''
    >>> Asks the user to enter either yes or no. If the user inputs anything else, will prompt the user to enter a new response.

    >>> Returns: (str) response
    '''
    valid_response = ['yes', 'no']
    while True :
        response = input('').lower()
        if response in valid_response :
            return response
        else :
            print("Your response is invalid please enter either 'yes' or 'no': ", end = '')

def count_occurrence(words : list) :
    '''
    >>> Asks the user if they'd like to count the occurrence for any specific word. If the user response is yes, will prompt them to enter a word that is in the list of words in the story. Otherwise, will do nothing.
    '''
    print('\nDo you want to count each occurrence of a word in the story?: ', end = '')
    response = user_response()
    word = ''
    while response == 'yes' and word not in words :
        word = input('Enter a word to count: ')
    if response == 'yes' :
        print(f'{word} occurs {words.count(word)} times in the story.')

def replace_input(words : set) :
    '''
    >>> 
    '''
    word = ''
    print('\nDo you want to replace a word in the story with a new word?: ', end = '')
    response = user_response()
    while response == 'yes' and word not in words :
        word = input('Enter a word to replace: ')
    if word :
        replacement_word = input('Enter the replacement word: ')
        lines = ''
        with open('the_little_prince.txt', 'r+') as story :
            lines = story.readlines()
            story.seek(0)
            for line in lines :
                story.write(line.replace(word.lower(), replacement_word))

def main() :
    words = []
    with open('the_little_prince.txt', 'r') as story :
        lines = story.readlines()
    for line in lines :
        print(line.rstrip('\n'))
        words.extend(re.findall(r"\b[a-zA-Z]+[-']?[a-zA-Z]*\b", line.lower()))
    print('\n-----------------------------------------------------------------------')
    count_occurrence(words)
    print('\n-----------------------------------------------------------------------')
    replace_input(set(words))

if __name__ == '__main__' :
    main()