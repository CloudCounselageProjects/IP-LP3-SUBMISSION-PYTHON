n=input()
notwr=n.find('not')
poorwr=n.find('poor')+4
if notwr<poorwr and notwr>0 and poorwr>0:
	word=n.replace(n[notwr:poorwr],'good')
else:
	word=n
print(word)