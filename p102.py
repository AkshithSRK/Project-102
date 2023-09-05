import os
import shutil

from_dir = "C:/Users/akshi/Downloads/C102_assets-main/C102_assets-main"
to_dir = "C:/Users/akshi/Onedrive/Desktop/C0"
list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    
    if extension == "":
        continue
    if extension in [".gif",".png",".jfif",".jpeg",".jpg"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "image_files"
        path3 = to_dir + "/" + "image_files" + file_name 
        print(path2), print(path3)
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
    elif extension in [".txt",".doc",".pdf",".xlsx",".ppt"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "document_files"
        path3 = to_dir + "/" + "document_files" + file_name 
        print(path2), print(path3)
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)