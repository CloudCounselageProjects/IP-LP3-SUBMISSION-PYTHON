#CODING QUESTIONS:7
#Write a Python program to convert temperatures to and from celsius, Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in Fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius


temp = input()
if 'C' in temp:
	lst = temp.split('C')
	result = int(round((9 * int(lst[0])) / 5 + 32))
	print(int(lst[0]),"°C is ",sep='',end='')
	print(result,"in Fahrenheit")
elif 'F' in temp:
	lst = temp.split('F')
	result = int(round((int(lst[0]) - 32) * 5 / 9))
	print(int(lst[0]),"°F is ",sep='',end='')
	print(result,"in Celsius")
else:
	print("Input proper convension")


#INPUT:
#60C

#OUTPUT:
#60°C is 140 in Fahrenheit

