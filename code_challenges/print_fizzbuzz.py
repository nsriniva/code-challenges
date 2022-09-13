
pdict = {1:'fizz',10:'buzz',11:'fizzbuzz'}

for n in range(1,100):
    mult = 0
    if n%3 == 0:
        mult = 1
    if n%5 == 0:
        mult += 10

    if mult != 0:
        print(f'{pdict[mult]}')
    else:
        print(n)

