import pygame
from game.game import BigTwoGame
from ui.render import Renderer
from ui.input import InputHandler

class BigTwoApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.renderer = Renderer()
        self.input_handler = InputHandler(self.renderer)
        self.game = BigTwoGame()
        self.game.setup()
        self.buttons = {}

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.render()
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

    def render(self):
        self.screen.fill(self.renderer.COLORS['background'])
