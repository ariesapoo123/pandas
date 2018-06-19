import pandas as pd

data = {'Name': ['Apoo', 'Anie'], 'Age': [20,21], 'Email id' : ['apoorvajai0@gmail.com', 'aniketkumar.ray@gmail.com'],\
        'PhoneNo':['9045287058','7017370671']}

df = pd.DataFrame(data)

print(df)