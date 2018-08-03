import UIHandler, pygame


class Button:
    def __init__(self, x, y, w, h, text):
        pygame.font.init()
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.SysFont('Verdana', 10)
        self.text_surface = self.font.render(str(text), True, (0, 0, 0))

    def on_click(self):
        print('Clicked!')

    def draw(self, display):
        display.blit(self.text_surface, (self.rect.x + 3, self.rect.y + 3))
        pygame.draw.rect(display, (0, 0, 0), self.rect, 2)
