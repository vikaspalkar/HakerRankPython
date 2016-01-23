# Enter your code here. Read input from STDIN. Print output to STDOUT


n=input()

lis=[]
a =raw_input()
lis=a.split()
newlis=list(map(int,lis))
newlis.sort()

st=set(newlis)

st=st.union()

L=list(st)
L.sort()
print L[-2]
