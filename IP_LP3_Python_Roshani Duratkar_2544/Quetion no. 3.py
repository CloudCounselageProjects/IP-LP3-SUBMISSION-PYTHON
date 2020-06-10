# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:34:29 2020

@author: HP
"""

def freq(str): 
  
    # break the string into list of words  
    str = str.split()          
    str2 = [] 
    sum=0
    # loop till string values present in list str 
    for i in str:              
  
        # checking for the duplicacy 
        if i not in str2: 
  
            # insert value in str2 
            str2.append(i)  
              
    for i in range(0, len(str2)): 
  
        # count the frequency of each word(present  
        # in str2) in str and print 
        sum=sum+i
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))     
    print(sum)
def main(): 
    n=int(input("Enter no of words: "))
    print("Enter ",n," words: ")
    str=input()
    freq(str)                     
  
if __name__=="__main__": 
    main()       