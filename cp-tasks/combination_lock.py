# https://dmoj.ca/problem/bts19p4 identical problem



from sys import stdin, exit

def solve():
    n, m = 12, 9

    arr = sorted([1, 1, 2, 2, 7, 7, 8, 8, 8, 8, 9, 9])

    prev = cur = down = 0

    for i in arr:
        cur += min(m - i, i)
        if i + i < m:
            down += 1

    best = cur
    length = len(arr)

    for num, i in enumerate(arr[:]):

        delta = i - prev
        if delta == 0:
            arr.append(i)
            length += 1
            continue

        cur -= delta * (down - num)

        while down < length and (arr[down] - i) % m * 2 <= m:
            cur += (arr[down] - i) % m - (prev - arr[down]) % m
            down += 1

        cur += delta * (length - down)

        best = min(best, cur)

        prev = i
        arr.append(i)
        length += 1

    return best

print("Case #%d: %d" % (1, solve()))