

temp = input("Input temperature ")
degree = int(temp[:-1])
initial = temp[-1]

if initial.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  print(temp,"is",result,"in Farhenheit")
elif initial.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  print(temp,"is",result,"in Celsius")
else:
  print("Input correct temperature")
  quit()

