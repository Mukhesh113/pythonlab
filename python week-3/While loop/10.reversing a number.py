#Y.Mukhesh
#Reversing a number
n=int(input('enter a number:'))
rev=0
while n > 0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reverse of  given number is ", rev)

#output
#enter a number:2345
#reverse of  given number is  5432
