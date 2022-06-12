import pandas as pd

df = pd.read_csv('my_todolist.csv')

df['Done'] = df['Done'].replace(to_replace = False, value = True)
print(df['Done'])