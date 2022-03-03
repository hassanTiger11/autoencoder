import os
FOLDER_PATH = os.path.join(os.getcwd(), 'mutant_plots')
def change_folder_names():
    
    folder = open(FOLDER_PATH, 'w+')
    for f in os.listdir(FOLDER_PATH):
        print(f)

def change_file_names():
    return

change_folder_names()