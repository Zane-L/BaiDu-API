# coding:utf-8
import os
import time
from BaiDu_API import baidu_api

def faces_register(group_name):
    group_path = "user_dir/" + group_name
    for root, dirs, files in os.walk(group_path, topdown=False):
        user_id = root.replace(group_path + '\\', '')
        # print(user_id)
        for name in files:
            img_path = os.path.join(root, name)
            base_64 = BD_API.imgToBase64(img_path)
            # QPS=2，设置0.6s注册一次
            res = BD_API.face_register(base_64, user_id)
            time.sleep(0.6)
            if res['error_code'] !=0:
                print("用户"+user_id+"照片上传失败，"+"{\'error_code\':"+str(res['error_code']) +";" +"  \'error_msg\':"+res['error_msg']+"}"
                      +"，文件位置："+ img_path)
            if name == files[-1]:
                print("用户"+user_id+"上传成功")


if __name__ == "__main__":

    group_name = "example_dir"
    # group_name = "face_train_data"
    BD_API = baidu_api.BaiDuAPI_Interface()
    # print(BD_API.access_token)
    faces_register(group_name)



















    # imgPath = r"C:\Users\lee\Pictures\lena.jpg"
    # imgPath = "hz.jpg"
    # result = json.loads(faceDetect(imgToBase64(imgPath)))['result']
    # face_list = result['face_list'][0]
    # location = face_list['location']
    # age = face_list['age']
    # beauty = face_list['beauty']
    # expression = face_list['expression']['type']
    # gender = face_list['gender']['type']
    #
    # img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
    # leftTopX = int(location['left'])
    # leftTopY = int(location['top'])
    # rightBottomX = int(leftTopX + int(location['width']))
    # rightBottomY = int(leftTopY + int(location['height']))
    # cv2.rectangle(img, (leftTopX, leftTopY), (rightBottomX, rightBottomY), (0, 255, 0), 2)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # # 第一个坐标表示起始位置
    # cv2.putText(img, "age:" + str(age), (0, 20), font, 0.5, (200, 255, 255), 1)
    # # cv2.putText(img, "gender:" + gender.encode("utf-8"), (0, 40), font, 0.5, (200, 255, 255), 1)
    # cv2.putText(img, "gender:" + gender, (0, 40), font, 0.5, (200, 255, 255), 1)
    #
    # cv2.putText(img, "beauty:" + str(beauty), (0, 60), font, 0.5, (200, 255, 255), 1)
    # cv2.putText(img, "expression:" + str(expression), (0, 80), font, 0.5, (200, 255, 255), 1)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    #
    # print("end")