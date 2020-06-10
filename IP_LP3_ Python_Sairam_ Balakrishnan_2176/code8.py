print("1.Fahrenheit to Celcius")
print("2.Celcius to Fahrenheit")
choice = int(input())

if(choice==1):
    F = int(input())
    C = 5/9*(F-32)
    print(int(C))

else:
    C = int(input())
    F = C*9/5+32
    print(int(F))
