def appearance(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
  
    #print(snot)
    if spoor>snot and snot!=-1:
        str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  
print(appearance("'The lyrics is not that poor!'"))
print(appearance("'The lyrics is poor!'"))

