arr=list(map(int,input().split()))
for i in range(len(arr)-1):
	mini=arr[i]
	pos=i
	for j in range(i+1,len(arr)):
		if arr[j]<mini:
			mini=arr[j]
			pos=j
	arr[pos]=arr[i]
	arr[i]=mini
print(arr)