import random
import time
from copy import deepcopy

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_dix = i
        for j in range(i + 1, n):
            if arr[min_dix] > arr[j]:
                min_dix = j
        arr[i], arr[min_dix] = arr[min_dix], arr[i]
    return arr


def insertion_sort(r_arr):
    arr = r_arr.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key <= arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    left, right = [], []
    pivot = arr[0]
    for i in range(n):
        if pivot > arr[i]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


def i_quick_sort_(arr):
    n = len(arr)
    pass


def merge_sort(arr):
    def split(arr):
        n = len(arr)
        if n <= 1:
            return arr
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        return merge(split(left), split(right))

    def merge(left, right):
        lp, rp = 0, 0
        merged_arr = []
        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                merged_arr.append(left[lp])
                lp += 1
            else:
                merged_arr.append(right[rp])
                rp += 1
        while lp < len(left):
            merged_arr.append(left[lp])
            lp += 1

        while rp < len(right):
            merged_arr.append(right[rp])
            rp += 1

        return merged_arr

    return split(arr)


def i_merge_sort(arr):
    def i_merge(arr, left, right, middle):
        l_arr = arr[left:middle]
        r_arr = arr[middle:right + 1]
        l, r, k = 0, 0, left
        while l < len(l_arr) and r < len(r_arr):
            if l_arr[l] > r_arr[r]:
                arr[k] = r_arr[r]
                r += 1
            else:
                arr[k] = l_arr[l]
                l += 1
            k += 1

        while l < len(l_arr):
            arr[k] = l_arr[l]
            l += 1
            k += 1

    n = len(arr)
    width = 1
    while width < n:
        left = 0
        while left < n:
            right = min(n - 1, left + (2 * width) - 1)
            middle = left + width
            i_merge(arr, left, right, middle)
            left += width * 2
        width *= 2

    return arr


def heap_sort(arr):
    def heapify(arr, index, heap_size):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < heap_size and arr[largest] < arr[left]:
            largest = left
        if right < heap_size and arr[largest] < arr[right]:
            largest = right
        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            heapify(arr, largest, heap_size)

    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr





def main():
    random.seed(42)
    arr_dict = {
        "random": [random.randint(0, 1000) for _ in range(1000)],
        "sorted": [i for i in range(1, 1001)],
        "reverse": [i for i in range(1000, 0, -1)],
    }
    # arr_dict = {
    #     "random": [random.randint(0, 20) for _ in range(20)],
    #     "sorted": [i for i in range(1, 11)],
    #     "reverse": [i for i in range(10, 0, -1)],
    # }
    arr_sort = {
        "random": sorted(arr_dict["random"]),
        "sorted": arr_dict["sorted"],
        "reverse": arr_dict["sorted"],
    }
    sort_class = {
        'bubble_sort': bubble_sort,
        'selection_sort': selection_sort,
        'insertion_sort': insertion_sort,
        'quick_sort': quick_sort,
        'merge_sort': merge_sort,
        'merge_sort_iterative' : i_merge_sort,
        'heap_sort': heap_sort,
    }
    sort_list = [
        'bubble_sort',
        'selection_sort',
        'insertion_sort',
        # 'quick_sort',
        'merge_sort',
        'merge_sort_iterative',
        'heap_sort',
    ]
    # sort_list = ['merge_sort_iterative']
    for method in sort_list:
        print(method)
        print("------------------")
        for key, arr_value in arr_dict.items():
            average = 0
            for _ in range(10):
                arr = deepcopy(arr_value)
                start = time.time_ns()
                result = sort_class[method](arr)
                assert result == arr_sort[key]
                end = time.time_ns()
                average += end - start
            print(f"{key}:", average / 10)
        print("==================")


if __name__ == "__main__":
    main()
