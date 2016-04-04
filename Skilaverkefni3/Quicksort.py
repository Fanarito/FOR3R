import random
import time


def quick_sort(array):
    less, pivotlist, more = [], [], []

    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotlist.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotlist + more


run_time = []

for x in range(0, 50):
    array = list(range(10000))
    random.shuffle(array)

    start = time.time()
    sorted_arr = quick_sort(array)
    end = time.time()

    run_time.append(end - start)
    print(end - start)

print("average: ", sum(run_time) / float(len(run_time)))
