import sys
import pygame
import numpy as np
import Screens.Mainmenu as Mainmenu
import Screens.Gameplay as Gameplay
import games.TicTacToe as TicTacToe
import games.Othello as Othello
import games.Connectfour as Connectfour
class BaseGameClass :
    def __init__ (self, username1, username2, gameclass):
        self.player1 = username1
        self.player2 = username2
        self.current_turn = 1
        self.board = gameclass.board_generate()
        self.game = gameclass
    def is_move_valid(self, move):
        if self.game.is_valid_move(self.current_turn, self.board, move):
            return True
        return False
    def is_game_ended(self):
        if self.game.is_game_ended(self.board):
            return True
        return False
    def next_state(self, move):
        if self.is_move_valid(move):
            self.board = self.game.next_board_state(self.current_turn, self.board, move)
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

gameplay_background_image = pygame.image.load('media/images/gameplay_background.jpg')
gameplay_background_surf = pygame.transform.scale(gameplay_background_image, (1000, 800))

ttt_board_image = pygame.image.load('media/images/')
ttt_board_surf = pygame.transform.scale(ttt_board_image, (600, 600))

othello_board_image = pygame.image.load('media/images/')
othello_board_surf = pygame.transform.scale(ttt_board_image, (600, 600))

connectfour_board_image = pygame.image.load('media/images/')
connectfour_board_surf = pygame.transform.scale(ttt_board_image, (600, 600))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if mainmenu.is_active :
        mainmenu.display()
        if mainmenu.is_ttt_selected() :
            mainmenu.is_active = False
            ttt_class = TicTacToe.Ttt_class(ttt_board_surf)
            gameplay = Gameplay.Gameplay(gameplay_background_surf, display_screen, ttt_class)
            basegameclass = BaseGameClass(sys.argv[1], sys.argv[2], ttt_class)
            gameplay.is_active = True
            while not basegameclass.is_game_ended() :
                gameplay.display(basegameclass.board)
                selectedmove = gameplay.get_move()
                basegameclass.next_state(selectedmove)
            gameplay.is_active = False
        if mainmenu.is_othello_selected() :
            mainmenu.is_active = False
            othello_class = Othello.Othello_class(othello_board_surf)
            gameplay = Gameplay.Gameplay(gameplay_background_surf, display_screen, othello_class)
            basegameclass = BaseGameClass(sys.argv[1], sys.argv[2], othello_class)
            gameplay.is_active = True
            while not basegameclass.is_game_ended() :
                gameplay.display(basegameclass.board)
                selectedmove = gameplay.get_move()
                basegameclass.next_state(selectedmove)
            gameplay.is_active = False
        if mainmenu.is_connectfour_selected() :
            mainmenu.is_active = False
            connectfour_class = Connectfour.Connectfour_class(connectfour_board_surf)
            gameplay = Gameplay.Gameplay(gameplay_background_surf, display_screen, connectfour_class)
            basegameclass = BaseGameClass(sys.argv[1], sys.argv[2], connectfour_class)
            gameplay.is_active = True
            while not basegameclass.is_game_ended() :
                gameplay.display(basegameclass.board)
                selectedmove = gameplay.get_move()
                basegameclass.next_state(selectedmove)
            gameplay.is_active = False          
    pygame.display.update()
    clock.tick(60)
