from data import *
from pd_df import df
import pandas as pd

#print(df.melt(id_vars=df.columns[1:3], var_name='Position', value_name='Value'))
print(df)
print('\n','---'*5,'\n')
df_pets = (
    df.melt(
        id_vars = df.columns[:7],
        value_name='num_pets',
    ignore_index=False)
)

df_pets = df_pets[(','.join(df_pets.columns[0:7]).split(','))+['num_pets']]

print(df_pets)
