
L= []
n=input()

lst = list()
while(n):
    a = raw_input()
    lst = a.split()

    if(lst[0]=="insert"):
        L.insert(int(lst[1]),int(lst[2]))
    elif(lst[0]=="append"):
        L.append(int(lst[1]))
    elif(lst[0]=="print"):
        print L
    elif(lst[0]=="remove"):
        L.remove(int(lst[1]))
    elif(lst[0]=="index"):
        L.index(int(lst[1]))
    elif(lst[0]=="count"):
        L.count()
    elif(lst[0]=="pop"):
        L.pop()
    elif(lst[0]=="sort"):
        L.sort()
    elif(lst[0]=="reverse"):
        L.reverse()
    n-=1
