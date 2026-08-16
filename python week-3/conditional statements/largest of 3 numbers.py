#Y.Mukhesh
#largest of three numbers
a=int(input('enter first number:'))
b=int(input('enter secoend number'))
c=int(input('enter third number'))
if a>b:
    if a>c:
        largest=a
    else:
        largest=c
else:
    if b>c:
        largest=b
    else:
        largest=c
print('largest= ',largest)

#output
#enter first number:5
#enter secoend number6
#enter third number3
#largest=  6
