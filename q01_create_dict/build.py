# %load q01_create_dict/build.py
import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q01_create_dict(data):
    'write your solution here'

    dictionary = {'Name':data['Name'],
                 'Count':data['Count']}
    return dictionary

# q01_create_dict(data)



