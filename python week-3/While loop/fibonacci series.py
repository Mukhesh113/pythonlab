#Y.Mukhesh
#Fibonacci series
n=int(input('enter a number of terms:'))
a=0
b=1
i=2
print(a,b,end=' ')
while i<n:
    c=a+b
    print(c, end=' ')
    a=b
    b=c
    i=i+1

#output
#enter a number of terms:7
#0 1 1 2 3 5 8 
