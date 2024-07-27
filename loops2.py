#1.using for loop print 1 to 100 num
#2.using for loop append 1 to 100 in empty list
# 3.find sum of 1 to 100 num in a list

for i in range(1,101):
    print(i,end=" ")


list=[]
for i in range(1,101):
   list.append(i)
print(*list)   



sum=0
for i in range(1,101):
    sum+=i
print(sum)    


n=int(input())
s=n*(n+1)/2
print(s)


