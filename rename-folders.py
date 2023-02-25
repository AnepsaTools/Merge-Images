import os 

path = os.listdir('123')
print(path)

def rename_folder(path):
    for folder in os.listdir(path):
        while len(folder) < 6:
            os.rename(path + '/' + folder, path + '/' + "0" + folder)
            folder = "0" + folder
        print(folder)

rename_folder('123')