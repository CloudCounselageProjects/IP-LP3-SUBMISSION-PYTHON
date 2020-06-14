d=input()
check=d[-1] 
temp=d[:-1]

if check=='F':
	fahrenheit = int(temp);
	celsius = (fahrenheit-32)/1.8;
	c=int(celsius)
	print(str(fahrenheit)+"\N{DEGREE SIGN}"+"F is "+str(c)+" in "+"Celsius")
	
elif check=='C':
	celsius=int(temp)
	fahrenheit = (celsius * 1.8) + 32
	g=int(fahrenheit)
	#print(str(g)+"\N{DEGREE SIGN}"+"F")
	print(str(celsius)+"\N{DEGREE SIGN}"+"C is "+str(g)+" in "+"Fahrenheit")
	
