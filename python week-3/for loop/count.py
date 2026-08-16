#Y.Mukhesh
#count
s=input('enter string:')
vowels=0
consonants=0
digits=0
spaces=0
for ch in s:
    if ch.lower() in 'aeiou':
        vowels=vowels+1
    elif ch.isalpha():
        consonants=consonants+1
    elif ch.isdigit():
        digits=digits+1
    elif ch==' ':
        spaces=spaces+1
print('vowels=', vowels)
print('consonants=',consonants)
print('digits=', digits)
print('spaces=', spaces)

#output
#enter string:Python program
#vowels= 3
#consonants= 10
#digits= 0
#spaces= 1
