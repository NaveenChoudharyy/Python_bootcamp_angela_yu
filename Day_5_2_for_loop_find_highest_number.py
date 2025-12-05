# Find the highest number in the list

l1 = [1,21,3,4,5,10,9,8,7,6]

num = l1[0]

for i in l1:
    if i > num:
        num = i
print(num)