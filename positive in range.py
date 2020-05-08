list=[]
n=int(input("Enter number of elements in list "))
for i in range(1,n+1):
 e=int(input())
 list.append(e)
print("The positive numbers in the range are")    
for j in list:
    if j>0:
     print(j)
