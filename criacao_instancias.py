import random


# level_1 -> apenas alguns elementos fora de lugar
# level_2 -> muitos elementos fora do lugar (utiliza o LIS)
# level_3 -> todos elementos fora do lugar

# Longest increasing subsequence
def LIS(a):
    L = []
    for (k, v) in enumerate(a):
        L.append(max([L[i] for (i, n) in enumerate(a[:k]) if n < v] or [[]], key=len) + [v])
    return max(L, key=len)


# Randomness Level
def RL(a):
    d = 1 - (float(len(LIS(a))) / len(a))

    if d < 0.3:
        return 1
    elif d <= 0.7:
        return 2
    else:
        return 3


def instance(arr_size):

    #instancias do tipo 1 foram ordenadas e então tiveram alguns elementos trocados
    file_1 = open('instances_level_1_' + str(arr_size) + '.txt', 'w+')

    for i in range(10):
        arr_1 = list(range(arr_size))
        indexes = random.sample(range(arr_size - 1), 4)

        # troca de elementos
        aux = arr_1[indexes[0]]
        arr_1[indexes[0]] = arr_1[indexes[1]]
        arr_1[indexes[1]] = aux

        aux = arr_1[indexes[2]]
        arr_1[indexes[2]] = arr_1[indexes[3]]
        arr_1[indexes[3]] = aux

        for number in arr_1:
            file_1.write(str(number) + ' ')
        file_1.write('\n')

    file_1.close()


    # instancias do tipo 2 têm muitos elementos fora de ordem
    file_2 = open('instances_level_2_' + str(arr_size) + '.txt', 'w+')

    n_i = 0

    while n_i < 10:
        arr_2 = random.sample(range(arr_size), arr_size)

        if RL(arr_2) == 3:
            n_i = n_i + 1
            for number in arr_2:
                file_2.write(str(number) + ' ')
            file_2.write('\n')

    file_2.close()

    #instancias do tipo 1 foram ordenadas de forma decrescente e então tiveram alguns elementos trocados
    file_3 = open('instances_level_3_' + str(arr_size) + '.txt', 'w+')

    for i in range(10):
        arr_3 = sorted(list(range(arr_size)), reverse=True)
        indexes = random.sample(range(arr_size - 1), 4)

        # troca de elementos
        aux = arr_3[indexes[0]]
        arr_3[indexes[0]] = arr_3[indexes[1]]
        arr_3[indexes[1]] = aux

        aux = arr_3[indexes[2]]
        arr_3[indexes[2]] = arr_3[indexes[3]]
        arr_3[indexes[3]] = aux

        for number in arr_3:
            file_3.write(str(number) + ' ')
        file_3.write('\n')

    file_3.close()

