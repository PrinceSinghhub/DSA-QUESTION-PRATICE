arr = [1000, 11, 445, 1, 330, 3000]
min = arr[0]
max = arr[0]

if min > max:
    min = arr[1]
    max = arr[0]
else:
    min = arr[0]
    max = arr[1]

print(min,max)