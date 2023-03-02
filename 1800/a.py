from re import compile
from sys import stdin

input = stdin.readline

meow = compile(r"(?i)[m]+[e]+[o]+[w]+")
for _ in range(int(input())):
    input()
    print("YES" if meow.fullmatch(input().rstrip()) else "NO")
