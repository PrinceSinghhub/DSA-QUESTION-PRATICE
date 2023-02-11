# arr = [5,-2,-3,-4]
arr = [-2,-6,-8,-9,-7,100,600]
# todo for neg all
all_neg = []
for i in arr:
    if i<0:
        all_neg.append(i)
    if i>=0:
        break
if len(arr) == len(all_neg):
    all_neg.sort()
    print(all_neg[len(all_neg)-1])
    quit()

# todo for non neg and positive
max = 0
current = 0
for i in arr:
   current+=i

   if current>max:
       max = current

   if current<0:
       current = 0
print(max)
