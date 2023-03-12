# To find median of number.
n=int(input("Enter no. of numbers: "))
y=[]
print("Enter the numbers: ")
for i in range(n):
    x=int(input())
    y.append(x)
y.sort()
print(y)
if n%2!=0:
    m=len(y)//2
    print("median:" ,y[m])
else:
    m = len(y) // 2
    print("median:", (y[m]+y[m-1])/2)

