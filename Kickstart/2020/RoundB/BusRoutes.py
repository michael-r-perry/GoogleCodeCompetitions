T = int(input())
for t in range(1, T+1):
    N, D = [int(num) for num in input().split(" ")]
    bts = [int(num) for num in input().split(" ")][::-1]
    for i in range(N):
        D = D // bts[i] * bts[i]
    print("Case #" + str(t) + ": " + str(D))
