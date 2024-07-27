#ascii
'''print(ord("a"))'''

#print the ascii values
'''for i in range(32,128):
    print(chr(i),end=" ")'''


#check how many vowels are there in a string
'''check=['a','e','i','o','u']
count=0
inp="vaishnavi"
for i in inp:
    if(i in check):
        count+=1
print(count)'''

#if uppercase letters are present
'''check=['a','e','i','o','u']
count=0
i="vaishnAvi"
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
print(count)'''

#consonants
'''vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="vaishnAvi"
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
    if(i in consonants):
        c+=1
print(count)
print(c)'''

#print all the vowels followed by consonants
'''vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
ans=""
i="vaishnAvi"
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
for i in inp:
    if(i in consonants):
         ans+=i
print(ans)'''







