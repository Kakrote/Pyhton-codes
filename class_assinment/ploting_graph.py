import matplotlib.pyplot as plt
import csv
details=['Anshul','MCA','B','13']

try:
  with open('brnad.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)  
    data = list(reader)  # Read all rows into a list
  print(data,'\n')
  labels = [row[0] for row in data[1:]]  # Skip header row 
#   print(labels)
  values = [float(row[1]) for row in data[1:]]  
#   print(values)

  # Create the pie chart
  plt.pie(values, labels=labels, autopct="%1.1f%%")
  plt.title("Pie Chart of Brand Distribution (from brand.csv)")
  plt.show()


except FileNotFoundError:
  print("Error: CSV file 'brand.csv' not found.")
except csv.Error as e:
  print(f"Error reading CSV file: {e}")

for i in details:
  print(i)