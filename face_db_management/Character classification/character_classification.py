import os
import shutil
import time
from BaiDu_API import baidu_api

if __name__ == '__main__':
    BD_API = baidu_api.BaiDuAPI_Interface("test2_group")
    # dir = "dir/0323am"
    dir = "dir/0323pm"
    # path = "dir/0323am/1616488431.jpg"
    i = 10000
    count = 0
    for root, dirs, files in os.walk(dir, topdown=True):
        for img in files:
            count += 1
            print("第 "+str(count)+" 张图片" )
            img_path = root+"/"+img
            img_64 = BD_API.imgToBase64(img_path)
            res1 = BD_API.face_search(img_64)
            time.sleep(0.5)
            # dir_path = "dir/02231913am"
            dir_path = "dir/02232146pm"
            # print(res1)
            if res1['result'] == None and res1['error_msg']=='pic not has face':
                continue
            elif res1['error_msg']=='match user is not found':
                # res3 = BD_API.face_getlist(str(i))

                res2 = BD_API.face_register(img_64,str(i),quality_control="NORMAL")
                print(res2)
                if res2['error_code'] == 0:
                    if os.path.exists(os.path.join(dir_path, str(i))):
                        shutil.copy(img_path, os.path.join(dir_path, str(i)))
                    else:
                        os.makedirs(os.path.join(dir_path, str(i)))
                        shutil.copy(img_path, os.path.join(dir_path, str(i)))
                        i = i+1
                time.sleep(0.3)
            else:
                score = res1['result']['user_list'][0]['score']
                if score <= 80:
                    res2 = BD_API.face_register(img_64, str(i), quality_control="HIGH")
                    # print(res2)
                    if res2['error_code'] == 0:
                        if os.path.exists(os.path.join(dir_path, str(i))):
                            shutil.copy(img_path, os.path.join(dir_path, str(i)))
                        else:
                            os.makedirs(os.path.join(dir_path, str(i)))
                            shutil.copy(img_path, os.path.join(dir_path, str(i)))
                            i += 1
                    time.sleep(0.3)

                    # print(res2)
                else:
                    user_id =res1['result']['user_list'][0]['user_id']
                    # print(user_id)
                    if os.path.exists(os.path.join(dir_path,user_id,img)):
                        print(user_id)
                        continue
                    else:
                        if os.path.exists(os.path.join(dir_path,user_id)):
                            shutil.copy(img_path, os.path.join(dir_path,user_id))
                        else:
                            os.makedirs(os.path.join(dir_path,user_id))
                            shutil.copy(img_path, os.path.join(dir_path,user_id))

                    # print(res1)