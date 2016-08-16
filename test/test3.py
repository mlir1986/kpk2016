#количество элементов, равных минимальному значению списка my_list с помощью len(my_list) и my_list.pop
my_list = [(lambda x:(x*87+12)%16)(i) for i in range(20)]
print(my_list)
min_value = my_list.pop()
min_number = 1
while len(my_list) > 0:
    num = my_list.pop()
    if num < min_value:
        min_value = num
        min_number = 1
    elif num == min_value:
        min_number += 1
print(min_number)

#количество вторых минимумов списка my_list с помощью len(my_list) и my_list.pop
my_list = [(lambda x:(x*296+2410)%4096)(i) for i in range(2000)]
min1 = my_list.pop()
min2 = my_list.pop()
min1_num = 1
min2_num = 1
while len(my_list):
    cur_num = my_list.pop()
    print (cur_num, end=' ')
    if cur_num < min1:
        min1, min2 = cur_num, min1
        min1_num, min2_num = 1, min1_num
    elif cur_num == min1:
        min1_num += 1
    elif cur_num < min2:
        min2 = cur_num
        min2_num = 1
    elif cur_num == min2:
        min2_num += 1
print('')
print (min1, min1_num, min2, min2_num)