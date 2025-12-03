import random
import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def measure_time(sort_function, data):
    data_copy = data.copy()
    start_time = timeit.default_timer()
    sort_function(data_copy)
    return timeit.default_timer() - start_time


if __name__ == "__main__":
    data_sizes = [100, 1000, 5000, 10000]

    print(f"{'Algorithm':<20} | {'Size':<10} | {'Time (sec)':<15}")
    print("-" * 50)

    for size in data_sizes:
        data = [random.randint(0, 100_000) for _ in range(size)]

        t_insert = measure_time(insertion_sort, data)
        print(f"{'Insertion Sort':<20} | {size:<10} | {t_insert:.6f}")

        t_merge = measure_time(merge_sort, data)
        print(f"{'Merge Sort':<20} | {size:<10} | {t_merge:.6f}")

        t_timsort = measure_time(sorted, data)
        print(f"{'Timsort (Built-in)':<20} | {size:<10} | {t_timsort:.6f}")

        print("-" * 50)
