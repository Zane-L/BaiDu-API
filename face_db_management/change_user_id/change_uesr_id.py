import os
BASE_DIR = os.path.abspath(__file__)
path = os.path.join(BASE_DIR,"..","user_register/user_dir/face_train_data")

name_id_dict = {}   # 名字和学号对应的字典
with open('1111.csv','r') as f:
    for line in f.readlines():
        tem = line.split(',')
        # 读取每一行前两个数据[x,y]
        data = [tem[x] for x in range(len(tem)) if x < 2]
        #添加到字典列表
        name_id_dict[data[0]] = data[1]
print(name_id_dict)


path = "../user_register/user_dir/face_train_data"
# name_list = []
for root, dirs, files in os.walk(path, topdown=True):
    # print(dirs)
    # if len(dirs) != 0:
    #     name_list = dirs
    for name in dirs:
        oldpath = os.path.join(root, name)
        newpath = os.path.join(root, name_id_dict[name])
        os.rename(oldpath,newpath)
        # os.r
        print(oldpath,newpath)
# print(name_list)

# dir_list = os.listdir(path)
# print(dir_list)



