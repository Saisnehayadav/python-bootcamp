#7.1you are given eith a comma seperated natural numbers 1 to 10. print only the even numbers
'''ist=list(map(int,input().split(",")))
for i in range(0,len(list)):
    if(list[i]%2==0):
        print(list[i],end=" ")
for i in range(1,len(list),2):
    print(list[i])
    
7#.2 how many even num are there in the above question
list=list(map(int,input().split(",")))
count=0
for i in range(1,len(list),2):
    count+=1
print(count)

#.3 you are given with a space seperated integer list find the number of even elements and odd elements in a given list
list=list(map(int,input().split(",")))
count_even=0
count_odd=0
for i in range(0,len(list)):
    if(list[i]%2==0):
        count_even+=1
    else:
       count_odd+=1
print(count_even,count_odd)'''

