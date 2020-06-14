def calculate():
    result=set()
    m=int(input())
    n=int(input())
    matrix=[]
    for i in range(0,m):
        row=list(map(int,input().split()))
        matrix.append(row)

    for i in range(0,m):

        maximum=max(matrix[i])
        count=0
        for k in range(n):
            if maximum==matrix[i][k]:
                count=count+1
        if count>1:
            return -1

        minimum=min(matrix[i])
        count=0
        for k in range(n):
            if minimum==matrix[i][k]:
                count=count+1
        if count>1:
            return -1
        
        result.add(maximum)
        result.add(minimum)
    
    column=[]
    for i in range(m):
        column.append([])
    for i in range(m):
        for j in range(n):
            column[j].append(matrix[i][j])
    for i in range(n):
        maximum=max(column[i])
        count=0
        for k in range(m):
            if maximum==column[i][k]:
                count=count+1
        if count>1:
            return -1
        
        minimum=min(column[i])
        count=0
        for k in range(m):
            if minimum==column[i][k]:
                count=count+1
        if count>1:
            return -1
        
        result.add(maximum)
        result.add(minimum)
    return(len(result))

answer=calculate()
print(answer)