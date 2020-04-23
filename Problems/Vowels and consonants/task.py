vowels = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
             'p', 'q', 'r', 's', 's', 't', 'v', 'w', 'x', 'y', 'z']

word = input()
for n in word:
    if n in vowels:
        print('vowel')
    elif n in consonant:
        print('consonant')
    else:
        break
