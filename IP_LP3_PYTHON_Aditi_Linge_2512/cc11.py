from datetime import *
year=int(input())
month=int(input())
day=int(input())
inp=datetime(year,month,day)

print(datetime.date(inp).isocalendar()[1])

