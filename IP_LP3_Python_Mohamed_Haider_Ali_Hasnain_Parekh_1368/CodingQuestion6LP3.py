#CODING QUESTIONS:​7 (This code was executed in Visual Studio Code)
# ​Write a Python program to convert temperatures to and from celsius, Fahrenheit. 
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in Fahrenheit ]
#Expected Output : 60°C is 140 in Fahrenheit 45°F is 7 in Celsius 

def converter():
    a=int(input('Enter number 1 for celsius to fahrenheit and 2 for fahrenheit to celsius : ', ))
    if a==1:
        celsius = int(input("Enter temperature in celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(celsius ,'C is', fahrenheit ,'in Fahrenheit')
    else:
        fahrenheit = int(input("Enter temperature in fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(fahrenheit , 'F is', celsius, 'in Celsius')
converter()

#End of question 6
