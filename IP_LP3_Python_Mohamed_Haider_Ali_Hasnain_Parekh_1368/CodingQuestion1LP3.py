#CODING QUESTIONS:​1 (This code was executed in Visual Studio Code)
#Read two integers from STDIN and print three lines where:
    #● The first line contains the sum of the two numbers.
    #● The second line contains the difference between the two numbers (first - second).
    #● The third line contains the product of the two numbers.
#Input Format 
#The first line contains the first integer, a. The second line contains the second integer, b
###Constraints
#1<_a<_10​10 1<_b<_10​10
#Output Format Print the three lines as explained above
#Sample Input 3    2
#Sample Output  5  1   6

a = int(input())             
b = int(input())

if 1<=a<=10*10 and 1<=b<=10*10:            
 sum = a+b
 difference = a-b
 product = a*b

 print (sum)                               #sum of a and b
 print (difference)                        #difference between a and b
 print (product)                           #product of a and b 

#End of question 1