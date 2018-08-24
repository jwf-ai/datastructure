# encoding: utf-8

def merge_sort(arr,arr_tmp,left,right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, arr_tmp, left,mid)
        merge_sort(arr,arr_tmp,mid+1,right)
        merge(arr,arr_tmp,mid,left,right)

def merge(arr,arr_tmp,mid,left,right):
    i = left
    j = mid + 1
    k = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            arr_tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            arr_tmp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        arr_tmp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        arr_tmp[k] = arr[j]
        k += 1
        j += 1

    for h in range(k):
        arr[left+h] = arr_tmp[h]

arr = [3,5,7,4,8,9,6,4,8,5]
arr_tmp = [0] * len(arr)

merge_sort(arr,arr_tmp,0,len(arr)-1)
print(arr)