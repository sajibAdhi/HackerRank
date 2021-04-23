x = int(input())
y = int(input())
z = int(input())
n = int(input())

finalList = list()
i = 0
while i <= x:
    j = 0
    while j <= y:
        k = 0
        while k <= z:
            if i+j+k != n:
                finalList.append([i, j, k])
            k = k+1
        j = j+1
    i = i+1
print(finalList)
