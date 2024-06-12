import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screenSize = (800,800)
        self.FPS = 60

        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock, self.dt = pygame.time.Clock(), 0

        self.backgroundColor = (0,0,0)
        self.isRun = False

    def run(self):
        self.isRun = True
        while self.isRun:
            self.screen.fill(self.backgroundColor)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.isRun = False

            pygame.display.update()
            self.clock.tick(self.FPS)
            pygame.display.set_caption(str(int(self.clock.get_fps())))

if __name__ == "__main__":
    main = Main()
    main.run()
    pygame.quit()