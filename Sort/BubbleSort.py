# encoding； utf-8

arr = [2,4,3,6,3,8,5,29,3,8]

def bubble_sort(arr):
    for i in range(len(arr)-1,1,-1):
        check = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                check = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if check == False:
            print(i)
            break
    return arr

print(bubble_sort(arr))