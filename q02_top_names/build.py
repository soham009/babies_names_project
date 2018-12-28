# %load q02_top_names/build.py
import pandas as pd
from collections import Counter
from greyatomlib.babies_names_project.q01_create_dict.build import q01_create_dict


path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q02_top_names(data):
    'write your solution here'
    dict1 = q01_create_dict(data)
    dict2 = Counter(dict1).most_common(25)
    return dict2, dict1

# q02_top_names(data)




