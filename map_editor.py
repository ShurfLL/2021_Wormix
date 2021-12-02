import numpy as np
from PIL import Image


def image_to_mass(path, w, h):
	img = Image.open(path)
	img.save(path, dpi=(w,h))
	img_1=Image.open(path)
	return np.array(img)


def detect_borders(mass):
    a = mass.sum(axis=2)
    space = a<15
    return space


def mass_to_txt(mass, path):
	file = open(path, 'w')
	for line in mass:
		for element in line:
			print(element, file=file)
	file.close()


#print(image_to_mass('maps/3flour22.jpg'))
mass_to_txt(detect_borders(image_to_mass('maps/3flour22.jpg', 1400, 600)), 'maps/map.txt')