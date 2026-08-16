#Y.Mukhesh
#palindrome
n=int(input('enter a number:'))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if original==rev:
    print('palindrome.')
else:
    print('not a palindrome.')

#output
#enter a number:1221
#palindrome.
