# encoding: utf-8

def quick_sort(arr, left, right):
    if left < right:
        pivotpos = partition(arr,left,right)
        quick_sort(arr,left,pivotpos-1)
        quick_sort(arr,pivotpos+1,right)


def partition(arr, left, right):
    pivotpos = left
    pivot = arr[left]

    for i in range(left+1,right):
        if arr[i] < pivot:
            pivotpos += 1
            if pivotpos != i:
                arr[pivotpos],arr[i] = arr[i],arr[pivotpos]
    arr[left] = arr[pivotpos]
    arr[pivotpos] = pivot

    return pivotpos

arr = [5,8,9,7,4,6,9,3,1,6]
quick_sort(arr,0,len(arr))
print(arr)