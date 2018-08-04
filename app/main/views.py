import os
from . import main
from flask import render_template,request,redirect,url_for
from werkzeug.utils  import secure_filename
from app import config
import json
from pyocr import pyocr
from PIL import Image

#保存文件路径
UPLOAD_FOLDER='upload_file'
#获取view.py路径
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDERS=os.path.join(basedir,UPLOAD_FOLDER)
config["UPLOAD_FOLDER"]=UPLOAD_FOLDERS
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

#主页
@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

#智能分析页面
@main.route('/identification/',methods=['GET','POST'])
def identification():
    return render_template('identification.html')

#文件上传
@main.route('/img_upload/',methods=['GET','POST'])
def img_upload_file():

    if request.method=='POST':
        #接收前端上传的文件，img_file为imput标签的name
        file=request.files["file"]
        #读取文件名
        filename=secure_filename(file.filename)
        #保存文件
        file.save(os.path.join(config["UPLOAD_FOLDER"],filename))

        #识别图片
        # 查找OCR引擎
        tools = pyocr.get_available_tools()[:]
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        img_path=os.path.join(config["UPLOAD_FOLDER"],filename)
        ocr_name="Using '%s'" % (tools[0].get_name())
        ocr_data=tools[0].image_to_string(Image.open(img_path),lang='chi_sim')
        result={
            'ocr_name':ocr_name,
            'ocr_data':ocr_data,
        }
        #成功识别后删除图片
        if len(ocr_data)!=0:
            os.remove(img_path)
        return json.dumps(result)


@main.route('/show_img_test/',methods=['GET','POST'])
#返回识别内容
def show_img_test(data):
    result = data
    if request.method=='GET':
        return json.dumps(result)
    else:
        pass



