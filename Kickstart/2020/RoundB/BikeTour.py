T = int(input())
for t in range(1, T+1):
    N = int(input())
    hs = [int(num) for num in input().split(" ")]
    peaks = 0
    for i in range(len(hs)):
        if i != 0 and i != len(hs) - 1:
            if hs[i] > hs[i-1] and hs[i] > hs[i+1]:
                peaks += 1
    print("Case #" + str(t) + ": " + str(peaks))
