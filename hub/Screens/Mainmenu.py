import pygame

class MainMenu :
    def __init__(self, background_photo, ttt_logo, othello_logo, connectfour_logo, screen):
        self.screen = screen
        self.background_surf = background_photo
        self.ttt_surf = ttt_logo
        self.othello_surf = othello_logo
        self.connectfour_surf = connectfour_logo
        self.ttt_rect = self.ttt_surf.get_rect(center=(200, 550))
        self.othello_rect = self.othello_surf.get_rect(center=(500, 550))
        self.connectfour_rect = self.connectfour_surf.get_rect(center=(800, 550))
        self.mainmenu_txt_font = pygame.font.Font(None, 100)
        self.mainmenu_message_surf = self.mainmenu_txt_font.render('Main Menu',False,(64, 64, 64))
        self.selectagame_message_surf = self.mainmenu_txt_font.render('Select a game',False,(64, 64, 64))
        self.mainmenu_message_rect = self.mainmenu_message_surf.get_rect(center=(500, 100))
        self.selectagame_message_rect = self.selectagame_message_surf.get_rect(center=(500, 250))
        self.is_active = False
    def display(self):
        self.screen.blit(self.background_surf, (0, 0))
        self.screen.blit(self.mainmenu_message_surf, self.mainmenu_message_rect)
        self.screen.blit(self.selectagame_message_surf, self.selectagame_message_rect)
        self.screen.blit(self.ttt_surf, self.ttt_rect)
        self.screen.blit(self.othello_surf, self.othello_rect)
        self.screen.blit(self.connectfour_surf, self.connectfour_rect)
    def is_ttt_selected(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.ttt_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed() == (True, False, False):
                return True
        return False
    def is_othello_selected(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.othello_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed() == (True, False, False):
                return True
        return False
    def is_connectfour_selected(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.connectfour_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed() == (True, False, False):
                return True
        return False
