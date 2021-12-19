from PIL import Image
import numpy as np
import pygame


def map_collision(obj, borders):
    collision=False
    b_x, b_y = np.shape(borders)[1]-1, np.shape(borders)[0]-1
    for i in range(max(obj.x-obj.r, 0),min(obj.x+obj.r, b_x)):
        for j in range(max(obj.y-obj.r, 0),min(obj.y+obj.r, b_y)):
            if((i-obj.x)**2+(j-obj.y)**2<=(obj.r-4)**2 and borders[j][i]==False):
                collision=True
    return collision


def check_traj(obj, dx, dy, borders):
    ret=False
    obj.x += dx
    obj.y += dy
    ret = map_collision(obj, borders)
    obj.x -= dx
    obj.y -= dy
    return ret


class Map():
    def __init__(self):
        self.name = None
        self.path = None
        self.borders = None
        self.image_mass = None
        self.map_image = None

    def image_to_mass(self, path):
        img = Image.open(path)
        self.image_mass = np.array(img)

    def detect_void(self):
        a = self.image_mass.sum(axis=2)
        a = a < 100
        self.borders = a

    def mass_to_image(self):
        pilImage = Image.fromarray(self.image_mass)
        self.map_image = pygame.image.fromstring(
            pilImage.tobytes(), pilImage.size, pilImage.mode)

    def create_map(self,path):
        self.image_to_mass(path)
        self.detect_void()
        self.mass_to_image()

    def remove_part_of_map(x, y, r, self):
        b_x, b_y = np.shape(self.borders)[1], np.shape(self.borders)[0]
        for i in range(max(0,x-r),min(x+r, b_x)):
            for j in range(max(0,y-r),min(y+r, b_y)):
                if((i-x)**2+(j-y)**2<=r**2):
                    self.borders[j][i]=True
                    self.image_mass[j][i] = [0, 0, 0]

    def draw_map(self, screen):
        screen.blit(self.map_image, (0, 0))


if __name__ == "__main__":
    print("This module is not for direct call!")