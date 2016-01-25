
#capitalize first letter of each word in given string

s= raw_input()
s1 = s.split(" ")
for i in range (0,len(s1)): 
    s1[i]= s1[i].capitalize()
print ' '.join(s1)
