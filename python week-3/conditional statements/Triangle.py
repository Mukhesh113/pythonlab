#Y.Mukhesh
#type of triangle
a=int(input('enter first side:'))
b=int(input('enter secoend side:'))
c=int(input('enter third side:'))
if a == b == c:
    print('equilateral triangle')
elif a==b or b==a or a==c:
    print('isosceles triangle')
elif a+b>c and b+c>a and c+a>b:
    print('scalene triangle')
else:
    print('not a valid triangle')

#output
#enter first side:5
#enter secoend side:3
#enter third side:4
#scalene triangle
