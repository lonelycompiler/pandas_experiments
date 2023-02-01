from data import *
companies = [all_companies[randint(0,len(all_companies)-1)] for i in range(num_people)]

d1 = dict(names=names,ids=ids,roles=roles,ages=ages,companies=companies)
df = pd.DataFrame(d1)

print(df.melt(id_vars=df.columns[1:3], var_name='Position', value_name='Value'))
