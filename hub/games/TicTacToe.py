import numpy as np
import pygame

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
        return board_array
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
            diagonal_array_top_left = board_array[np.linspace(0, no_of_diagonal_cells_left_top-1, no_of_diagonal_cells_left_top, dtype = int), np.linspace(current_move[1] - current_move[0], 9, no_of_diagonal_cells_left_top, dtype = int)]
        else :
            diagonal_array_top_left = board_array[np.linspace(current_move[0] - current_move[1], 9, no_of_diagonal_cells_left_top, dtype = int), np.linspace(0, no_of_diagonal_cells_left_top-1, no_of_diagonal_cells_left_top, dtype = int)]
        new_diagonal_array_top_left = np.hstack((np.zeros(1), diagonal_array_top_left, np.zeros(1)))
        is_diagonal_top_left_array_cell_current_turn = (new_diagonal_array_top_left == current_turn)
        not_matching_indices_list_diagonal_top_left = np.argwhere(is_diagonal_top_left_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_left_diff = not_matching_indices_list_diagonal_top_left[1:,0] - not_matching_indices_list_diagonal_top_left[:-1,0]
        if (not_matching_indices_list_diagonal_top_left_diff >= 6).any() :
            return True, current_turn

        no_of_diagonal_cells_top_right = 10 - abs(current_move[1] + current_move[0] - 9)
        if current_move[1] + current_move[0] <= 9:
            diagonal_array_top_right = board_array[np.linspace(0, no_of_diagonal_cells_top_right-1, no_of_diagonal_cells_top_right, dtype = int), np.linspace(no_of_diagonal_cells_top_right-1, 0, no_of_diagonal_cells_top_right, dtype = int)]
        else :
            diagonal_array_top_right = board_array[np.linspace(current_move[1] + current_move[0] - 9, 9, no_of_diagonal_cells_top_right, dtype = int), np.linspace(9, current_move[1] + current_move[0] - 9, no_of_diagonal_cells_top_right, dtype = int)]
        new_diagonal_array_top_right = np.hstack((np.zeros(1), diagonal_array_top_right, np.zeros(1)))
        is_diagonal_top_right_array_cell_current_turn = (new_diagonal_array_top_right == current_turn)
        not_matching_indices_list_diagonal_top_right = np.argwhere(is_diagonal_top_right_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_right_diff = not_matching_indices_list_diagonal_top_right[1:,0] - not_matching_indices_list_diagonal_top_right[:-1,0]
        if (not_matching_indices_list_diagonal_top_right_diff >= 6).any() :
            return True, current_turn

        return False, 0
    def display_board(self, screen):
        screen.blit(self.board, self.board_rect)
    def display_marks(self, screen, center_x, center_y, board_array):
        if board_array[int((center_y-115)/70)][int((center_x-185)/70)] == 1:
            pygame.draw.line(screen, "#fdd56c", (center_x-25, center_y-25), (center_x+25, center_y+25), width=5)
            pygame.draw.line(screen, "#fdd56c", (center_x+25, center_y-25), (center_x-25, center_y+25), width=5)
        elif board_array[int((center_y-115)/70)][int((center_x-185)/70)] == 2:
            pygame.draw.circle(screen, "#6fa1d7", (center_x, center_y), 25, width = 5)
    def display(self, screen, board_array):
        screen.blit(self.board, self.board_rect)
        self.screen = screen
        center_x_array = np.linspace(185, 815, 10)*np.ones((10, 1))
        center_y_array = (np.linspace(115, 745, 10)*np.ones((10, 1))).transpose()
        for i in range(10):
            for j in range(10) :
                self.display_marks(screen, center_x_array[i][j], center_y_array[i][j], board_array)
    def get_move(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] > 150 and mouse_pos[0] < 850 :
            if mouse_pos[1] > 80 and mouse_pos[1] < 780 :
                return ((mouse_pos[1]-80)//70 , (mouse_pos[0]-150)//70)
        return -1