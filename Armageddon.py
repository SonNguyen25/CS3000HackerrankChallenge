def findOPT(M, n, tab):
    M[0] = min(x[0], d[0])
    tab[0].append(1)
    i = 1
    while i < n:
        j = 0
        store = []
        maxVal = min(x[i], d[i])
        while j < i:
            if maxVal <= M[j] + min(x[i], d[i-1-j]):
                store = tab[j]
                maxVal = M[j] + min(x[i], d[i-1-j])
            j = j + 1   
        tab[i].extend(store)
        tab[i].append(i+1)
        M[i] = maxVal
        i = i + 1
    return tab[n-1]

def printRes(arr):
    for char in arr:
        print(char, end = " ")
inputs = int(input())
arr = [0 for x in range(inputs)]
val = [[] for x in range(inputs)]
x = list(map(int, input().split()))
d = list(map(int, input().split()))

result = findOPT(arr, inputs, val)
printRes(result)

#4
#1 10 10 1
#1 2 4 8
