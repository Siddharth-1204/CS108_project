import pygame 

class Postgame :
    def __init__(self, background, screen, font, mm_logo, exit_logo):
        self.mm_logo_surf = mm_logo
        self.exit_surf = exit_logo
        self.mm_logo_rect = pygame.Surface.get_rect(self.mm_logo_surf, center = (350, 400))
        self.exit_rect = pygame.Surface.get_rect(self.exit_surf, center = (650, 400))
        self.background_surf = background
        self.screen = screen
        self.font = font
        self.is_active = False
        self.pressed = False
    def display(self):
        self.screen.blit(self.background_surf, (0, 0))
        self.screen.blit(self.mm_logo_surf, self.mm_logo_rect)
        self.screen.blit(self.exit_surf, self.exit_rect)
    def get_option(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.mm_logo_rect.collidepoint(mouse_pos):
            return "MM"
        if self.exit_rect.collidepoint(mouse_pos):
            return "Exit"
    def released(self):
        if pygame.mouse.get_pressed() == (True, False, False):
            return False
        return True