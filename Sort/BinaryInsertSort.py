# encoding: utf-8


def binary_insert_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        left = 0
        right = i-1

        while left <= right:
            middle = (left + right) // 2
            if temp < arr[middle]:
                right = middle -1
            else:
                left = middle + 1
        for j in range(i-1,j,-1):
            arr[j+1] = arr[j]

        arr[j] = temp

arr = [3,2,5,4,7,5,9,6,3,5]
print(binary_insert_sort(arr))