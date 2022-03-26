from PIL import Image
import os
import numpy as np
from tensorflow import keras
save_procc_dir = 'static/processed'
IMG_SIZE = 120

def convert(save_dir, filename):
	image = Image.open(os.path.join(save_dir, filename))
	size = image.size
	image = image.resize((IMG_SIZE, IMG_SIZE)).convert('L')
	img_arr = np.array(image)[np.newaxis, :, :, np.newaxis] / 255.
	model = keras.models.load_model('gen.keras')
	colorized_img = (model(img_arr)[0] * 255.).numpy().astype('uint8')

	scaled_img = Image.fromarray(colorized_img).resize(size)
	scaled_img.save(os.path.join(save_procc_dir, filename))
	return save_procc_dir + '/' + filename

