import numpy as np
from PIL import Image


def image_to_mass(path):
	img = Image.open(path)
	return np.array(img)


def detect_void(mass):
    a = mass.sum(axis=2)
    return a < 100


def mass_to_txt(mass, path):
	file = open(path, 'w')
	for line in mass:
		for element in line:
			file.write(str(element)+' ')
		file.write('\n')
	file.close()


def map_collision(obj, borders):
	collision=False
	b_x, b_y = np.shape(borders)[1]-1, np.shape(borders)[0]-1
	for i in range(max(obj.x-obj.r, 0),min(obj.x+obj.r, b_x)):
		for j in range(max(obj.y-obj.r, 0),min(obj.y+obj.r, b_y)):
			if((i-obj.x)**2+(j-obj.y)**2<=obj.r**2 and borders[j][i]==False):
				collision=True
	return collision


def remove_part_of_map(x, y, r, borders, image_mass):
	b_x, b_y = np.shape(borders)[1], np.shape(borders)[0]
	print(b_x, b_y)
	for i in range(max(0,x-r),min(x+r, b_x)):
		for j in range(max(0,y-r),min(y+r, b_y)):
			if((i-x)**2+(j-y)**2<=r**2):
				borders[j][i]=False
				image_mass[j][i] = [0, 0, 0]


def check_traj(obj, dx, dy, borders):
	ret=False
	obj.x += dx
	obj.y += dy
	ret = map_collision(obj, borders)
	obj.x -= dx
	obj.y -= dy
	return ret



image_mass = image_to_mass('maps/map1.jpg')
borders=detect_void(image_mass)
#remove_part_of_map(1300,600,1000,borders,image_mass)
#mass_to_txt(image_mass, 'maps/map.txt')