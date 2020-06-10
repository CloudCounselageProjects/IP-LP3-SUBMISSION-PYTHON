print('Provide temperature in celsius')
celsius = float(input())
print('Provide temperature in fahrenheit')
fahrenheit = float(input())
f = ((celsius*9)/5) + 32
print('%0.1f degree C is %0.1f in Fahrenheit' %(celsius,f))
c = ((fahrenheit - 32)*5)/9
print('%0.1f Fahrenheit is %0.1f in Celsius' % (fahrenheit,c))