#Read a given string, change the character at a given index and then print the modified string.

#Input Format 
#The first line contains a string, S. 
#The next line contains an integer i, denoting the index location and a character c separated by a space.

s=raw_input()
l=raw_input()
a=list(l.split(" "))
b=int(a[0])
c=a[1]

s1 = list(s)

s1[b] = c
s = ''.join(s1)
print s
