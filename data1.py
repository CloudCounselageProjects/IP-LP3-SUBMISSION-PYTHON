import pandas as pd

df = pd.read_csv("C:\\Users\\hp\pratiksha.csv")
cd = df.to_csv(sep=',')
print(cd)
