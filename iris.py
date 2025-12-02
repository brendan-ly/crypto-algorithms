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

option = int(input("Enter 1 to enroll, 2 to authenticate, 3 to delete a user's iris data: "))

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
    while True:
        name = input("Enter your name: ")
        iris_input = input("Enter your iris code you are trying to authenicate in hex: ")
        if name not in iris_data.keys():
            print("You are not enrolled yet, please do that before entering recognition phase")
            break
        given_iris = iris_data[name]
        
        bit_len = len(iris_input)*4
        input_bin = bin(int(iris_input,16))[2:].zfill(bit_len)
        
        given_bit_len = len(given_iris)*4
        given_bin = bin(int(given_iris,16))[2:].zfill(given_bit_len)
        
        if (bit_len == given_bit_len):
            count = 0
            comp_list = list(zip(input_bin, given_bin))
            ham = 0
            for x in comp_list:
                if (x[0] != x[1]):
                    count = count + 1
                    print(input_bin)
                    print(given_bin)
                    
                    ham = (count/bit_len)
                    print(ham)

            if ham < 0.32:
                print("Recognition successful")
            else:
                print("Recognition failed")

            choice = input("Would you like to do another recognition? (yes/no): ")
            if choice == 'no':
                break
        else:
            print("ERROR: wrong sized input given")
            break
  case 3:
    name = input("Enter the name of the user you want to delete iris data of: ")
    if name in iris_data:
        del iris_data[name]
        save_iris_data()
        print(f"{name}'s iris data has been deleted.")
    else:
        print("User not found.")
  case _:
    print("Invalid input")

