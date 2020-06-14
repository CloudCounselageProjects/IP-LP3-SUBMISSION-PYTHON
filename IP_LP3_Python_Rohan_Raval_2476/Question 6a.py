
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


def slicing(a,step):
    return [a[i::step] for i in range(step)]


matrixx = []
print("Enter the Elements Row Wise: ")

# For user input
a=[]
for i in range(3):          # A for loop for row entries
    
    for j in range(3):      # A for loop for column entries
        a.append(int(input()))
    matrixx.append(a)
mat=slicing(a,3)
print(mat)


if __name__ == '__main__':
  nCount = countSpecialElements(mat)
  print(nCount)
  



"""
OUTPUT:

Enter the Elements Row Wise:                    #user input

1

5

8

3

2

7

4

9

6
[[1, 3, 4], [5, 2, 9], [8, 7, 6]]               #output
7

"""



