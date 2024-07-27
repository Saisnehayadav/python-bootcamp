#i/p:hello123world
#o/p:6
check="0123456789"
ans=0
i="hello 123wOrld"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)
