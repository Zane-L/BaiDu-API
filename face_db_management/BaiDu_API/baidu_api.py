# coding:utf-8
import urllib.request, sys
import ssl
import json
import base64
import cv2
import requests

class BaiDuAPI_Interface:
    def __init__(self,group_id = "group_repeat"):
        self.AK = "yYF5N8TTagIwEggL1cQmrUth"
        # 你的应用Secret Key
        self.SK = "w9aGfod1qnstwjDcsmMvtz4cNFLrBX5z"
        self.access_token = self.getToken()
        self.group_id = group_id

    # 获取API的token
    def getToken(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=yYF5N8TTagIwEggL1cQmrUth&client_secret=w9aGfod1qnstwjDcsmMvtz4cNFLrBX5z'
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        if (content):
            token = json.loads(content)['access_token']
        return token


     # 人脸检测与属性分析
    def faceDetect(self,imgBase64):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        request_url = request_url + "?access_token=" + self.access_token
        request = urllib.request.Request(request_url)
        request.add_header('Content-Type', 'application/json')
        data = {"image": imgBase64, "image_type": "BASE64", "face_field": "age,beauty,expression,face_shape,gender","max_face_num":120}
        response = urllib.request.urlopen(request, urllib.parse.urlencode(data).encode("utf-8"))
        content = response.read()
        if content:
            # print(content)
            return content

    # 图片转换为base64编码
    def imgToBase64(self,imgPath):
        with open(imgPath, "rb") as f:  # 转为二进制格式
            base64_data = base64.b64encode(f.read())  # 使用base64进行加密
            # base64_data = str(base64.b64encode(f.read()))[2:]
            return base64_data
        # img = open("jt_ldh.jpg", "rb").read()
        # img64 = str(base64.b64encode(img))[2:]
        # return img64

    # 人脸注册
    def face_register(self,imgBase64,user_id,quality_control="NORMAL"):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add"
        params = {"image":imgBase64,"image_type":"BASE64","group_id":self.group_id,"user_id":user_id,"user_info":"student","quality_control":quality_control,"liveness_control":"NONE"}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            # print(response.json())
            return response.json()
    # 人脸删除
    def user_delet(self, user_id,face_token):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/delete"
        params = {"user_id":user_id,"group_id":self.group_id,"face_token":face_token}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            # print(response.json())
            return response.json()

        # 获取用户人脸列表
    def face_getlist(self,user_id):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/faceset/face/getlist"

        params = {"user_id":user_id,"group_id":self.group_id}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            # print(response.json())
            return response.json()

    # 人脸搜索
    def face_search(self,imgBase64):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
        params = {"image": imgBase64, "image_type": "BASE64", "group_id_list": "test_group",
                  "quality_control": "NONE", "liveness_control": "NONE"}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            # print(response.json())
            return response.json()