import os
import sys 
import time

directory = sys.argv[1]
initial_list = os.listdir(directory)

while True:
    temp_list = os.listdir(directory)
    for item in temp_list:
        """ File addition detection """ 
        if item not in initial_list:
            print(f'New item {item} found, adding to the database!')
            initial_list.append(item)
            print("Database updated successfully.")
        """ File deletion detection """
        if item in initial_list and not in temp_list:
            print(f"Deletion of {item} detected.")
            initial_list.remove(item)
            print("Database updated successfully")
    
    time.sleep(30)
