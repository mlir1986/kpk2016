from random import *
A = [randint(0, 100) ** 3 % 1000 for i in range(10 ** 6 + 1)]
print(len(A))

A0 = []
A1 = []
A2 = []
A3 = []
A4 = []
A5 = []
A6 = []
A7 = []
A8 = []
A9 = []
for num in A:
    if num%10 == 0: A0.append(num)
    elif num%10 == 1: A1.append(num)
    elif num%10 == 2: A2.append(num)
    elif num%10 == 3: A3.append(num)
    elif num%10 == 4: A4.append(num)
    elif num%10 == 5: A5.append(num)
    elif num%10 == 6: A6.append(num)
    elif num%10 == 7: A7.append(num)
    elif num%10 == 8: A8.append(num)
    else: A9.append(num)
A = A0+A1+A2+A3+A4+A5+A6+A7+A8+A9
B0 = []
B1 = []
B2 = []
B3 = []
B4 = []
B5 = []
B6 = []
B7 = []
B8 = []
B9 = []
for num in A:
    if (num//10)%10 == 0: B0.append(num)
    elif (num//10)%10 == 1: B1.append(num)
    elif (num//10)%10 == 2: B2.append(num)
    elif (num//10)%10 == 3: B3.append(num)
    elif (num//10)%10 == 4: B4.append(num)
    elif (num//10)%10 == 5: B5.append(num)
    elif (num//10)%10 == 6: B6.append(num)
    elif (num//10)%10 == 7: B7.append(num)
    elif (num//10)%10 == 8: B8.append(num)
    else: B9.append(num)
A = B0+B1+B2+B3+B4+B5+B6+B7+B8+B9
C0 = []
C1 = []
C2 = []
C3 = []
C4 = []
C5 = []
C6 = []
C7 = []
C8 = []
C9 = []
for num in A:
    if (num//100) == 0: C0.append(num)
    elif (num//100) == 1: C1.append(num)
    elif (num//100) == 2: C2.append(num)
    elif (num//100) == 3: C3.append(num)
    elif (num//100) == 4: C4.append(num)
    elif (num//100) == 5: C5.append(num)
    elif (num//100) == 6: C6.append(num)
    elif (num//100) == 7: C7.append(num)
    elif (num//100) == 8: C8.append(num)
    else: C9.append(num)
C = C0+C1+C2+C3+C4+C5+C6+C7+C8+C9

print(C[len(A)//2])