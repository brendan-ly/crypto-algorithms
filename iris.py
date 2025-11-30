"""

Problem 1: Authenticate Using Iris Code (hamming distance)

Sources: 

Pandas for database: https://pandas.pydata.org/
Checking if Iris data csv file exists: https://www.geeksforgeeks.org/python/python-os-path-exists-method/

"""

import pandas as pd
import os

IRIS_DATA_FILE = "iris_data.csv"

if os.path.exists(IRIS_DATA_FILE):
    df = pd.read_csv(IRIS_DATA_FILE)
    iris_data = dict(zip(df['Name'], df['Iris Code']))
else:
    iris_data = {}
    df = pd.DataFrame(columns=['Name', 'Iris Code'])

def save_iris_data():
    df = pd.DataFrame(list(iris_data.items()), columns=['Name', 'Iris Code'])
    df.to_csv(IRIS_DATA_FILE, index=False)


option = int(input("Enter 1 or 2 for Enrollment/Recognition phase respectively: "))

match option:
  case 1: 
    while True:
      name = input("Enter your name: ")
      iris_input = input("Enter your iris code in hex: ")
      if name in iris_data.keys():
        print("You are already enrolled")
        break
      elif iris_input in iris_data.values():
        print("Matching iris data already in database, two people cannot have the same iris data.")
        break

      iris_data[name] = iris_input
      save_iris_data()
      print(f"{name}'s iris code has been saved to database.")
      choice = input("Enroll another person? (yes/no): ")
      if choice == 'no':
        break
  case 2:
    print("Recognition phase not done yet")
  case _:
    print("Invalid input")


