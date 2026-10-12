

num=[1,20,3,67,7,9,23,12,5]
n=len(num)

for i in range(1,n):
    key=num[i]
    j=i-1
    while j>=0 and num[j]>key:
        num[j+1]=num[j]
        j-=1
    num[j+1]=key

print(num)


'''for i in range(n-1):
    key=num[i]
    j=i+1
    while j>=0 and num[j]<key:
        num[j-1]=num[j]
        j-=1
    num[j+1]=key

print(num)'''
