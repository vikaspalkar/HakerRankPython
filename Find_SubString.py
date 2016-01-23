a=raw_input()
b=raw_input()
count=0
for c in range(len(a)):
    if a[c:c+len(b)] == b:
        count += 1
print count
