inp = input()
vowels = 'aeiouAEIOU'
if len(inp) == 1 and inp.isalpha():
    if inp in vowels:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')
