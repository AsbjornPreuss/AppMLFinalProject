# AUTHOR: Daniel Lomholt Christensen
# DATE: Spring 2024
# PURPOSE: Labelling of data for the final applied machine learning project
import matplotlib.pyplot as plt
import numpy as np
import time
import os

directory = input("Enter the directory in which all the csv files with images are kept: ")
start_index = int(input('Enter the starting index you are going to do: '))
fnames = sorted(os.listdir(directory))
categories = [[], []]
for file in fnames:
    if not file.endswith('.csv'):
        continue
    # Check split when Asbjørn gives me the files
    index = int(file.split('.')[0])
    # If the file is before the start index, skip it
    if index < start_index:
        continue
    # Every 20 files, ask the user if they wants to exit
    if index%10 == 0:
        exit = input("Write any string to not exit the program: ")
        if exit == "":
            break
    image = np.genfromtxt(directory + '/' + file, delimiter=',', ndmin=2).data
    category = "r"
    while category not in ['s','l','d', 'f', 'j', 'k']:
        print(index, start_index, file)
        plt.imshow(image, cmap='binary')
        plt.title(file)
        plt.show(block=False)
        plt.pause(2)
        plt.close()
        category = input('''s for reading errors,
d for muon (straight lines),
f for electron (Squiqqly lines),
j for X-rays(small dots),
k for other things,
l for multiple objects,
Any to repeat:\n''')
    categories[1].append(category)
    categories[0].append(index)
    
# Convert categories to numbers
def category_to_number(category):
    if category == 's':
        return 4
    if category == 'k':
        return 0
    if category == 'j':
        return 1
    if category == 'f':
        return 2
    if category == 'd':
        return 3
    if category == 'l':
        return 4
categories[1] = [category_to_number(category) for category in categories[1]]
categories = np.array(categories)
# Finally write the categories to a numpy file
np.save(f'./labels/categories_{categories[0,0]}_{categories[0,-1]}.npy', categories)




