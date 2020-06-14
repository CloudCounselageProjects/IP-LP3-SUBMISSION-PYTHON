m=int(input())
n=int(input())
if 1<=m<=100 and 1<=n<=100:
	a=[]
	rmax=[]
	rmin=[]
	cmax=[]
	cmin=[]
	for i in range(0,m):
		b=[]
		for j in range(0,n):
			b.append(input())
		a.append(b)
	for i in range(0,m):
		rowmin=a[i][0]
		rowmax=a[i][0]
		for j in range(0,n):
                	if a[i][j]>rowmax:
                    		rowmax=a[i][j]
                	if a[i][j]<rowmin:
                    		rowmin=a[i][j]
		rmax.append(rowmax)
		rmin.append(rowmin)
	for j in range(0,n):
		colmin=a[0][j]
		colmax=a[0][j]
		for i in range(0,m):
			if a[i][j]>colmax:
				colmax=a[i][j]
			if a[i][j]<colmin:
				colmin=a[i][j]
		cmax.append(colmax)
		cmin.append(colmin)
	count=0
	for i in range(0,m):
		for j in range(0,n):
 			if a[i][j]==rmax[i] or a[i][j]==rmin[i] or a[i][j]==cmax[j] or a[i][j]==cmin[j]:
					count=count+1
	print(count)
