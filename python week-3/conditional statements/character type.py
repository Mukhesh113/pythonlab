#Y.Mukhesh
#Character type
ch=input('enter character:')
if ch.isalpha():
    if ch.lower() in 'aeiou':
        print('vowel')
    else:
        print('consonant')
elif ch.isdigit():
    print('digit')
else:
    print('special symbol')


#output
#enter character:6
#digit

