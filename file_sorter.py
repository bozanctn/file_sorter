import os 
import shutil

path = r"Your path"

file_name = os.listdir(path)

folder_names = ['csv files', 'mp4 files', 'jpg files']

for loop in range(0,3):
   if not  os.path.exists(path + folder_names[loop]):
        print(path + " " + folder_names[loop])
        os.makedirs(path + " " + folder_names[loop])

for file in file_name:
   if ".csv" in file and not os.path.exists(path + " csv files/" + file):
       shutil.move(path + file, path + " csv files/" + file)
   elif ".jpg" in file and not os.path.exists(path + " jpg files/" + file):
      shutil.move(path + file, path + " jpg files/" + file)
   elif ".mp4" in file and not os.path.exists(path + " mp4 files/" + file):
       shutil.move(path + file, path + " mp4 files/" + file)
   else:
       print("THere are files in this path that were not moved!")