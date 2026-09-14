s = input("Enter a string: ")
ch = input("Enter character to count: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print("Occurrences:", count)
#output:
Enter a string: mukhesh
Enter character to count: e
Occurrences: 1
