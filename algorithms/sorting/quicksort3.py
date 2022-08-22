def lomutoPartition(A, low, high):
    if low >= high:
        return
    pivot = A[high]
    i = low-1
    for j in range(low, high):
        if pivot >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    print(*A)
    lomutoPartition(A, low, i)
    lomutoPartition(A, i+2, high)


ar_count = int(input().strip())

A = list(map(int, input().rstrip().split()))

lomutoPartition(A, 0, len(A)-1)
