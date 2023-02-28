from sys import stdin
input = stdin.readline

fb = "FBFFBFFBFBFFBFFBFBFFBFFBFBFFBFFB"
for _ in range(int(input())):
    n = int(input())
    if input().rstrip() in fb:
        print("YES")
    else:
        print("NO")
