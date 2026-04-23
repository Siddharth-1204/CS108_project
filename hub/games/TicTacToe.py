import numpy as np
import pygame
import math

class Ttt_class :
    def __init__(self, board) :
        self.board = board
        self.board_rect = self.board.get_rect(center = (500, 430))
    def board_generate(self):
        return np.zeros((10, 10))
    def is_valid_move(self, current_turn, board_array, current_move):
        if board_array[current_move[0]][current_move[1]] == 0:
            return True
        return False
    def next_board_state(self, current_turn, board_array, current_move):
        board_array[current_move[0]][current_move[1]] = current_turn
        return board_array, 3-current_turn
    def is_game_ended(self, board_array, current_move):
        horizontal_line = board_array[current_move[0],:]
        vertical_line = board_array[:,current_move[1]]
        current_turn = board_array[current_move[0]][current_move[1]]

        new_horizontal_line = np.hstack((np.zeros(1), horizontal_line, np.zeros(1)))
        is_cell_in_horizontal_current_turn = (new_horizontal_line == current_turn)
        not_maching_indices_horizontal = np.argwhere(is_cell_in_horizontal_current_turn == False)
        not_matching_indices_diff_horizontal = not_maching_indices_horizontal[1:,0] - not_maching_indices_horizontal[:-1,0]
        if (not_matching_indices_diff_horizontal >= 6).any() :
            return True, current_turn
        
        new_vertical_line = np.hstack((np.zeros(1), vertical_line, np.zeros(1)))
        is_cell_in_vertical_current_turn = (new_vertical_line == current_turn)
        not_maching_indices_vertical = np.argwhere(is_cell_in_vertical_current_turn == False)
        not_matching_indices_diff_vertical = not_maching_indices_vertical[1:,0] - not_maching_indices_vertical[:-1,0]
        if (not_matching_indices_diff_vertical >= 6).any() :
            return True, current_turn

        no_of_diagonal_cells_left_top = 10 - abs(current_move[1] - current_move[0])
        if current_move[1] >= current_move[0]:
            diagonal_array_top_left = board_array[np.arange(0, no_of_diagonal_cells_left_top, dtype = int), np.arange(current_move[1] - current_move[0], 10, dtype = int)]
        else :
            diagonal_array_top_left = board_array[np.arange(current_move[0] - current_move[1], 10, dtype = int), np.arange(0, no_of_diagonal_cells_left_top, dtype = int)]
        new_diagonal_array_top_left = np.hstack((np.zeros(1), diagonal_array_top_left, np.zeros(1)))
        is_diagonal_top_left_array_cell_current_turn = (new_diagonal_array_top_left == current_turn)
        not_matching_indices_list_diagonal_top_left = np.argwhere(is_diagonal_top_left_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_left_diff = not_matching_indices_list_diagonal_top_left[1:,0] - not_matching_indices_list_diagonal_top_left[:-1,0]
        if (not_matching_indices_list_diagonal_top_left_diff >= 6).any() :
            return True, current_turn

        no_of_diagonal_cells_top_right = 10 - abs(current_move[1] + current_move[0] - 9)
        if current_move[1] + current_move[0] <= 9:
            diagonal_array_top_right = board_array[np.arange(0, no_of_diagonal_cells_top_right, dtype = int), np.arange(no_of_diagonal_cells_top_right-1, -1, -1, dtype = int)]
        else :
            diagonal_array_top_right = board_array[np.arange(current_move[1] + current_move[0] - 9, 10, dtype = int), np.arange(9, current_move[1] + current_move[0] - 10, -1, dtype = int)]
        new_diagonal_array_top_right = np.hstack((np.zeros(1), diagonal_array_top_right, np.zeros(1)))
        is_diagonal_top_right_array_cell_current_turn = (new_diagonal_array_top_right == current_turn)
        not_matching_indices_list_diagonal_top_right = np.argwhere(is_diagonal_top_right_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_right_diff = not_matching_indices_list_diagonal_top_right[1:,0] - not_matching_indices_list_diagonal_top_right[:-1,0]
        if (not_matching_indices_list_diagonal_top_right_diff >= 6).any() :
            return True, current_turn

        if (board_array != 0).all() :
            return True, 0

        return False, 0
    def display_marks(self, i, j):
        if self.board_array[j][i] == 1:
            pygame.draw.line(self.screen, "#fdd56c", (160+i*70, 90+j*70), (210+i*70, 140+j*70), width=6)
            pygame.draw.line(self.screen, "#fdd56c", (210+i*70, 90+j*70), (160+i*70, 140+j*70), width=6)
        elif self.board_array[j][i] == 2:
            pygame.draw.circle(self.screen, "#6fa1d7", (185+i*70, 115+j*70), 25, width = 5)
        return True
    def display(self, screen, board_array, font, username1, username2, turn, is_game_ended, winner):
        screen.blit(self.board, self.board_rect)
        if not is_game_ended:
            player = username1 if turn == 1 else username2
            colour = "#fdd56c" if turn == 1 else "#6fa1d7"
            text_surface = font.render(f"{player}'s turn", False, colour)
        elif is_game_ended and winner!=0:
            player = username1 if turn == 2 else username2
            colour = "#fdd56c" if turn == 2 else "#6fa1d7"
            text_surface = font.render(f"{player} won", False, colour)
        else:
            text_surface = font.render("Match tied", False, (64, 64, 64))
        text_rect = pygame.Surface.get_rect(text_surface, midtop = (500, 10))
        screen.blit(text_surface, text_rect)
        self.screen = screen
        self.board_array = board_array
        display_vector = np.vectorize(self.display_marks)
        work = display_vector(np.arange(0, 10, dtype = int)*np.ones((10, 1), dtype = int), (np.arange(0, 10, dtype = int)*np.ones((10, 1), dtype = int)).transpose())
    def get_move(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > 150 and mouse_pos[0] < 850 :
            if mouse_pos[1] > 80 and mouse_pos[1] < 780 :
                return ((mouse_pos[1]-80)//70 , (mouse_pos[0]-150)//70)
        return -1
    def animate(self, screen, board_array, selected_move, current_turn, started_animating):
        if current_turn == 2:
            global r, dr
            if started_animating:
                r = 0
                dr = 2
            else:
                r+=dr
                if r+dr > 25:
                    dr = 25-r
            pygame.draw.circle(self.screen, "#6fa1d7", (int(185+selected_move[1]*70), int(115+selected_move[0]*70)), r, width = int(r/5))
            if r == 25:
                return False
            return True
        else:
            global l, dl
            if started_animating:
                l = 0
                dl = 2
            else:
                l+=dl
                if l+dl > 25:
                    dl = 25-l
            pygame.draw.line(self.screen, "#fdd56c", (int(185+selected_move[1]*70-l), int(115+selected_move[0]*70-l)), (int(185+selected_move[1]*70+l), int(115+selected_move[0]*70+l)), width=int(l/4))
            pygame.draw.line(self.screen, "#fdd56c", (int(185+selected_move[1]*70+l), int(115+selected_move[0]*70-l)), (int(185+selected_move[1]*70-l), int(115+selected_move[0]*70+l)), width=int(l/4))
            if l == 25:
                return False
            return True
    def animate_win(self, board_array, current_move, win_animation_started, winner):
        global l, dl, mx, my, x, y
        if winner == 0:
            return False
        if win_animation_started :
            horizontal_line = board_array[current_move[0],:]
            vertical_line = board_array[:,current_move[1]]
            current_turn = board_array[current_move[0]][current_move[1]]

            new_horizontal_line = np.hstack((np.zeros(1), horizontal_line, np.zeros(1)))
            is_cell_in_horizontal_current_turn = (new_horizontal_line == current_turn)
            not_maching_indices_horizontal = np.argwhere(is_cell_in_horizontal_current_turn == False)
            not_matching_indices_diff_horizontal = not_maching_indices_horizontal[1:,0] - not_maching_indices_horizontal[:-1,0]
            if (not_matching_indices_diff_horizontal >= 6).any() :
                mx, my = 1, 0
                horizontal_left = np.argwhere(new_horizontal_line[:current_move[1]+1] != current_turn)
                coins_left_side = current_move[1]- horizontal_left[-1][0]
            
            new_vertical_line = np.hstack((np.zeros(1), vertical_line, np.zeros(1)))
            is_cell_in_vertical_current_turn = (new_vertical_line == current_turn)
            not_maching_indices_vertical = np.argwhere(is_cell_in_vertical_current_turn == False)
            not_matching_indices_diff_vertical = not_maching_indices_vertical[1:,0] - not_maching_indices_vertical[:-1,0]
            if (not_matching_indices_diff_vertical >= 6).any() :
                mx, my = 0, 1
                vertical_left = np.argwhere(new_vertical_line[:current_move[0]+1] != current_turn)
                coins_left_side = current_move[0] - vertical_left[-1][0]

            no_of_diagonal_cells_left_top = 10 - abs(current_move[1] - current_move[0])
            if current_move[1] >= current_move[0]:
                diagonal_array_top_left = board_array[np.arange(0, no_of_diagonal_cells_left_top, dtype = int), np.arange(current_move[1] - current_move[0], 10, dtype = int)]
                current_index = current_move[0]
            else :
                diagonal_array_top_left = board_array[np.arange(current_move[0] - current_move[1], 10, dtype = int), np.arange(0, no_of_diagonal_cells_left_top, dtype = int)]
                current_index = current_move[1]
            new_diagonal_array_top_left = np.hstack((np.zeros(1), diagonal_array_top_left, np.zeros(1)))
            is_diagonal_top_left_array_cell_current_turn = (new_diagonal_array_top_left == current_turn)
            not_matching_indices_list_diagonal_top_left = np.argwhere(is_diagonal_top_left_array_cell_current_turn == False)
            not_matching_indices_list_diagonal_top_left_diff = not_matching_indices_list_diagonal_top_left[1:,0] - not_matching_indices_list_diagonal_top_left[:-1,0]
            if (not_matching_indices_list_diagonal_top_left_diff >= 6).any() :
                mx, my = 1, 1
                top_left_left = np.argwhere(new_diagonal_array_top_left[:current_index+1] != current_turn)
                coins_left_side = current_index - top_left_left[-1][0]

            no_of_diagonal_cells_top_right = 10 - abs(current_move[1] + current_move[0] - 9)
            if current_move[1] + current_move[0] <= 9:
                diagonal_array_top_right = board_array[np.arange(0, no_of_diagonal_cells_top_right, dtype = int), np.arange(no_of_diagonal_cells_top_right-1, -1, -1, dtype = int)]
                current_index = current_move[0]
            else :
                diagonal_array_top_right = board_array[np.arange(current_move[1] + current_move[0] - 9, 10, dtype = int), np.arange(9, current_move[1] + current_move[0] - 10, -1, dtype = int)]
                current_index = 9 - current_move[1]
            new_diagonal_array_top_right = np.hstack((np.zeros(1), diagonal_array_top_right, np.zeros(1)))
            is_diagonal_top_right_array_cell_current_turn = (new_diagonal_array_top_right == current_turn)
            not_matching_indices_list_diagonal_top_right = np.argwhere(is_diagonal_top_right_array_cell_current_turn == False)
            not_matching_indices_list_diagonal_top_right_diff = not_matching_indices_list_diagonal_top_right[1:,0] - not_matching_indices_list_diagonal_top_right[:-1,0]
            if (not_matching_indices_list_diagonal_top_right_diff >= 6).any() :
                mx, my = 1, -1
                top_right_right = np.argwhere(new_diagonal_array_top_right[current_index+2:] != current_turn)
                coins_left_side = top_right_right[0][0]
            x = int(185+current_move[1]*70 - 70*coins_left_side*mx)
            y = int(115+current_move[0]*70 - 70*coins_left_side*my)
            l = 0
            dl = 3
        else:
            l+=dl
            if l+dl > 330:
                dl = 330-l
        pygame.draw.line(self.screen, (64, 64, 64), (x-25*mx, y-25*my), (x -25*mx + l*mx, y - 25*my + l*my), width=8)
        if l == 330 :
            return (False, "TicTacToe")
        return (True, "TicTacToe")
