from PIL import Image
import os

path = 'qrs/'
resize_ratio = 0.5  # where 0.5 is half size, 2 is double size

def resize_aspect_fit():
    dirs = os.listdir(path)
    for item in dirs:
        if item == '.png':
            continue
        if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)

            image = image.resize((124, 124))
            image.save(file_path + "_small" + extension, 'PNG', quality=90)

resize_aspect_fit()