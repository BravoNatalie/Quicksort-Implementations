# Implementação do Quicksort com as seguintes estratégias de escolha do pivô:
#   1. mediana (O(n log n));
#   2. valor aleatório através de distribuição uniforme (O(n log n));
#   3. média de valores: (primeiro elemento + elemento central + último elemento)/3;
#   4. dada na sala.

import random

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
        return b, mid
    if (c <= b <= a):
        return b, mid
    if (a <= c <= b):
        return c, end-1
    if (b <= c <= a):
        return c, end-1

    return a, begin


def pivotChoosing(array, begin, end, method=1):
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


def partition(array, begin, end):
    pivot = pivotChoosing(array, begin, end, method=4)
    i = (begin - 1)

    for j in range(begin, end):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1]

    return (i+1)


def quicksort(array, begin=0, end=None):
    if (end is None):
        end = len(array)-1
    if (begin < end):
        pivot = partition(array, begin, end)
        quicksort(array, begin, pivot-1)
        quicksort(array, pivot+1, end)
    else:
        return
