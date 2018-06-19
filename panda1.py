import pandas as pd

data = {'Name': ['Apoo', 'Anie'], 'Age': [20,21], 'Email id' : ['apoorvajai0@gmail.com', 'aniketkumar.ray@gmail.com'],\
        'PhoneNo':['9045287058','7017370671']}

df = pd.DataFrame(data)

print(df)


output


  Name  Age                   Email id     PhoneNo
0  Apoo   20      apoorvajai0@gmail.com  9045287058
1  Anie   21  aniketkumar.ray@gmail.com  7017370671
