import os
FOLDER_PATH = os.path.join(os.getcwd(), 'mutant_plots')
def change_folder_names(FOLDER_PATH = ''):
    
    for f in os.listdir(FOLDER_PATH):
        folder = os.path.join(FOLDER_PATH, f)
        for chng_f in os.listdir(folder):
            if (not chng_f.startswith('ds_')): 

                old_folder_name = os.path.join(folder, chng_f)
                new_folder_name =  os.path.join(folder, f'ds_{chng_f}')
                print(f'#chnge folder {old_folder_name} -> {new_folder_name}')
                os.rename(old_folder_name, new_folder_name)
                change_file_names(new_folder_name = new_folder_name)
            


def change_file_names(new_folder_name = ''):
    for img in os.listdir(new_folder_name):
                if (not img.startswith('img_')): 
                    old_img_name = os.path.join(new_folder_name, img)
                    new_img_name = os.path.join(new_folder_name, f'img_{img}')
                    print(f'#chnge img {old_img_name} -> {new_img_name}')
                    os.rename(old_img_name, new_img_name)
    



change_folder_names(FOLDER_PATH = FOLDER_PATH)