n=str(input())
output=''
for ch in n:
    if ch not in output:
        output=output+ch
print(output)