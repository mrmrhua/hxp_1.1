
from  flask import  jsonify
from flask_restful import Resource
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os
from  config import qiniu_access_key,qiniu_secret_key
import  json


class GetUpToken(Resource):
    def get(self):
        # 构建鉴权对象
        q = Auth(qiniu_access_key, qiniu_secret_key)
        # 回调策略
        # policy = {
        #     'callbackUrl': 'houxiaopang.com/qiniu/callback',
        #     'callbackBody': 'filename=$(fname)'
        # }
        # print(q)
        upToken = q.upload_token(bucket='designfile', key=None)
        # print(upToken)
        return jsonify({ 'uptoken':upToken })

