#Y.Mukhesh
#leap year
year=int(input('enter year:'))
if year%400 == 0:
    print(year, 'is a leap year')
elif year%4 == 0 and year%100!=0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')

#output
#enter year:1900
#1900 is not a leap year
