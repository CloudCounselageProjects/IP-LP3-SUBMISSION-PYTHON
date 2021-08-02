import pandas as pd

df = pd.read_csv("C:\\Users\\hp\pratu.csv")
cd = df.to_csv(sep='\t')
print(cd)
