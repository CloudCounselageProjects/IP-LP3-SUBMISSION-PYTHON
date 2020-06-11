n=str(input())
x=n.find('not')
y=n.find('poor')
if (x<y):
    p=slice(x)
v=n[p]
c=(v+"good")
print(c