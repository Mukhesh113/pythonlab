#Y.Mukhesh
#prime
n=int(input('enter a number:'))
count=0
for i in range(2, n):
    if n%i==0:
        count=count+1
if count==0:
    print('prime')
else:
    print('not prime')

#output
#enter a number:567
#not prime
