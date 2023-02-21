import os

os.getcwd()

path = "qrs/"

for i, filename in enumerate(os.listdir(path)):
    os.rename(os.path.join(path, filename), os.path.join(path, str(i) + ".png"))

