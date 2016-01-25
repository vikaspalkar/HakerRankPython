#You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
#(Rangoli is a form of Indian folk art based on creation of patterns.)

#Different sizes of alphabet rangoli are shown below:

#size 3

#  ----c----
#  --c-b-c--
#  c-b-a-b-c
#  --c-b-c--
#  ----c----



import string

n=input()

alpha=string.ascii_lowercase

for i in range(n-1,0,-1):
    row=["-"]*(n*2-1)
    for j in range(0,n-i):
        row[n-1-j]=alpha[j+i]
        row[n-1+j]=alpha[j+i]
    print "-".join(row)

for i in range(0,n):
    row=["-"]*(n*2-1)
    for j in range(0,n-i):
        row[n-1-j]=alpha[j+i]
        row[n-1+j]=alpha[j+i]
    print "-".join(row)
