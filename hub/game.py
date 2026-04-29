import sys
import pygame
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import csv
import datetime
import Screens.Mainmenu as Mainmenu
import Screens.Gameplay as Gameplay
import Screens.Analytics as Analytics
import Screens.Postgame as Postgame
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
        self.who_won = 0
        self.animating = False
        self.started_animating = False
    def is_move_valid(self, move):
        if self.game.is_valid_move(self.current_turn, self.board, move):
            return True
        return False
    def next_state(self, move):
        if self.is_move_valid(move):
            self.board, self.current_turn = self.game.next_board_state(self.current_turn, self.board, move)
            self.recent_move = move
            self.is_game_ended, self.who_won = self.game.is_game_ended(self.board, move)
            if self.is_game_ended:
                self.win_animation_started = True

pygame.init()
display_screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Game Hub")
clock = pygame.time.Clock()

font_1 = pygame.font.Font("media/fonts/Pixeltype.ttf",size =  60)
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

othello_board_surf = pygame.image.load('media/images/othello_board.png').convert()
othello_board_surf = pygame.transform.scale(othello_board_surf, (600, 600))

connectfour_board_surf = pygame.image.load('media/images/connectfour_board.png').convert()
connectfour_board_surf = pygame.transform.scale(connectfour_board_surf, (700, 700))

mm_logo_surf = pygame.image.load('media/images/ttt_logo.jpg').convert()
mm_logo_surf = pygame.transform.scale(mm_logo_surf, (200, 200))

exit_logo_surf = pygame.image.load('media/images/othello_logo.jpg').convert()
exit_logo_surf = pygame.transform.scale(exit_logo_surf, (200, 200))


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
        
        if mainmenu.is_othello_selected() :
            mainmenu.game_selected = True
            the_game_class = Othello.Othello_class(othello_board_surf)
        
        if mainmenu.is_connectfour_selected() :
            mainmenu.game_selected = True
            the_game_class = Connectfour.Connectfour_class(connectfour_board_surf)
        
        if mainmenu.game_selected == True :
            if mainmenu.released() == True :
                basegameclass = BaseGameClass(sys.argv[1], sys.argv[2], the_game_class)
                gameplay = Gameplay.Gameplay(gameplay_background_surf, display_screen, the_game_class, font_1, basegameclass.player1, basegameclass.player2)
                mainmenu.game_selected = False
                mainmenu.is_active = False
                gameplay.is_active = True

    elif gameplay.is_active :
        if basegameclass.is_game_ended == False and basegameclass.animating == False :
            gameplay.display(basegameclass.board, basegameclass.current_turn, False, basegameclass.who_won)
            if pygame.mouse.get_pressed() == (True, False, False):
                gameplay.clicked = True
            if gameplay.clicked and gameplay.released ():
                if basegameclass.game.get_move() != -1 :
                    basegameclass.selectedmove = basegameclass.game.get_move()
                    if basegameclass.is_move_valid(basegameclass.selectedmove):
                        basegameclass.animating = True
                        basegameclass.started_animating = True
                gameplay.clicked = False
        elif basegameclass.is_game_ended == False and basegameclass.animating == True:
            basegameclass.animating = gameplay.animate(basegameclass.board, basegameclass.selectedmove, basegameclass.current_turn, basegameclass.started_animating)
            basegameclass.started_animating = False
            if basegameclass.animating == False:
                basegameclass.next_state(basegameclass.selectedmove)
                gameplay.display(basegameclass.board, basegameclass.current_turn, basegameclass.is_game_ended, basegameclass.who_won)
        else :
            basegameclass.win_animating, basegameclass.game_name = gameplay.animate_win(basegameclass.board, basegameclass.current_turn, basegameclass.recent_move, basegameclass.win_animation_started, basegameclass.who_won)
            basegameclass.win_animation_started = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not basegameclass.win_animating:
                gameplay.ended = True
            if gameplay.ended and gameplay.space_released():
                analytics = Analytics.Analytics(gameplay_background_surf, display_screen, font_1)
                gameplay.is_active = False
                analytics.is_active = True
                gameplay.ended = False
                
                winner,loser = basegameclass.player1,basegameclass.player2
                if basegameclass.who_won == 2:
                    winner,loser = loser,winner
                elif basegameclass.who_won == 0 :
                    winner,loser = "tie","tie"

                

                with open('history.csv','a') as history :
                    writer = csv.writer(history)
                    writer.writerow([basegameclass.player1, basegameclass.player2, winner,loser , datetime.date.today(), basegameclass.game_name])
        
    elif analytics.is_active :
        analytics.display(basegameclass.player1, basegameclass.player2, basegameclass.who_won, basegameclass.game_name)
        if pygame.mouse.get_pressed() == (True, False, False):
            analytics.pressed = True
        if analytics.pressed and analytics.released():
            argument = analytics.leaderboard()
            subprocess.run(["bash", "./leaderboard.sh", argument])
            analytics.pressed = False
            postgame = Postgame.Postgame(gameplay_background_surf, display_screen, font_1, mm_logo_surf, exit_logo_surf)
            analytics.is_active = False
            postgame.is_active = True


    elif postgame.is_active :
        postgame.display()
        if pygame.mouse.get_pressed() == (True, False, False):
            postgame.pressed = True
        if postgame.pressed and postgame.released() :
            if postgame.get_option() == "MM":
                postgame.is_active = False
                mainmenu.is_active = True
            elif postgame.get_option() == "Exit" :
                postgame.is_active = False
                pygame.quit()
                sys.exit()
            postgame.pressed = False
    pygame.display.update()
    clock.tick(60)
