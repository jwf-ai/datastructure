# encoding: utf-8


def siftDown(i,arr,n):
    while 2 * i + 1 < n:
        left = 2 * i + 1
        right = 2 * i + 2
        maxChild = 0
        if arr[i] < arr[left]:
            maxChild = left
        else:
            maxChild = i
        if right < n:
            if arr[maxChild] < arr[right]:
                maxChild = right

        if maxChild != i:
            arr[maxChild],arr[i] = arr[i],arr[maxChild]
            i = maxChild
        else:
            break

def adjustHeap(arr,n):
    start = n // 2 -1
    for i in range(start,-1,-1):
        siftDown(i,arr,n)
    return arr



if __name__ == "__main__":
    arr = [16,7,3,20,17,8]

    for i in range(len(arr)-1,0,-1):
        arr = adjustHeap(arr,i+1)
        arr[0],arr[i] = arr[i],arr[0]


    print(arr)
