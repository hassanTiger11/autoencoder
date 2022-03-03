import os
FOLDER_PATH = os.path.join(os.getcwd(), 'mutant_plots')
def change_folder_names():
    
    for f in os.listdir(FOLDER_PATH):
        folder = os.path.join(FOLDER_PATH, f)
        for chng_f in os.listdir(folder):
            old_folder_name = os.path.join(folder, chng_f)
            new_folder_name =  os.path.join(folder, f'ds_{chng_f}')
            os.rename(old_folder_name, new_folder_name)
            for img in new_folder_name:
                old_img_name = os.path.join(new_folder_name, img)
                new_img_name = os.path.join(new_folder_name, f'img_{img}')
                os.rename(old_img_name, new_img_name)


def change_file_names():
    return

change_folder_names()