def pr(num):
    s1=num.find("not")
    s2=num.find("poor")


    if s2>s1 and s1>0 and s2>0:
        num1=num.replace(num[s1:(s2+4)],"good")
        return num1
    else:
        return num
print(pr("the lyrics not that poor"))