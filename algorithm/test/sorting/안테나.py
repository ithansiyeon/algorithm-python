import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().rstrip().split(" ")))
array.sort()

print(array[(n-1)//2])