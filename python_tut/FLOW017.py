from sys import stdin
for _ in range(int(input())):
    lst = list(map(int, stdin.readline().split(' ')))
    lst = sorted(lst)
    print(lst[1])
