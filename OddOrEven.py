try:
    inp = eval(input().strip())
    if inp>0 and inp % 2 == 0:
        print('Even')
    else:
        print('Odd')
except:
    print('Invalid Number')
