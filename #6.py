#take a space seperated input from user and print alternate elements
list=list(map(int,input().split( )))
for i in range(0,len(list),2):
    print(list[i],end=" ")