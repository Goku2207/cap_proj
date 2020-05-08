n=int(input("Enter the number of terms "))
a=0
b=1
if n>0:
 print(a)
if n>1:
 print(b)
if n>2:
  for i in range(3,n+1):
    s=a+b
    a=b
    b=s
    print(s)
