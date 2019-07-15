import time
import random
import quicksort


def runningTime(results, method):
    instances = ['instances_level_1_100.txt', 'instances_level_1_1000.txt',
                 'instances_level_1_10000.txt', 'instances_level_2_100.txt',
                 'instances_level_2_1000.txt', 'instances_level_2_10000.txt',
                 'instances_level_3_100.txt', 'instances_level_3_1000.txt',
                 'instances_level_3_10000.txt']

    results = open(results, 'w+')

    for instance in instances:
        with open(instance, 'r') as file:
            mean = 0
            for line in file:
                vec = line.split(' ')
                start = time.time()
                quicksort.quicksort(vec, method)
                end = time.time()
                mean += (end - start)
            mean /= 10
            time_ms = mean * 1000

            results.write(instance + ' mean time: ' + str(time_ms) + '\n')


runningTime('results_method_4.txt', 4)

