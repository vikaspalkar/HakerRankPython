n = int(raw_input())
dct = dict()
lst = list()
for i in range(n):
    a = raw_input()
    lst = a.split()
    d = lst[0]
    lst.remove(lst[0])
    newlst = list(map(float, lst))
    dct[d] = newlst
name = raw_input()
total = 0
if name in dct:
    marks = dct[name]
    no = len(marks)
    for num in marks:
        total += num
avg = total / no
print "%.2f" % avg
