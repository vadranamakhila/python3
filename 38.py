m,n=map(int,raw_input().split())
m = m ^ n
n = m ^ n
m = m ^ n
print m,n
