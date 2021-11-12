inputs = []
n = int(input())
for i in range(n):
    word = input()
    inputs.append(word)

def LCPHelper(w1, w2):
    length = min(len(w1), len(w2))
    commonPrefix = []
    i = 0
    while i <= length-1:
        if w1[i] != w2[i]:
            break
        commonPrefix.append(w1[i])
        i += 1
    return commonPrefix

def LCP(array):
    if len(array) == 2:
        return LCPHelper(array[0], array[1])
    if len(array) == 1:
        return array[0]
    if len(array) > 0:
        B = array[:len(array)//2]
        C = array[len(array)//2:]
        half1 = LCP(B)
        half2 = LCP(C)
        return LCPHelper(half1, half2)

print(''.join(map(str, LCP(inputs)))) 

