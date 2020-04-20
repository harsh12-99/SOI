from flask import Flask,send_from_directory
from flask import request,redirect,render_template,url_for
from object_size import process
from werkzeug.utils import secure_filename
import os
from PIL import ImageFilter
from PIL import Image
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './media'

@app.route('/')
def index():
    return render_template('index.html')

#Function to convert image to text.
@app.route('/success',methods=['POST', 'GET'])
def success():
    image = request.files['image']
    fn = (image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], '1.jpg'))
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], '1.jpg'))
    width = request.form['width']
    result = process(img,width)
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(debug=True)
    #'0.0.0.0',8000
    app.run(host='127.0.0.1',port =5000,debug=True)