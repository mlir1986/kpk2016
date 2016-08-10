from random import shuffle
A = list(range(int(input('размер массива'))))
shuffle(A)
print (*A)
n = 0
while A != sorted(A):
    shuffle(A)
    n += 1
print (*A)
print (n)