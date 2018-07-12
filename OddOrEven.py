try:
    inp = eval(input().strip())
    if inp > 0 :
        if inp % 2 == 0:
            print('Even')
        else:
            print('Odd')
    else:
        print('Invalid')
except:
    print('Invalid')
