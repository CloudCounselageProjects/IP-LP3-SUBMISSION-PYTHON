'''Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit ]
'''


celsius = int(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is %0.2f in Fahrenheit' %(celsius, fahrenheit))
fahrenheit = int(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is %0.2f in Celsius' %(fahrenheit, celsius))
