def check(my_sort):
    import random

    A = [1, 3, 2, 5, 4, 0]
    A_ans = [0, 1, 2, 3, 4, 5]
    my_sort (A)
    print ( 'test case #1: ' + ('OK' if A == A_ans else 'Fail'))

    A = [random.randint(1, 100) for i in range (1000)]
    A_ans = sorted(A)
    my_sort (A)
    print ( 'test case #2(main): ' + ('OK' if A == A_ans else 'Fail'))

    A = [-5, -2, -3, -1, 0, 4, 1,6]
    A_ans = [-5, -3, -2, -1, 0, 1, 4, 6]
    my_sort (A)
    print ( 'test case #3: ' + ('OK' if A == A_ans else 'Fail'))

    A = [[5], [2], [3], [5], [4], [1]]
    A_ans = sorted(A)
    my_sort (A)
    print ( 'test case #4: ' + ('OK' if A == A_ans else 'Fail'))

def do_nothing (A):
        pass

def bubble_sort(A):
    N = len (A)
    for prohod in range (1, N):
        for i in range (N-prohod):
            if A[i] > A[i+1]:
                tmp = A[i]
                A[i] = A[i+1]
                A[i+1] = tmp

def choice_sort(A):
    N = len (A)
    for pos in range (0, N-1):
        for i in range (pos+1, N):
            if A[i] < A[pos]:
                A[pos], A[i] = A[i], A[pos]

def insert_sort(A):
    N = len(A)
    for pos in range(1,N):
        # уверен, что список отсортирован с 0 по pos-1 позиции включительно
        i = 0
        while A[i] < A[pos]:
            i += 1
        # уверен, что и указывает на элемент не меньше вставляемого
        tmp = A[pos]
        for k in range (pos-1, i-1, -1):
            A[k+1] = A[k]
        A[i] = tmp

if __name__ == '__main__':
    print ('Test Пузырьковая сортировка')
    check(bubble_sort)
    print ('Test Сортировка выбором')
    check(choice_sort)
    print ('Test Сортировка вставками')
    check(insert_sort)