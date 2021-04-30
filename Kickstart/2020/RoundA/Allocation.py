T = int(input())
for x in range(1, T+1):
    N, B = [int(num) for num in input().split(" ")]
    prices = [int(num) for num in input().split(" ")]
    prices.sort()
    purchNum = 0
    for price in prices:
        if price > B:
            break
        B -= price
        purchNum += 1
    print("Case #" + str(x) + ": " + str(purchNum))
