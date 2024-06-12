import pygame
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

    def createPlanet(self):
        #TODO: create planet on right click and ask for mass with numpad input
        pass

    def deletePlanet(self):
        #TODO: delete planet on left click
        pass

    def zoom(self):
        #TODO: change the scale var of Planet class base on mouse scroll
        pass

    def run(self):
        self.isRun = True
        while self.isRun:
            self.screen.fill(self.backgroundColor)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.isRun = False

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