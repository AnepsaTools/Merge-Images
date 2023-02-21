import os
from PIL import Image

source_folder1 = 'logo/'
source_folder2 = 'qrs/'
target_folder = 'Image_Merged/'

n = len(os.listdir(source_folder1))

dir = os.listdir(source_folder1)
print(dir)

for img_no in range(1,n+1):
    img1 = source_folder1+str(img_no)+".png"
    img2 = source_folder2+str(img_no)+".png"
    
    images = [Image.open(x) for x in [img1, img2]]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))


    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save(target_folder+"/target_folder_"+str(img_no)+".png")