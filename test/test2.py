# количество чисел, кратных 7, в последовательности, генерируемой лямбда-функцией
def generate_number():
     return lambda x: (x*693 + 5)%100
number = generate_number
n = 0
i = 1
while number()(i):
    if number()(i)%7 == 0:
        n += 1
        print( i, 'это', number()(i))
    i += 1
print (n)



# сумма чисел, кратных 7, в последовательности, генерируемой лямбда-функцией
def generate_number():
     return lambda x: (x*693 + 5)%100
number = generate_number
s = 0
i = 1
while number()(i):
    if number()(i)%7 == 0:
        s += number()(i)
        print( i, 'это', number()(i), end=',')
        print( "сумма равна", s)
    i += 1
print (s)

# среднее арифметическое чисел, кратных 4, в последовательности, генерируемой лямбда-функцией
def generate_number():
     return lambda x: (x*693 + 5)%100
number = generate_number
s = 0
i = 1
f = 0
while number()(i):
    if number()(i)%4 == 0:
        s += number()(i)
        f += 1
        print( i, 'это', number()(i))
    i += 1
print (s/f)

# минимальное из чисел, кратных 3, в последовательности, генерируемой лямбда-функцией
def generate_number():
     return lambda x: (x*693 + 5)%100
number = generate_number

n_min = 100
i = 1
while number()(i):
    if number()(i)%3 == 0:
        n_min = min(n_min, number()(i))
        print( i, 'это', number()(i))
    i += 1
print (n_min)