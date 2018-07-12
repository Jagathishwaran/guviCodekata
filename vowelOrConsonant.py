inp = input()
vowels = 'aeiouAEIOU'
if len(inp) == 1 and inp.isalpha():
    if inp in vowels:
        print('vowel')
    else:
        print('consonant')
else:
    print('Invalid')
