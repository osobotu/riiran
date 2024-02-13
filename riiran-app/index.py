from flask import (
    Blueprint, current_app, flash, g, jsonify, redirect, render_template, request, session, url_for
)
import os
from werkzeug.utils import secure_filename

bp = Blueprint('index', __name__, url_prefix='/')


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/', methods=['GET'])
def index():
    return render_template('/index.html')

@bp.route('/upload', methods=['POST'])
def upload_image():
    if 'braille-image' not in request.files:
        return render_template('index.html', error='No braille-image part')

    file = request.files['braille-image']

    if file.filename == '':
        return render_template('index.html', error='No image uploaded')


    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        file.save(file_path)
        
        image_url = url_for('static', filename='uploads/' + filename)
        return jsonify({'message': 'File uploaded successfully', 'image_url': image_url})
    else:
        formats = ','.join(ALLOWED_EXTENSIONS)
        return  jsonify({'message': 'Allowed formats: ' + formats, 'image_url': image_url})
    

