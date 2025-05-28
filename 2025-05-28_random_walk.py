import pygame
import random

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([640, 480])
        self.x = self.screen.get_width() / 2
        self.y = self.screen.get_height() / 2
        self.run()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # self.screen.fill((0,0,0))
            color = random.choice([(255,0,0), (0,255,0), (0,0,255), (255,255,0), (0,255,255),(255,0,255)])
            self.x += random.random() - 0.5
            self.y += random.random() - 0.5
            pygame.draw.circle(self.screen,color ,[self.x,self.y], 2)
            pygame.display.update()

if __name__ == '__main__':
    App()