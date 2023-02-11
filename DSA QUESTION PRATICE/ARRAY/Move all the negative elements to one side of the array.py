n = list(map(int,input().split(',')))
neg = []
pos = []
for i in n:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)

# todo wuth future
pos.sort()
pos.reverse()
res = neg+pos
for i in res:
    print(i,end = " ")

# todo withput fun
# pos.sort()
# pos_rev = []
# for i in range(len(pos)-1,-1,-1):
#     pos_rev.append(pos[i])
# res = neg+pos_rev
# for i in res:
#     print(i,end = " ")