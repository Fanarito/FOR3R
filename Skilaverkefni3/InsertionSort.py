import random
import time


def insertion_sort(array):
    for x in range(1, len(array)):
        j = x
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1
    return array

run_time = []

for x in range(0, 50):
    array = list(range(10))
    random.shuffle(array)

    start = time.time()
    sorted_arr = insertion_sort(array)
    end = time.time()

    run_time.append(end - start)
    print(end - start)

print("average: ", sum(run_time) / float(len(run_time)))
