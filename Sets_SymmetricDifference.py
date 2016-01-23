n=input()

a = raw_input()
lis = a.split()
newlis = list(map(int, lis))


m=input()

b = raw_input()
lis1 = b.split()
newlis1 = list(map(int, lis1))


set1= set(newlis)
set2=set(newlis1)

set3=set1.symmetric_difference(set2)
l=list(set3)
l.sort()

for x in l:
    print x
