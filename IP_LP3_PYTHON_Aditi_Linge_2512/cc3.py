n=int(input())
a=[]
count=0
unique_list=[]
#input of words
for i in range(0,n):
    s=input()
    a.append(s)



#count distinct words in list
for i in a:
    if i not in unique_list:
        unique_list.append(i)
    


res=[]
for i in unique_list:
    res.append(a.count(i))
        
             
    
print(len(unique_list))

for i in res:
    print(i,end=" ")


    
