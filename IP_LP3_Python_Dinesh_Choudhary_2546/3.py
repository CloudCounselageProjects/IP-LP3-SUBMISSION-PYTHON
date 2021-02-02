n=int(input())
wr=[]
wr2=[]
for i in range(n):
	word=input()
	wr.append(word)
	if word not in wr2:
		wr2.append(word)
print(len(wr2))
for d in wr2:
	print(wr.count(d),end=' ')

	

	