# encoding: utf-8

def shell_sort(arr):

    d = len(arr)
    while d > 0:
        d = d // 2

        for x in range(d):
            for i in range(x+d,len(arr),d):
                temp = arr[i]
                j = i
                while j > 0 and temp < arr[j-d]:
                    arr[j] = arr[j-d]
                    j -= d
                arr[j] = temp
    return arr

arr = [2,5,4,3,7,1]
print(shell_sort(arr))