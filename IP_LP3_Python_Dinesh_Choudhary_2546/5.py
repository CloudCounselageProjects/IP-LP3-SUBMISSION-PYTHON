n=input()
st=[]
for d in n:
	if d not in st:
		st.append(d)
print(''.join(st))