s="ababacd"
output=" "
for ch in s:
    if ch not in output:
        output=output+ch
print(output)