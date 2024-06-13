import pygame
from random import randint
from planet import Planet

class Main:
    def __init__(self):
        pygame.init()
        self.screenSize = (800,800)
        self.FPS = 60

        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock, self.dt = pygame.time.Clock(), 0

        self.planetsGroup: list[Planet] = []
        self.planetsGroup.append(Planet(pos=(0,0), mass=2e30, vel=(0,0), color=(200,0,100)))
        self.planetsGroup.append(Planet(pos=(-1,0), mass=6e26, vel=(0,29.29), color=(25,112,219)))
        self.planetsGroup.append(Planet(pos=(0.5,0), mass=6e26, vel=(0,29.78), color=(0,200,100)))
        self.planetsGroup.append(Planet(pos=(1.3,0), mass=6e29, vel=(0,-30.78), color=(100,0,100)))

        self.backgroundColor = (0,0,0)
        self.isRun = False

    def createPlanet(self) -> None:
        mouseCoords = pygame.mouse.get_pos()
        pos = ((mouseCoords[0]/Planet.SCALE-Planet.WIDTH/(2*Planet.SCALE))/Planet.AU,
               (mouseCoords[1]/Planet.SCALE-Planet.HEIGHT/(2*Planet.SCALE))/Planet.AU)
        mass = 6e29 #TODO: add keyboard input
        vel = (randint(-10,10),randint(-10,10))
        color = (randint(0,255), randint(0,255), randint(0,255))
        self.planetsGroup.append(Planet(pos=pos, mass=mass, vel=vel, color=color))

    def deletePlanet(self) -> None:
        mouseCoords = pygame.mouse.get_pos()
        for i,planet in enumerate(self.planetsGroup):
            if planet.isClick(mouseCoords):
                del self.planetsGroup[i]
                return

    def zoomIn(self) -> None:
        #TODO: change the scale var of Planet class base on mouse scroll
        pass

    def zoomOut(self) -> None:
        #TODO: change the scale var of Planet class base on mouse scroll
        pass

    def mouveCamera(self) -> None:
        #TODO: move the camera with the arrows keys
        pass

    def run(self):
        self.isRun = True
        while self.isRun:
            self.screen.fill(self.backgroundColor)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.isRun = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: #left click
                        self.createPlanet()
                    elif event.type == 3: #right click
                        self.deletePlanet()
                    elif event.type == 4: #scroll up
                        self.zoomIn()
                    elif event.type == 5: #scroll down
                        self.zoomOut()

            for p in self.planetsGroup:
                p.update(self.planetsGroup)

            for p in self.planetsGroup:
                p.draw(self.screen)

            pygame.display.update()
            self.clock.tick(self.FPS)
            pygame.display.set_caption(str(int(self.clock.get_fps())))

if __name__ == "__main__":
    main = Main()
    main.run()
    pygame.quit()