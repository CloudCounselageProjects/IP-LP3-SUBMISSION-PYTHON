def cel(f):
	c=((f-32)/9)*5
	print(str(f)+chr(176)+'F is '+str(round(c))+' in Celsius')
def fe(c):
	f=((c/5)*9)+32
	print(str(c)+chr(176)+'C is '+str(round(f))+' in Fahrenheit')
c=int(input('Enter temperature in Celsius : '))
f=int(input('Enter temperature in Fahrenheit : '))
fe(c)
cel(f)
