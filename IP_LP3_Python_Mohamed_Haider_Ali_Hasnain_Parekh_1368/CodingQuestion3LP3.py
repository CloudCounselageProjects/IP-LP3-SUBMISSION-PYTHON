#CODING QUESTIONS:​4 (This code was executed in Visual Studio Code)
#Little Robert likes mathematics. Today his teacher has given him two integers and asked to find out how many integers can divide both the numbers. 
# Would you like to help him in completing his school assignment?
#Input Format : There are two integers, a and b as input to the program. 
#Output Format: Print the number of common factors of a and b. Both the input value should be in a range of 1 to 10^12.
# Input:  10  15
# Output: 2


def commonfactors():
    a=int(input())
    b=int(input())
    counter=0
    temp=1
    if a>b:
        while temp<a:
            if a%temp==0 and b%temp==0:
                counter+=1;
            temp+=1;
    else:
        while temp<b:
            if a%temp==0 and b%temp==0:
                counter+=1;
            temp+=1;
    print(counter)
commonfactors()

#End of question 3