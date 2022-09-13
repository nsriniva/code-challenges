NotDivBy3Or5 = 0
DivBy3 = 1
DivBy5 = 10
DivBy3And5 = 11

pdict = {DivBy3: "fizz", DivBy5: "buzz", DivBy3And5: "fizzbuzz"}

for n in range(1, 101):

    divBy = NotDivBy3Or5

    if n % 3 == 0:
        divBy = DivBy3
    if n % 5 == 0:
        divBy += DivBy5

    if divBy != NotDivBy3Or5:
        print(f"{pdict[divBy]}")
    else:
        print(n)
