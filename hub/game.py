import sys
import pygame
import numpy as np
import Screens.Mainmenu as Mainmenu

class BaseGameClass :
    def __init__ (self, username1, username2, game):
        self.player1 = username1
        self.player2 = username2
        self.current_turn = 1
        self.board = game.board_generate()
        self.is_game_ended = False
    def next_state(self, move, game):
        self.board = game.next_board_state(self.board, self.current_turn, move)
        self.is_game_ended = game.is_game_ended(self.board)
        if self.current_turn == 1: self.current_turn = 2
        if self.current_turn == 2: self.current_turn = 1

pygame.init()
display_screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Game Hub")
clock = pygame.time.Clock()

mainmenu_background_image = pygame.image.load('media/images/mainmenu_background.jpg')
mainmenu_ttt_logo_image = pygame.image.load('media/images/ttt_logo.jpg')
mainmenu_othello_logo_image = pygame.image.load('media/images/othello_logo.jpg')
mainmenu_connectfour_logo_image = pygame.image.load('media/images/connectfour_logo.png')

mainmenu_background_surf = pygame.transform.scale(mainmenu_background_image, (1000, 800))
mainmenu_ttt_logo_surf = pygame.transform.scale(mainmenu_ttt_logo_image, (200, 200))
mainmenu_othello_logo_surf = pygame.transform.scale(mainmenu_othello_logo_image, (200, 200))
mainmenu_connectfour_logo_surf = pygame.transform.scale(mainmenu_connectfour_logo_image, (200, 200))

mainmenu = Mainmenu.MainMenu(mainmenu_background_surf, mainmenu_ttt_logo_surf, mainmenu_othello_logo_surf, mainmenu_connectfour_logo_surf, display_screen)
mainmenu.is_active = True

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if mainmenu.is_active :
        mainmenu.display()
        if mainmenu.is_ttt_selected() :
            mainmenu.is_active = False
        if mainmenu.is_othello_selected() :
            mainmenu.is_active = False
        if mainmenu.is_connectfour_selected() :
            mainmenu.is_active = False
    
    pygame.display.update()
    clock.tick(60)
