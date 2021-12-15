import pygame
from map_editor import map_collision

g = 0.5  #Ускорение свободного падения

wind_force = 0  #Сила ветра


def sign(x):
    if x>0:
        return 1
    if x<0:
        return -1
    return 0


def calculate_accelerations(obj):
    apply_wind_force(obj)
    apply_gravitational_force(obj)


def move_object(body, dt, borders):
    """
    Перемещает тело
    """
    body.vx += body.ax * dt   #Обновляем параметры по оси 0х
    for i in range (0, int( body.vx * dt + body.ax * dt**2 )):
        body.x += sign(body.vx)
        if map_collision(body, borders):
            body.vx, body.vy, body.ax, body.ay = 0, 0, 0, 0
            body.x -= 3*sign(body.vx)
            break

    
    body.vy += body.ay * dt  #Обновляем параметры по оси 0у
    for i in range (0, int( body.vy * dt + body.ay * dt**2 )):
        body.y += sign(body.vy)
        if map_collision(body, borders):
            body.vx, body.vy, body.ax, body.ay = 0, 0, 0, 0
            body.y -= 3*sign(body.vy)
            break
    
    body.ax = 0
    body.ay = 0

def apply_wind_force(body):
    body.ax += wind_force / body.m


def apply_gravitational_force(body):
    body.ay += g

def recalculate_objects_positions(objects, dt):
    """Пересчитывает координаты объектов.
    **dt** — шаг по времени
    """

    for body in objects:
        move_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
