import numpy as np
import random
import time
import sys


#Insertion
def insertion_sort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        temp = arr[i]
        j = i-1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

#selection
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]



#Merge
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    i = 0    
    j = 0
    k = l
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def merge_sort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)



#QuickSort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    else: 
      return arr
      
def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
 
            i = i + 1
 
            (arr[i], arr[j]) = (arr[j], arr[i])
 
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
 
    return i + 1

if __name__ == "__main__":
    # while True:
    #     #print("Choose a Sorting algorithm to run")
        # choice = sys.argv[1] #input('1 = Insertion Sort,2 = Selection Sort, 3 =Merge Sort, 4= QuickSort:')
        # if (choice=="insertion" or choice=="selection" or choice=="merge"or choice =="quick"):
        #     break
    choice = sys.argv[1]
    arrNumber = int(sys.argv[2]) #input("Enter number of arrays: "))
    arrsize= int(sys.argv[3]) #input("Please select size of arrays:"))
    randDF = np.random.rand(arrNumber,arrsize)
    if choice == "insertion":
      start = time.time()
      for row in randDF:
        insertion_sort(row)
      end = time.time()
      print("Running time in Miliseconds is: ",((end - start)*1000)/arrNumber)
    if choice == "selection":
      start = time.time()
      for row in randDF:
        selection_sort(row)
      end = time.time()
      print("Running time in Miliseconds is: ",((end - start)*1000)/arrNumber)

    if choice == "merge":
      start = time.time()
      for row in randDF:
        merge_sort(row,0,arrsize-1)
      end = time.time()
      print("Running time in Miliseconds is: ",((end - start)*1000)/arrNumber)

    if choice == "quick":
      start = time.time()
      for row in randDF:
        quick_sort(row,0,arrsize-1)
      end = time.time()
      print("Running time in Miliseconds is: ",((end - start)*1000)/arrNumber)



    