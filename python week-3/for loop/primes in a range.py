#Y.Mukhesh
#Primes in range
start=int(input('enter starting number:'))
end=int(input('enter ending number:'))
for n in range(start, end+1):
    count=0
    for i in range(2, n):
        if n%i==0:
            count=count+1
    if count==0:
        print(n,end=' ')

#output
#enter starting number:4
#enter ending number:10
#5 7 
