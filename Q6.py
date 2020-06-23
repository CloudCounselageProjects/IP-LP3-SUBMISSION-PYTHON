string=input()
if("not" in string):
    nt=string.index("not")
    if("poor" in string[nt:]):
        poor=string.index("poor")
        print(string[:nt] +"good" + string[poor+4:] )
else:
    print(string)