from flask import Blueprint, request
from src.utils import resp, utils
from flask import Flask, request
from werkzeug.utils import secure_filename  # 获取上传文件的文件名
import os
import time

gl_upload = Blueprint('upload', __name__, url_prefix='/upload')

UPLOAD_FOLDER = r'D:\website\commonStatic'  # 上传路径
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])  # 允许上传的文件类型


@gl_upload.route('/<string:folder>', methods=['post'])
def upload_folder(folder):
    file = request.files['file']  # 获取上传的文件
    if file and allowed_file(file.filename):  # 如果文件存在并且符合要求则为 true
        filename = secure_filename(file.filename)  # 获取上传文件的文件名
        uploadFileName = time.strftime('%Y%m%d%H%M%S%F', time.localtime())[0:17] + '.' + filename.rsplit('.', 1)[1]
        uploadAddress = UPLOAD_FOLDER + '\\' + folder
        if not os.path.exists(uploadAddress):
            os.mkdir(uploadAddress)
        file.save(os.path.join(uploadAddress, uploadFileName))  # 保存文件
        return resp.resp_succ(folder + '/' + uploadFileName, '上传成功')  # 返回保存成功的信息
    # 使用 GET 方式请求页面时或是上传文件失败时返回上传文件的表单页面
    return resp.resp_fail({}, '上传失败')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
