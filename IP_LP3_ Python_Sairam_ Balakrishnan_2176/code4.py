num1 = int(input())
num2 = int(input())
count = 0
if(num1>=num2):
    for i in range(1,num2+1):
        if(num1%i==0 and num2%i==0):
            count = count + 1
else:
    for i in range(1,num1+1):
        if (num1%i==0 and num2%i==0):
            count = count + 1

print(count)
