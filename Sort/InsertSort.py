# encoding: utf-8

arr = [2,5,4,3,7,1]

# 直接插入
def insert_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr

# 二分插入
def insert_sort_binary(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            left = 0
            right = i - 1
            temp = arr[i]

            while left <= right:
                mid = (left + right)//2
                if arr[i] < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            for j in range(i-1,left-1,-1):
                arr[j+1] = arr[j]
            arr[left] = temp
    return arr

print(insert_sort(arr))
print(insert_sort_binary(arr))
