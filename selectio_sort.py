num=[10,20,3,4,22,35,6,7,1]
n=len(num)
'''
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if num[j]<num[min]:
            min=j
    num[i],num[min]=num[min],num[i]'''





for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if num[j]<num[min]:
            min=j
    num[i],num[min]=num[min],num[i]

print("sorted are ->",num)