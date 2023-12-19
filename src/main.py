def bubble_sort(arr):
    circle = 1
    while circle > 0:
        circle = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                circle += 1
    return arr


def bigger_element(arr, k):
    sorted_arr = bubble_sort(arr)
    if k <= len(sorted_arr):
        kth_largest_element = sorted_arr[-k]
        kth_largest_index = arr.index(kth_largest_element)
        return [kth_largest_element, kth_largest_index]
    else:
        raise ValueError("k is greater than the length of the array")
