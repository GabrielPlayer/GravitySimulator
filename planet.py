from __future__ import annotations
import pygame

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67e-11
    SCALE = 40 / AU
    TIMESTEP = 3600*24
    WIDTH = 800
    HEIGHT = 800

    def __init__(self, pos: tuple[int, int], mass: int, vel: tuple[int,int], color=(25,112,219)) -> None:
        """ pos is base on the center of the window\n
            mass in kg (earth mass is 6e26 and sun mass is 2e30)\n
            vel is the x and y base speed of the planet
        """
        self.color = color
        self.pos = pos
        self.mass = mass
        self.vel = vel
        self.radius = 5 # TODO: add radius base on the mass and the window's scale

    def draw(self, screen) -> None:
        x = self.pos[0] * self.SCALE + self.WIDTH / 2
        y = self.pos[1] * self.SCALE + self.HEIGHT / 2
        pygame.draw.circle(screen, self.color, (x,y), self.radius)