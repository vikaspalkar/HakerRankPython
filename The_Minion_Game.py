#Kevin and Stuart want to play the 'The Minion Game'.

#Game Rules

#Both players are given the same string, S.
#Both players have to make substrings using the letters of the string S.
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.

#Scoring
#A player gets +1 point for each occurrence of the substring in the string S.

#For Example:
#String S = BANANA
#Kevin's vowel beginning word = ANA
#Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

str1=raw_input()
vowels='AEIOU'

kevinscore=0
stuartscore=0

for i in range(len(str1)):
    if str1[i] in vowels:
        kevinscore+=(len(str1)-i)
    else:
        stuartscore+=(len(str1)-i)

if kevinscore>stuartscore:
    print "Kevin",kevinscore
elif kevinscore<stuartscore:
    print "Stuart",stuartscore
else:
    print "Draw"
