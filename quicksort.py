# Implementação do Quicksort com as seguintes estratégias de escolha do pivô:
#   1. mediana (O(n log n));
#   2. valor aleatório através de distribuição uniforme (O(n log n));
#   3. média de valores: (primeiro elemento + elemento central + último elemento)/3;
#   4. dada na sala.


def findPivot(lista, n1, n2): # algoritmo usado para a 4ª estratégia, está errado e tem q arruamar
    pos = n1 + 1
    if(pos > n2):
        return 0
    if(lista[pos] >= lista[pos-1]):
        pos = pos + 1
    return pos 


def partition(array, begin, end):  
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=len(array)-1):
    if(begin < end):
        pivot = partition(array, begin, end)
        quicksort(array, begin, pivot-1)
        quicksort(array, pivot+1, end)
    else:
        return 