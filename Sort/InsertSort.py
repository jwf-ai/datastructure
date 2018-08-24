# encoding: utf-8

arr = [2,4,5,3,4,8,6,4,5,7,3,8]

def insert_sort(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            for j in range(i-1,0,-1):
                if temp < arr[j]:
                    arr[j+1] = arr[j]
                else:
                    arr[j] = temp
                    break
    return arr

print(insert_sort(arr))
