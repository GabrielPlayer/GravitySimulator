import pygame
from random import randint
from planet import Planet

class Main:
    SCROLL_SPEED = 5
    CAMERA_SPEED = 5

    def __init__(self):
        pygame.init()
        self.screenSize = (800,800)
        self.FPS = 60

        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock, self.dt = pygame.time.Clock(), 0

        self.cameraControl = {pygame.K_UP: (1,1),
                              pygame.K_DOWN: (1,-1),
                              pygame.K_LEFT: (0,1),
                              pygame.K_RIGHT: (0,-1)}
        self.keyPressed = {}

        self.planetsGroup: list[Planet] = []
        self.planetsGroup.append(Planet(pos=(0,0), mass=2e30, vel=(0,0), color=(200,0,100)))
        self.planetsGroup.append(Planet(pos=(-1,0), mass=6e26, vel=(0,29.29), color=(25,112,219)))
        self.planetsGroup.append(Planet(pos=(0.5,0), mass=6e26, vel=(0,29.78), color=(0,200,100)))
        self.planetsGroup.append(Planet(pos=(1.3,0), mass=6e29, vel=(0,-30.78), color=(100,0,100)))

        self.backgroundColor = (0,0,0)
        self.isPause = False
        self.isRun = False

    def calculPlanetPos(self, pos: tuple[int,int]) -> tuple[int,int]:
        return ((pos[0]/Planet.SCALE-Planet.WIDTH/(2*Planet.SCALE))/Planet.AU,
               (pos[1]/Planet.SCALE-Planet.HEIGHT/(2*Planet.SCALE))/Planet.AU)

    def createPlanet(self) -> None:
        mouseCoords = pygame.mouse.get_pos()
        pos = self.calculPlanetPos(mouseCoords)
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
        Planet.SCALE += self.SCROLL_SPEED / Planet.AU

    def zoomOut(self) -> None:
        Planet.SCALE -= self.SCROLL_SPEED / Planet.AU if Planet.SCALE > self.SCROLL_SPEED / Planet.AU else 0

    def mouveCamera(self, axe: int, direction: int) -> None:
        updateTuple = lambda t,a,d: (t[0]+d*self.CAMERA_SPEED, t[1]) if a == 0 else (t[0], t[1]+d*self.CAMERA_SPEED)
        for planet in self.planetsGroup:
            planet.pos = tuple(map(lambda c: c*Planet.AU, self.calculPlanetPos(updateTuple(planet.getWindowPos(planet.pos), axe, direction))))
            planet.orbit = [tuple(map(lambda c: c*Planet.AU, self.calculPlanetPos(updateTuple(planet.getWindowPos(orb), axe, direction)))) for orb in planet.orbit]

    def pause(self) -> None:
        self.isPause = not self.isPause
        if self.isPause:
            Planet.TIMESTEP = 0
        else:
            Planet.TIMESTEP = 3600*24

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
                    elif event.button == 3: #right click
                        self.deletePlanet()
                    elif event.button == 4: #scroll up
                        self.zoomIn()
                    elif event.button == 5: #scroll down
                        self.zoomOut()
                elif event.type == pygame.KEYDOWN:
                    self.keyPressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        self.pause()
                elif event.type == pygame.KEYUP:
                    self.keyPressed[event.key] = False

            for k in self.cameraControl.keys():
                if self.keyPressed.get(k):
                    axe,direction = self.cameraControl.get(k)
                    self.mouveCamera(axe, direction)

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