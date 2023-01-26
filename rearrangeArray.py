array = ["elephant", "boy", "ant", "truck", "zebra", "sister", "sinister"]

def arrangeTheArray(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

rearranged = arrangeTheArray(array)
print(rearranged)
n = list(reversed(rearranged))
print(n)
