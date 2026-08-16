#Y.Mukhesh
#inverted right angled traingle
n=int(input('enter number of rows:'))
for i in range(n,0,-1):
    for j in range(i):
        print('*', end=' ')
    print()

#output
#enter number of rows:5
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 
