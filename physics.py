import pygame

g = 10  #Ускорение свободного падения

wind_force = 50


def move_objects(body, dt):
    """
    Перемещает тело
    """


    ax = wind_force / body.m
    body.x += ( body.Vx * dt + ax * dt**2 )
    body.Vx += ax*dt

    body.y += ( body.Vy * dt + g * dt**2 )
    body.Vy += g * dt



def recalculate_objects_positions(objects, dt):
    """Пересчитывает координаты объектов.
    **dt** — шаг по времени
    """

    for body in objects:
        move_objects(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
