import pygame
import numpy as np

class Gameplay :
    def __init__(self, background, screen, gameclass):
        self.background_surf = background
        self.gameclass = gameclass
        self.screen = screen
        self.is_active = False
        self.clicked = False
    def first_display(self, is_game_started, first_board_array):
        if not is_game_started :
            self.screen.blit(self.background_surf, (0, 0))
            self.screen.blit(self.gameclass.board, self.gameclass.board_rect)
            self.gameclass.display(self.screen, first_board_array)
    def display(self, board):
        self.screen.blit(self.background_surf, (0, 0))
        self.gameclass.display(self.screen, board)
    def released(self):
        return pygame.mouse.get_pressed() == (False, False, False) 
    