from flask import Flask, url_for, render_template, request, redirect
from utils import convert
import os

app = Flask(__name__)

upload_folder = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
	if not 'image' in request.files:
		return redirect('/')

	file = request.files['image']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect('/')

	if file:
		filename = file.filename
		save_dir = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(save_dir)

		filename_processed = convert(app.config['UPLOAD_FOLDER'], filename)
		return render_template('index.html', filename='../' + filename_processed)
	
	return redirect('/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)