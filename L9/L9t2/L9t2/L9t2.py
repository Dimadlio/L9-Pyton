n=list(map(int,input().split()))
a1=set()
for i in n:
    print('YES' if i in a1 else 'NO')
    a1.add(i)