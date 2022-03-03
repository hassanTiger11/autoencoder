import os
FOLDER_PATH = os.path.join(os.getcwd(), 'mutant_plots')
def change_folder_names():
    
    for f in os.listdir(FOLDER_PATH):
        folder = os.path.join(FOLDER_PATH, f)
        for chng_f in os.listdir(folder):
            new_folder_name = f'ds_{chng_f}'
            print(f'old: {chng_f}\nnew: {new_folder_name}')


def change_file_names():
    return

change_folder_names()