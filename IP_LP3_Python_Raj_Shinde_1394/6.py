# problem number 6   
def countSpecialElements(matrix):
    nRows= len(matrix)
    nCount=0

    for row in matrix:
        for indexCol, element in enumerate(row):
            if element==min(row) or element==max(row):
                if row.count(element)>1:
                    return -1
                nCount=nCount+1
            else:
                listColumn=[]
                
                for indexRow in range(0, nRows):
                    listColumn.append(matrix[indexRow][indexCol])
                    
                if element==min(listColumn) or element==max(listColumn):
                    if listColumn.count(element)>1:
                        return -1
                    nCount=nCount+1
    return nCount

# Accept number of rows and columns 
R, C = map(int,input().split())
#Accept elements rowwise  
if 0 < R and C < 100:
    matrix = []  
    for i in range(R):           
        a =[] 
        for j in range(C):       
             a.append(int(input())) 
        matrix.append(a) 

nc = countSpecialElements(matrix)
print(nc)