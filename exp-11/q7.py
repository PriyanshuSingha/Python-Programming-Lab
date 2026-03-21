import pandas as pd
data={
    'name':['alice','bob','charlie'],
    'age':[25,30,35],
    'city':['new york','san francisco','los angeles']
}
df=pd.DataFrame(data)
print("Dataframe:")
print(df)
print("\n age column:")
print(df['age'])
print('\n row at index 1:')
print(df.iloc[1])