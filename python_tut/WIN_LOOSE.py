''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
from sys import stdin, stdout


def main():
    result = []
    for test in range(int(input())):
        inputs = int(input())
        lstW = []
        lstW=list(map(int,input().split()))
        lstW= [int(x) for x in lstW]
        lstP = []
        lstP = (stdin.readline().split())
        lstP=[int(x) for x in lstP]
        lstP = sorted(lstP)
        lstW = sorted(lstW)
        flag=1
        for x,y in zip(lstP,lstW) :
            if (y > x) :
                flag=0
                break
        if(flag==1):
            result.append('WIN')
        else :
            result.append('LOSE')
    for elem in result :
        print(elem)



main()
