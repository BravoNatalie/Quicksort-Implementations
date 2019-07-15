# Implementação do Quicksort com as seguintes estratégias de escolha do pivô:
#   1. mediana (O(n log n));
#   2. valor aleatório através de distribuição uniforme (O(n log n));
#   3. média de valores: (primeiro elemento + elemento central + último elemento)/3;
#   4. dada na sala.

import random

global maximum


def _lis(arr, n):
    global maximum

    if n == 1:
        return 1

    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1

    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1

    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum, maxEndingHere)

    return maxEndingHere


# longest increasing subsequence
def lis(arr):
    # to allow the access of global variable
    global maximum

    n = len(arr)
    maximum = 1
    _lis(arr, n)

    return maximum


def randomnessLevel(arr):
    d = 1 - (float(lis(arr)) / len(arr))

    if d < 0.3:
        return 1
    elif d <= 0.7:
        return 2
    else:
        return 3


# gera instâncias
def instancesGenerator(arr_size, num_instances):
    total_instances = 0
    n_1 = 0  # número de instâncias do tipo 1
    n_2 = 0  # número de instâncias do tipo 2
    n_3 = 0  # número de instâncias do tipo 3

    file_1 = open('level_1.txt', 'w+')
    file_2 = open('level_2.txt', 'w+')
    file_3 = open('level_3.txt', 'w+')

    while total_instances < 3 * num_instances:
        arr = random.sample(range(arr_size), arr_size)
        d = randomnessLevel(arr)

        if d == 1 and n_1 < num_instances:
            n_1 = n_1 + 1
            print('Level 1 - instance number = ', n_1)
            total_instances = total_instances + 1
            for number in arr:
                file_1.write(str(number) + ' ')
            file_1.write('\n')

        elif d == 2 and n_2 < num_instances:
            n_2 = n_2 + 1
            print('Level 2 - instance number = ', n_2)
            total_instances = total_instances + 1
            for number in arr:
                file_2.write(str(number) + ' ')
            file_2.write('\n')

        elif d == 3 and n_3 < num_instances:
            n_3 = n_3 + 1
            print('Level 3 - instance number = ', n_3)
            total_instances = total_instances + 1
            for number in arr:
                file_3.write(str(number) + ' ')
            file_3.write('\n')

    file_1.close()
    file_2.close()
    file_3.close()


def txtToArray(file):
    array = list()

    with open(file, 'r') as reader:
        line = reader.readline().rstrip('\n').split()
        while len(line) != 0:
            array.append(line)
            line = reader.readline().rstrip('\n').split()

    return array


def teste():
    instancesGenerator(10, 4)

    file_1 = txtToArray('level_1.txt')
    file_2 = txtToArray('level_2.txt')
    file_3 = txtToArray('level_3.txt')

    print(">>> Executing quicksort in file 1: ")

#     for i in range(1, 5):
#       print('Method ' + str(i) + ':')
#       teste = file_1
    i = 1
    for array in file_1:
        print('------Unordered:')
        print(array)
        quicksort(array, method=i)
        print('------Method ' + str(i) + ' Ordered:')
        print(array)
        print('\n')
        i = i+1


# def findPivot(lista, n1, n2): # algoritmo usado para a 4ª estratégia, está errado e tem q arruamar
#     pos = n1 + 1
#     if(pos > n2):
#         return 0
#     if(lista[pos] >= lista[pos-1]):
#         pos = pos + 1
#     return pos


def mediana(array, begin, end):
    mid = (begin+end-1)//2
    a = array[begin]
    b = array[mid]
    c = array[end-1]

    if (a <= b <= c):
        return mid
    if (c <= b <= a):
        return mid
    if (a <= c <= b):
        return end-1
    if (b <= c <= a):
        return end-1

    return begin


def pivotChoosing(array, begin, end, method):
    try:
        if (method == 1):
            p = mediana(array, begin, end)
        elif (method == 2):
            p = random.randint(begin, end)
        elif (method == 3):
            p = (begin + len(array)//2 + end)//3
        elif (method == 4):
            # não entendi qual era a sugestão do professor e fiz isso por enquanto
            p = (begin + (end - begin))//2
        else:
            raise StopIteration
    except StopIteration:
        print("Método não existe!")

    array[p], array[end] = array[end], array[p]

    return array[end]


def partition(array, begin, end, method):
    pivot = pivotChoosing(array, begin, end, method)
    i = (begin - 1)

    for j in range(begin, end):
        if (array[j] <= pivot):
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1]

    return (i+1)


def quicksort(array, begin=0, end=None, method=4):
    if (end is None):
        end = len(array)-1
    if (begin < end):
        p = partition(array, begin, end, method)
        quicksort(array, begin, p-1, method)
        quicksort(array, p+1, end, method)
    else:
        return


def main():
    teste()


if __name__ == "__main__":
    main()
