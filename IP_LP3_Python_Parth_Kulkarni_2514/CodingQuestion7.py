#Write a Python program to convert temperatures to and from celsius, Fahrenheit. 
celcius = float(input('Enter temperature in celcius: '))
fahrenheit = (celcius * 9/5) + 32
f = float(input('Enter temperature in fahrenheit: '))
c = (f-32)*5/9
degree=u"\N{DEGREE SIGN}" 
print(celcius,degree+'C is ',round(fahrenheit),'in Fahrenheit')
print(f,degree+'F is ',round(c),'in Celcius')
#Expected Output : 
#60°C is 140 in Fahrenheit 
#45°F is 7 in Celsius 