#problem number 9

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
    # assume the first element as the minimum.
        mini = i
        for j in range(i+1, n):
            if (arr[j] < arr[mini]):
                # Update position of minimum element if a smaller element is found.
                mini = j
        # Swap the minimum element with the first element of the unsorted part.     
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    return arr


A = []
n = int(input())
for i in range(n):
    x = int(input())
    A.append(x)
print(selectionSort(A))

