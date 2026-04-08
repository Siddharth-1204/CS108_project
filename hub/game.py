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
        self.is_game_ended = False
        self.board = gameclass.board_generate()
        self.game = gameclass
        self.is_game_started = False
        self.who_won = 0
    def is_move_valid(self, move):
        if self.game.is_valid_move(self.current_turn, self.board, move):
            return True
        return False
    def next_state(self, move):
        if self.is_move_valid(move):
            self.board = self.game.next_board_state(self.current_turn, self.board, move)
            self.recent_move = move
            self.is_game_ended, self.who_won = self.game.is_game_ended(self.board, move)
            if self.current_turn == 1: self.current_turn = 2
            else : self.current_turn = 1

pygame.init()
display_screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Game Hub")
clock = pygame.time.Clock()

mainmenu_background_surf = pygame.image.load('media/images/mainmenu_background.png').convert()
mainmenu_ttt_logo_surf = pygame.image.load('media/images/ttt_logo.jpg').convert()
mainmenu_othello_logo_surf = pygame.image.load('media/images/othello_logo.jpg').convert()
mainmenu_connectfour_logo_surf = pygame.image.load('media/images/connectfour_logo.png').convert()

mainmenu_background_surf = pygame.transform.scale(mainmenu_background_surf, (1000, 800))
mainmenu_ttt_logo_surf = pygame.transform.scale(mainmenu_ttt_logo_surf, (200, 200))
mainmenu_othello_logo_surf = pygame.transform.scale(mainmenu_othello_logo_surf, (200, 200))
mainmenu_connectfour_logo_surf = pygame.transform.scale(mainmenu_connectfour_logo_surf, (200, 200))

mainmenu = Mainmenu.MainMenu(mainmenu_background_surf, mainmenu_ttt_logo_surf, mainmenu_othello_logo_surf, mainmenu_connectfour_logo_surf, display_screen)
mainmenu.is_active = True

gameplay_background_surf = pygame.image.load('media/images/gameplay_background.png').convert()
gameplay_background_surf = pygame.transform.scale(gameplay_background_surf, (1000, 800))

ttt_board_surf = pygame.image.load('media/images/tictactoe_board.png').convert_alpha()
ttt_board_surf = pygame.transform.scale(ttt_board_surf, (700, 700))
'''
othello_board_surf = pygame.image.load('media/images/mainmenu_background.jpg').convert()
othello_board_surf = pygame.transform.scale(othello_board_surf, (600, 600))
'''

connectfour_board_surf = pygame.image.load('media/images/connectfour_board.png').convert()
connectfour_board_surf = pygame.transform.scale(connectfour_board_surf, (700, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if mainmenu.is_active :
        mainmenu.display()
        if mainmenu.is_ttt_selected() :
            mainmenu.game_selected = True
            the_game_class = TicTacToe.Ttt_class(ttt_board_surf)
        '''
        if mainmenu.is_othello_selected() :
            mainmenu.game_selected = True
            the_game_class = Othello.Othello_class(othello_board_surf)
        '''
        if mainmenu.is_connectfour_selected() :
            mainmenu.game_selected = True
            the_game_class = Connectfour.Connectfour_class(connectfour_board_surf)
        
        if mainmenu.game_selected == True :
            if mainmenu.released() == True :
                gameplay = Gameplay.Gameplay(gameplay_background_surf, display_screen, the_game_class)
                basegameclass = BaseGameClass(sys.argv[1], sys.argv[2], the_game_class)
                mainmenu.game_selected = False
                mainmenu.is_active = False
                gameplay.is_active = True

    elif gameplay.is_active :
        if basegameclass.is_game_ended == False :
            gameplay.first_display(basegameclass.is_game_started)
            if pygame.mouse.get_pressed() == (True, False, False):
                gameplay.clicked = True
            if gameplay.clicked and gameplay.released ():
                if basegameclass.game.get_move() != -1 :
                    basegameclass.is_game_started = True
                    selectedmove = basegameclass.game.get_move()
                    basegameclass.next_state(selectedmove)
                    gameplay.display(basegameclass.board)
                gameplay.clicked = False
        else :
            gameplay.is_active = False
            mainmenu.is_active = True
    pygame.display.update()
    clock.tick(60)
