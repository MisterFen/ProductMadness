import pygame


class AbilityOverlay:

    def __init__(self, pos, ability):
        self.x, self.y = pos
        self.ability = ability
        self.time_active = 0
        self.max_time_active = 30

    def on_tick(self):
        self.time_active += 1


class AbilityUnreadyOverlay(AbilityOverlay):

    def get_surface(self):
        s = pygame.Surface((54, 54))
        s.set_alpha(80)
        s.fill((255, 0, 0))
        return s


class AbilityReadyOverlay(AbilityOverlay):
    img = pygame.image.load("art/ability_ready_overlay.png")

    def get_image(self):
        return self.img