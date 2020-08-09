""" Resize & Rotate all images files of a directory"""

from PIL import Image
import os

op_dir='/opt/icons/'
in_dir='/home/student-04-d68dc73fe1be/images/'

for i in os.listdir(in_dir):
	if i.startswith('ic'):
		file=in_dir+i
		im=Image.open(file)
		im.convert("RGB").refsize((128,128)).rotate(90).save(op_dir+i+'.jpeg')