#Y.Mukhesh
#sum,average of digits
n=int(input('enter a number:'))
temp=n
sum=0
count=0
while temp > 0:
    digit= temp%10
    sum=sum+digit
    count=count+1
    temp=temp//10
average=sum/count
print('sum= ', sum)
print('average= ', average)

#output
#enter a number:2026
#sum=  10
#average=  2.5
