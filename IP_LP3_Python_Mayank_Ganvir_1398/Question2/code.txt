a=int(input("Enter the number:"))
if(a%400==0 or a%100!=0 and a%4==0):
    print("True")
else:
    print("False")