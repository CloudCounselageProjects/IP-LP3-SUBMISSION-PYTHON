n=int(input())
d={}
for i in range(n):
	w=input()
	d[w]=d.get(w,0)+1
print(len(d))
for i in d:
	print(d[i],end=' ') 