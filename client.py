import os
import sys 
import time

directory = sys.argv[1]
initial_list = os.listdir(directory)

while True:
    temp_list = os.listdir(directory)
    for item in temp_list:
        if item not in initial_list:
            """ File addition detection """ 
            print(f'New item {item} found, adding to the database!')
            initial_list.append(item)
            print("Database updated successfully.")

    for item in initial_list:
        if item not in temp_list:
            """ File deletion detection """
            print(f"Deletion of {item} detected")
            initial_list.remove(item)
            print("Database updated successfully")
    
    time.sleep(15)
