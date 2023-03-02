from string import ascii_lowercase
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input().rstrip()
    dic = {}
    ans = 0
    for x in ascii_lowercase:
        dic[x] = [0, 0]
    for x in list(a):
        if x.isupper():
            dic[x.lower()][1] += 1
        else:
            dic[x][0] += 1
    for x in dic.values():
        while min(x) != 0:
            m = min(x)
            x[0] -= m
            x[1] -= m
            ans += m
        if max(x) > 1:
            a = max(x) // 2
            if k > a:
                ans += a
                k -= a
            else:
                ans += k
                k = 0
    print(ans)
