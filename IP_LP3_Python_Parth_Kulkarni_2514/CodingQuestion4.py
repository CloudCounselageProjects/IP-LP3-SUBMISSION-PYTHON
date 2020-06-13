#Little Robert likes mathematics. Today his teacher has given him two integers and             asked to find out how many integers can divide both the numbers. Would you like to                help him in completing his school assignment? 
x = int(input())
y = int(input())			

def cal_fact(x,y):
	if (x == 0):
		return y
	return (cal_fact(y%x,x))

if (x>0 and x<(10**12+1) and y>=1 and y<(10**12+1)):
    count = 1
    for i in range(2, cal_fact(x, y)+1):
        if x % i == 0 and y % i == 0:
            count = count + 1
    print(count)
#Input:  10  15 
#Output: 2

