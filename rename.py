from os import listdir, rename
from os.path import isfile, join

mypath = "oldmen"
oldMenFilenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i, filename in enumerate(oldMenFilenames):
  fileExtension = filename.split(".")[1]
  newFilename = str(i) + '.png'
  rename(f'./oldmen/{filename}', f'./oldmen/{newFilename}')



