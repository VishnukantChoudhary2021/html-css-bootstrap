import matplotlib.pyplot as plt
passs=0
numbers=[5,4,3,2,1]
y=[10,20,30,40,50]

plt.plot(numbers,y)
plt.xlabel("age")
plt.ylabel("year")
plt.title("population")
plt.show()

plt.plot(numbers,y,label="student marks" )
plt.grid()
# for i in range(len(numbers)-1):
#     swap=False
#     passs+=1

#     for j in range(len(numbers)-i-1):
#         if numbers[j]>numbers[j+1]:
#             numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
#             swap=True
#     if not swap:
#         break

'''
n=len(numbers)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if numbers[j]<numbers[min]:
            min=j
    temp=numbers[i]
    numbers[i]=numbers[min]
    numbers[min]=temp
    

print(passs)
print(numbers)'''