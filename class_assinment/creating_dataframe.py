import pandas as pd
import numpy as np
details=['Neha bisht','MCA','B','45']

data = np.array([["Neha", 'MCA', 45], ['Nidi', "BBA", 16], ["Shivani", "MBA", 19]])

columns = ['Name', 'Cources', 'Roll_no']

df = pd.DataFrame(data, columns=columns)

print(df,"\n")

for i in details:
    print(i)