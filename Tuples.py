n=input()

T= tuple(int(x.strip()) for x in raw_input().split(' '))

count=T.__hash__()

print count
