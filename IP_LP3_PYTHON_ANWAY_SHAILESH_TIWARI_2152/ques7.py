# question 7


n = int(input('enter thr choice\n1.celcius to fahrenheit\n2.fahrenheit to celcius\n'))
if n == 1:
    c = float(input('enter value of celcius\n'))
    f = (c*9/5)+32
    print(f'{c}°C is {f} in Fahrenheit ')
elif n == 2:
    f = float(input('enter value in fahrenhiet\n'))
    c = (f - 32)*5 / 9
    print(f'{f}°F is {c} in Celsius')
