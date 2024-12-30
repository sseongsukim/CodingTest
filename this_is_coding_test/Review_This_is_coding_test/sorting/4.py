"""
5 3
1 2 5 4 3
5 5 6 6 5
"""
N, M = map(int, input().split())
alist = sorted(list(map(int, input().split())))
blist = sorted(list(map(int, input().split())), reverse= True)
for i in range(M):
    if alist[i] < blist[i]:
        alist[i], blist[i] = blist[i], alist[i]
    else:
        break

print(sum(alist))