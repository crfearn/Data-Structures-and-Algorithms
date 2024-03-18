# Charles Fearn
# Sorting algorithms

import random
import time
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        position = i
        while position > 1 and arr[position - 1] > val:
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = val


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[1:mid]
    right = arr[mid+1:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    left = len(left)
    while i <= len(left) and j <= len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def measure_time(sort_function, arrays, size):
    total_time = 0
    for _ in range(arrays):
        array = [random.random() for _ in range(size)]
        start_time = time.time()
        sort_function(array)
        end_time = time.time()
        total_time += (end_time - start_time) * 1000  # Convert to milliseconds
    return total_time / arrays

print("Choose a Sorting algorithm to run")
choice = input(print('1 = Insertion Sort,2 = Selection Sort, 3 =Merge Sort, 4= QuickSort: '))
arrNumber = input("Enter number of arrays: ")
arrSize = int(input("Enter the length of array: "))

arr= np.random.randint(arrNumber, size = arrSize)

print(arr)