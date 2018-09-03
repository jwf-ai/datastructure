# encoding: utf-8

arr = [2,5,4,3,7,1]

def insert_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr

print(insert_sort(arr))
