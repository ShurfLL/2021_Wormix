import pygame

g = 10  #Ускорение свободного падения

wind_force = 10  #Сила ветра
wind_direct = 1  #Напревление ветра (определяется знаком)

def move_objects(body, dt):
    """
    Перемещает тело
    """
    body.ax = 0
    body.ay = 0

    wind_force(body)
    gravitational_force(body)

    body.Vx += body.ax * dt    #Обновляем параметры по оси 0х
    body.x += ( body.Vx * dt + ax * dt**2 )

    body.Vy += body.ay * dt  #Обновляем параметры по оси 0у
    body.y += ( body.Vy * dt + ay * dt**2 )

def wind_force(body):
    if wind_direct * body.Vx > 0:
        body.ax += wind_force / body.m
    body.ax -= wind_force / body.m

def gravitational_force(body):
    body.ay += g

def recalculate_objects_positions(objects, dt):
    """Пересчитывает координаты объектов.
    **dt** — шаг по времени
    """

    for body in objects:
        move_objects(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
