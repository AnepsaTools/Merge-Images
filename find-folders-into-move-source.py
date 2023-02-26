import os
import shutil

src_path = (r'')
dst_path = (r'')

for path, subdirs, files in os.walk(src_path):
    if len(subdirs) > 0:
        print(path)
        print(subdirs)


for file in os.listdir(src_path):
    shutil.move(os.path.join(src_path, file), dst_path)