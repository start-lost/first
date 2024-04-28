

import pandas as pd

l_connections = [
    {
        "user_name": "etl_user",
        "password": "123",
        "host": "192.168.1.1",
        "name": "Igor"
    },
    {
        "user_name": "test_user",
        "password": "456",
        "host": "8.8.8.8",
        "name": "Kolia"

    }
]

df1 = pd.DataFrame(l_connections)
print(df1)
print(type(df1))

df1.to_csv("from_pandas.csv") #, index=False

df2 = pd.read_csv("from_pandas.csv")
