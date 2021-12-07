import pygame

g = 0.5  #Ускорение свободного падения

wind_force = 1  #Сила ветра


def calculate_accelerations(obj):
    apply_wind_force(obj)
    apply_gravitational_force(obj)


def move_object(body, dt):
    """
    Перемещает тело
    """
    body.vx += body.ax * dt    #Обновляем параметры по оси 0х
    body.x += int( body.vx * dt + body.ax * dt**2 )

    body.vy += body.ay * dt  #Обновляем параметры по оси 0у
    body.y += int( body.vy * dt + body.ay * dt**2 )

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
