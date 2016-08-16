from math import *

my_list = [(lambda x:(x*87+12)%100)(i) for i in range(20)]
print(my_list)
summ = 0
sum_sq = 0
num = 0

while len(my_list):
    cur_num = my_list.pop()

    if cur_num%2 == 0:
        num += 1
        print (num,end=" ")
        summ += cur_num
        sum_sq += cur_num**2
        D2 = sum_sq/num - (summ/num)**2
        print (D2, sqrt(D2))
print (sqrt(D2))


