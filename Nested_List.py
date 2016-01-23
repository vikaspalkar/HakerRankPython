n=input()
L=[]
for x in range(n):
    a=raw_input()
    b=input()
    L.insert(x,[b,a])
L.sort()

min=L[0][0]
count=0
for z in L:
    b = L[count][0]
    if(b>min):
        secmin=L[count][0]
        break
    count+=1
c=0
lis1=[]
for y in L:
    if(L[c][0]==secmin):
        lis1.append(L[c][1])
    c+=1

lis1.sort()
c1=0
for s in lis1:
    print lis1[c1]
    c1+=1
