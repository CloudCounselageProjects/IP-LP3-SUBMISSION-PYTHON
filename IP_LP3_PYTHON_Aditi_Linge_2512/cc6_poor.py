e=input()
#not...poor then replace whole by good
res=e.split()
#a=str(res)

if (('not' in e) and (('poor' or 'poor?' or 'poor!' or 'poor,') in e)):
    i_n=res.index("not")
   
    
    
    
    
        
        
    if('poor?' in e):
        i_p=res.index("poor?")
        if(i_n<i_p):
            res[i_n:i_p+1]=""
            res.insert(i_n,'good?')
        
        
    elif('poor!' in e):
         i_p=res.index("poor!")
         if(i_n<i_p):
             res[i_n:i_p+1]=""
             res.insert(i_n,'good!')
        

    elif('poor,' in e):
        i_p=res.index("poor,")
        if(i_n<i_p):
             res[i_n:i_p+1]=""
             res.insert(i_n,'good,')

    elif('poor' in e):
         i_p=res.index("poor")
         if(i_n<i_p):
             res[i_n:i_p+1]=""
             res.insert(i_n,'good')
       
#list comprehension for list_to_string
    s=' '.join([str(i) for i in res])

    #print(res)
    print(s)

else:
    print(e)

    





    
