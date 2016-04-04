# Virkar i python 2 en ekki 3

import random
import time


def merge_sort(array):
    if len(array) <= 1: return array

    left = []
    right = []

    for idx, val in enumerate(array):
        if idx % 2 == 0:
            left.append(array[idx])
        else:
            right.append(array[idx])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    while left:
        result.append(left[0])
        left.pop(0)
    while right:
        result.append(right[0])
        right.pop(0)

    return result

run_time = []

for x in range(0, 50):
    array = list(range(10000))
    random.shuffle(array)

    start = time.time()
    sorted_arr = merge_sort(array)
    end = time.time()

    run_time.append(end - start)
    print(end - start)

print("average: ", sum(run_time) / float(len(run_time)))
