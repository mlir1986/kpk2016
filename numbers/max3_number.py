x = int(input())
m1 = m2 = m3 = -100000
m1_n = m2_n = m3_n = 0
while x != 0:
    if x > m1:
        m1, m2, m3 = x, m1, m2
        m1_n, m2_n, m3_n = 1, m1_n, m2_n
    elif x == m1:
        m1_n +=  1
    elif x > m2:
        m2, m3 = x, m2
        m2_n, m3_n = 1, m2_n
    elif x == m2:
        m2_n += 1
    elif x > m3:
        m3 = x
        m3_n = 1
    elif x == m3:
        m3_n += 1
    #считывание х для последующей итерации
    x = int(input())
print (m1, m2, m3)
print (m1_n, m2_n, m3_n)