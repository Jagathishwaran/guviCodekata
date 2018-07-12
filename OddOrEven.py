try:
    inp = eval(input().strip())
    if inp % 2 == 0:
        print('Even')
    else:
        print('Odd')
except:
    print('Invalid Number')
