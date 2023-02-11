from numpy import *
def reverse(a):
    result = []

    y=len(a)-1
    while(y>=0):
        result.append(a[y])
        y-=1

    result = array(result)
    return result
a=array([1,2,3,7,8,90,80])
b=reverse(a)
print(b)

# todo string reverse
a="codex coder"
b=len(a)-1
r=''
for i in range(b,-1,-1):
    r=r+a[i]
print(r)