import os

path = os.listdir('Image_Merged')

def rename_images(path):
    for file in os.listdir(path):
        while len(file) < 11:
            os.rename(path + '/' + file, path + '/' + "0" + file)
            file = "0" + file
        print(file)

rename_images('Image_Merged')