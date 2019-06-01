for _ in range(int(input())) :
    lst=list(map(int,input()))
    lst=lst[::-1]
    str1=int("".join(map(str,lst)))
    print(str1)