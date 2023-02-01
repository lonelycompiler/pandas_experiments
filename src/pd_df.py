import pandas as pd
from data import *

df = pd.DataFrame(
        dict(names=names,ids=ids,roles=roles,ages=ages,companies=get_random_companies(), music=music,colors=favorite_colors,
             num_dogs=num_dogs,num_cats=num_cats,num_fish=num_fish)
)

names_s = pd.Series(names)
ids_s = pd.Series(ids)
roles_s = pd.Series(ids)
ages_s = pd.Series(ages)
companies_s = pd.Series(get_random_companies())
music_s = pd.Series(music)
colors_s = pd.Series(favorite_colors)
