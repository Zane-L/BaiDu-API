import os
import time
from BaiDu_API import baidu_api


def user_delete(group_name):
    group_path = "user_id_dir/" + group_name
    for root, dirs, files in os.walk(group_path, topdown=True):
        for user_id in dirs:
            res = BD_API.face_getlist(user_id)
            if res['error_code'] == 0:
                face_list = res['result']['face_list']
                for face in face_list:
                    # print(face['face_token'])
                    del_res = BD_API.user_delet(user_id,face['face_token'])
                    if face == face_list[-1] and del_res['error_code'] == 0:
                        print("用户"+user_id+"删除成功")

            else:
                print("用户"+user_id+"删除失败: ","\'error_msg\': "+ res['error_msg'])



if __name__ == '__main__':

    group_name = "example_dir"
    # group_name = "face_train_data"
    BD_API = baidu_api.BaiDuAPI_Interface("group_repeat")
    # print(BD_API.access_token)
    user_delete(group_name)
