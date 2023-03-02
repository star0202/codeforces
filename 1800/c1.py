from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    input()
    s = list(map(int, input().split()))
    bonus = []
    ans = 0
    for i in range(len(s)):
        if s[i] == 0 and s[:i]:
            ss = sorted(s[:i], reverse=True)
            ans += ss[0]
            s[s.index(ss[0])] = 0
    print(ans)
