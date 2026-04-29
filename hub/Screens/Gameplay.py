import pygame
import numpy as np

class Gameplay :
    def __init__(self, background, screen, gameclass, font, username1, username2):
        self.background_surf = background
        self.gameclass = gameclass
        self.screen = screen
        self.player1 = username1
        self.player2 = username2
        self.font = font
        self.is_active = False
        self.clicked = False
        self.ended = False
    def display(self, board, turn, is_game_ended, winner):
        self.screen.blit(self.background_surf, (0, 0))
        self.gameclass.display(self.screen, board, self.font, self.player1, self.player2, turn, is_game_ended, winner)
    def released(self):
        return pygame.mouse.get_pressed() == (False, False, False) 
    def animate(self, board_array, selected_move, current_turn, started_animating):
        self.screen.blit(self.background_surf, (0, 0))
        self.gameclass.display(self.screen, board_array, self.font, self.player1, self.player2, current_turn, False, 0)
        return self.gameclass.animate(self.screen, board_array, selected_move, current_turn, started_animating)
    def animate_win(self, board_array, current_turn, recent_move, win_animation_started, winner):
        self.display(board_array, current_turn, True, winner)
        return self.gameclass.animate_win(board_array, recent_move, win_animation_started, winner)
    def space_released(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return False
        return True
