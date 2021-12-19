""""Модуль физики используется для описания движения тел под внешним воздействием

Основное применение - изменение параметров тел (координат, скоростей и ускорений).

Functions
----------
sign()
    Обрабатывает число и выдаёт его знак,
    используется для определения направления движения
calculate_accelerations()
    Вызывает другие функции пересчёта ускорений
move_object()
    Принимает на вход объект и производит изменения его параметров
apply_wind_force()
    Обновляет ускорение объекта, связанное с ветром
apply_gravitational_force()
    Обновляет ускорение объекта, связанное с гравитацией
recalculate_objects_positions()
    Получает на вход список объектов для обновления их параметров
    и обращается с ними к функции move_object()
"""

import pygame
from map_editor import map_collision

g = 0.5  #Ускорение свободного падения

wind_force = 0  #Сила ветра


def sign(x):
    """Определяет направление движения."""
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def calculate_accelerations(obj):
    """Обращается ко всем функциям для пересчёта ускорения."""
    apply_wind_force(obj)
    apply_gravitational_force(obj)


def move_object(body, dt, borders):
    """Перемещает тело."""
    body.vx += body.ax * dt
    for i in range(0, int(body.vx * dt + body.ax * dt**2)):
        body.x += sign(body.vx)
        if map_collision(body, borders):
            body.vx, body.vy, body.ax, body.ay = 0, 0, 0, 0
            body.x -= 3*sign(body.vx)
            break

    body.vy += body.ay * dt
    for i in range(0, int(body.vy * dt + body.ay * dt**2)):
        body.y += sign(body.vy)
        if map_collision(body, borders):
            body.vx, body.vy, body.ax, body.ay = 0, 0, 0, 0
            body.y -= 3*sign(body.vy)
            break
    
    body.ax = 0
    body.ay = 0

def apply_wind_force(body):
    """Обновляет ускорение, связанное с ветром"""
    body.ax += wind_force / body.m


def apply_gravitational_force(body):
    """Обновляет ускорение, связанное с гравитацией"""
    body.ay += g

def recalculate_objects_positions(objects, dt):
    """Пересчитывает координаты объектов.
    **dt** — шаг по времени
    """
    for body in objects:
        move_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
