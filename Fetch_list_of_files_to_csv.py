#!/usr/bin/env python3

import os
import csv

# change the path to the folder where you want the csv file to be saved and the path to copy files to csv file.
os.chdir('/path/to/the/folder')

print("Opening csv file ")

with open('csv_file_to_write.csv','w+') as file:
    writer = csv.writer(file)
    
    # you can even mention path of the folder where you want to perform the operation.
    file_name = os.listdir()
    
    for name in file_name:
        writer.writerow([name])
        
file.close()
print("Closing file")
############################# END #############################
