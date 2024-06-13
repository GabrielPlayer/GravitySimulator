from __future__ import annotations
import pygame
import math

class Planet:
    AU = 149.6e6 * 1000
    G = 6.67e-11
    SCALE = 55 / AU
    TIMESTEP = 3600*24
    WIDTH = 800
    HEIGHT = 800
    SUN_RADIUS = 10
    TARGET_FRACTION_OF_WINDOW = 0.1
    VISUAL_SCALE = min(WIDTH, HEIGHT) * TARGET_FRACTION_OF_WINDOW / (SUN_RADIUS*3)

    def __init__(self, pos: tuple[int, int], mass: int, vel: tuple[int,int], color=(25,112,219)) -> None:
        """ pos in AU (earth is at 1 AU of the sun) is base on the center of the window\n
            mass in kg (earth mass is 6e26 and sun mass is 2e30)\n
            vel in km/s is the x and y base speed of the planet (earth is 29.29)
        """
        self.color = color
        self.pos = (pos[0]*self.AU, pos[1]*self.AU)
        self.mass = mass
        self.vel = (vel[0]*1000, vel[1]*1000)
        self.radius = self.SUN_RADIUS * (self.mass/2e30)**0.7 # TODO: find better way to define radius (here use star system only work for heavy planet)
        self.orbit = []

    def attraction(self, planet: Planet) -> tuple[float, float]:
        x,y = planet.pos[0]-self.pos[0],planet.pos[1]-self.pos[1]
        d = math.sqrt(x**2+y**2)
        force = self.G*(planet.mass*self.mass)/(d**2)
        theta = math.atan2(y,x)
        fX, fY = math.cos(theta) * force, math.sin(theta) * force
        return (fX, fY)

    def update(self, listPlanets: list[Planet]) -> None:
        totalForce = [sum(i) for i in zip(*[self.attraction(planet) for planet in listPlanets if planet!=self])]
        self.vel = (self.vel[0]+totalForce[0]/self.mass*self.TIMESTEP,
                    self.vel[1]+totalForce[1]/self.mass*self.TIMESTEP)
        self.pos = (self.pos[0]+self.vel[0]*self.TIMESTEP,
                    self.pos[1]+self.vel[1]*self.TIMESTEP)
        self.orbit.append(self.pos)

    def isClick(self, mousePos: tuple[int,int]) -> bool:
        windowPos = self.getWindowPos(self.pos)
        x,y = mousePos[0]-windowPos[0],mousePos[1]-windowPos[1]
        d = math.sqrt(x**2+y**2)
        return d <= self.radius*self.VISUAL_SCALE

    def getWindowPos(self, pos: tuple[int,int]) -> tuple[int, int]:
        return (pos[0] * self.SCALE + self.WIDTH / 2, pos[1] * self.SCALE + self.HEIGHT / 2)

    def draw(self, screen) -> None:
        x,y = self.getWindowPos(self.pos)
        if len(self.orbit) > 2:
            updatePoints = [(point[0]*self.SCALE+self.WIDTH/2,point[1]*self.SCALE+self.HEIGHT/2) for point in self.orbit]
            pygame.draw.lines(screen, self.color, False, updatePoints)
        pygame.draw.circle(screen, self.color, (x,y), self.radius*self.VISUAL_SCALE)