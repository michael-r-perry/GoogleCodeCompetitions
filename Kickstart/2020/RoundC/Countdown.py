T = int(input())
for t in range(1, T+1):
    N, K = [int(num) for num in input().split(" ")]
    A = [int(num) for num in input().split(" ")]
    d_count = 0
    count = 0
    for i in range(1, N):
        if (A[i] == A[i-1] - 1):
            d_count += 1
        else:
            d_count = 0
        if (A[i] == 1 and d_count >= K-1):
            count += 1
    print("Case #" + str(t) + ": " + str(count))
