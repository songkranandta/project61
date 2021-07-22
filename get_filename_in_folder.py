import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = "/videos"
path_name = ROOT_DIR+path

# for file_name in os.listdir(path_name):
#     print("filename:",file_name +"  path:",path_name)
name = 'Video_1623219056.avi'

list_name_myfolder = []
for file_name in os.listdir(path_name):
    if file_name < name:
        list_name_myfolder.__iadd__([file_name])


print(list_name_myfolder)