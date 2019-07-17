# DCC001 - Análise de Projeto de Algoritmos
# Universidade Federal de Juiz de Fora (UFJF) - MG
#
# Tema do trabalho: 
#   Análise de escolhas diferentes de pivô para o algoritmo de ordenação QuickSort.
#
#Integrantes do grupo:
#   1. Ludmila Ribeiro Bôscaro Yung
#   2. Luís Henrique Simplício Ribeiro
#   3. Natalie Bravo
#
#Implementação do Quicksort com as seguintes estratégias de escolha do pivô:
#   1. mediana de três;
#   2. valor aleatório através de distribuição uniforme;
#   3. média;
#   4. dada na sala.

import random
import matplotlib.pyplot as plt
import results
import criacao_instancias
    
def pivot_aula(array, begin, end):
    begin = begin + 1
    r = end
    while(True):
        if  begin > end:
            break
        if array[begin] >= array[begin -1]:
            begin = begin +1
        else:
            r = begin
            break
    
    return r

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
            p = (begin + end)//2
        elif (method == 4):
            p = pivot_aula(array, begin, end)
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

timeRandom = []
timeMediana = []
timeMedia = []
timeSala = []
lenght = []
lenghtBigger = []
elements = [1000, 2000, 3000, 4000, 5000, 7000]
elementsBigger = [50000, 100000, 200000, 400000, 800000, 1000000]

def graficosAnalise(xl = "Qnt. Elements(und)", yl = "Time(sec)"):
	
    plt.subplot(211)
    plt.title('Análise de escolhas de pivô para o Quicksort', fontsize=20)
    plt.plot(lenght, timeRandom, label = "Quicksort - Random")
    plt.plot(lenght, timeMediana, label = "Quicksort - Mediana")
    plt.plot(lenght, timeMedia, label = "Quicksort - Média")
    plt.plot(lenght, timeSala, label = "Quicksort - Estratégia feita em sala de aula")
    legend = plt.legend(loc='upper left', shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
    legend = plt.legend(loc='upper left', shadow=True)
    frame = legend.get_frame()
    frame.set_facecolor('0.90')
	
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.show()


def main():
    #graficosAnalise()

    # criacao_instancias.instance(100)
    # criacao_instancias.instance(1000)
    # criacao_instancias.instance(10000)
    # results.runningTime('results_method_1.txt', 1)

    # criacao_instancias.instance(100)
    # criacao_instancias.instance(1000)
    # criacao_instancias.instance(10000)
    # results.runningTime('results_method_2.txt', 2)

    # criacao_instancias.instance(100)
    # criacao_instancias.instance(1000)
    # criacao_instancias.instance(10000)
    # results.runningTime('results_method_3.txt', 3)

    # criacao_instancias.instance(100)
    # criacao_instancias.instance(1000)
    # criacao_instancias.instance(10000)
    # results.runningTime('results_method_4.txt', 4)


if __name__ == "__main__":
    main()
