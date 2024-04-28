import pandas as pd
import numpy as np
details=['Anshul','MCA','B','13']

data = np.array([["Anshul", 'MCA', 13], ['Aman', "BBA", 16], ["NIkhil", "MBA", 19]])

columns = ['Name', 'Cources', 'Roll_no']

df = pd.DataFrame(data, columns=columns)

print(df,"\n")

for i in details:
    print(i)