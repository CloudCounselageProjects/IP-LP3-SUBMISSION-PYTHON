
def year1(year):
	if(year>=1990 and year<=2010):
		if(year%4==0 and year%100!=0 or year%400==0):
			return True
		else:
			return False
year=int(input())
r=year1(year)
print(r)