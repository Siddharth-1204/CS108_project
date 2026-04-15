import numpy as np
import pygame

class Connectfour_class :
    def __init__(self, board):
        self.board = board
        self.board_rect = self.board.get_rect(center = (500, 430))
    def board_generate(self):
        return np.zeros((7, 7))
    def is_valid_move(self, current_turn, board_array, current_move):
        if int(board_array[0][current_move]) == 0 :
            return True
        return False
    def next_board_state(self, current_turn, board_array, current_move):
        board_transpose_array = board_array.transpose()
        board_1d_array = board_transpose_array[current_move]
        board_array[board_1d_array[board_1d_array == 0].size-1][current_move] = current_turn
        return board_array, 3-current_turn
    def is_game_ended(self, board_array, current_move):
        board_changed_vertical_line = (board_array.transpose())[current_move]
        first_index_of_move = board_changed_vertical_line[board_changed_vertical_line == 0].size
        board_changed_horizontal_line = board_array[first_index_of_move]
        current_turn = board_array[first_index_of_move][current_move]
        winning_array = np.ones(4)*current_turn

        if first_index_of_move <= 3 :
            if (board_changed_vertical_line[first_index_of_move: first_index_of_move + 4] == winning_array).all():
                return True, current_turn
        
        new_board_changed_horizontal_line = np.hstack((np.zeros(1), board_changed_horizontal_line, np.zeros(1)))
        is_horizontal_line_cell_current_turn = (new_board_changed_horizontal_line == current_turn)
        not_matching_indices_list_horizontal = np.argwhere(is_horizontal_line_cell_current_turn == False)
        not_matching_indices_list_horizontal_diff = not_matching_indices_list_horizontal[1:,0] - not_matching_indices_list_horizontal[:-1,0]
        if (not_matching_indices_list_horizontal_diff >= 5).any() :
            return True, current_turn
        
        no_of_diagonal_cells_left_top = 7 - abs(current_move - first_index_of_move)
        if current_move >= first_index_of_move:
            diagonal_array_top_left = board_array[np.linspace(0, no_of_diagonal_cells_left_top-1, no_of_diagonal_cells_left_top, dtype = int), np.linspace(current_move - first_index_of_move, 6, no_of_diagonal_cells_left_top, dtype = int)]
        else :
            diagonal_array_top_left = board_array[np.linspace(first_index_of_move - current_move, 6, no_of_diagonal_cells_left_top, dtype = int), np.linspace(0, no_of_diagonal_cells_left_top-1, no_of_diagonal_cells_left_top, dtype = int)]
        new_diagonal_array_top_left = np.hstack((np.zeros(1), diagonal_array_top_left, np.zeros(1)))
        is_diagonal_top_left_array_cell_current_turn = (new_diagonal_array_top_left == current_turn)
        not_matching_indices_list_diagonal_top_left = np.argwhere(is_diagonal_top_left_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_left_diff = not_matching_indices_list_diagonal_top_left[1:,0] - not_matching_indices_list_diagonal_top_left[:-1,0]
        if (not_matching_indices_list_diagonal_top_left_diff >= 5).any() :
            return True, current_turn
        
        no_of_diagonal_cells_top_right = 7 - abs(current_move + first_index_of_move - 6)
        if current_move + first_index_of_move <= 6:
            diagonal_array_top_right = board_array[np.linspace(0, no_of_diagonal_cells_top_right-1, no_of_diagonal_cells_top_right, dtype = int), np.linspace(no_of_diagonal_cells_top_right-1, 0, no_of_diagonal_cells_top_right, dtype = int)]
        else :
            diagonal_array_top_right = board_array[np.linspace(current_move + first_index_of_move - 6, 6, no_of_diagonal_cells_top_right, dtype = int), np.linspace(6, current_move + first_index_of_move - 6, no_of_diagonal_cells_top_right, dtype = int)]
        new_diagonal_array_top_right = np.hstack((np.zeros(1), diagonal_array_top_right, np.zeros(1)))
        is_diagonal_top_right_array_cell_current_turn = (new_diagonal_array_top_right == current_turn)
        not_matching_indices_list_diagonal_top_right = np.argwhere(is_diagonal_top_right_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_right_diff = not_matching_indices_list_diagonal_top_right[1:,0] - not_matching_indices_list_diagonal_top_right[:-1,0]
        if (not_matching_indices_list_diagonal_top_right_diff >= 5).any() :
            return True, current_turn
        
        if first_index_of_move == 0 :
            if np.argwhere(board_changed_horizontal_line == 0).size == 0 :
                return True, 0
        
        return False, 0
    def display_board(self, screen):
        screen.blit(self.board, self.board_rect)
    def display_coin(self, i, j):
        if self.board_array[j][i] == 1:
            pygame.draw.circle(self.screen, "#039BE5", (217+94*i, 146+88*j), 37, width = 0)
        elif self.board_array[j][i] == 2:
            pygame.draw.circle(self.screen, "#F4511E", (217+94*i, 146+88*j), 37, width = 0)
    def display(self, screen, board_array):
        screen.blit(self.board, self.board_rect)
        self.screen = screen
        self.board_array = board_array
        display_vector = np.vectorize(self.display_coin)
        work = display_vector(np.arange(0, 7, dtype = int)*np.ones((7, 1), dtype = int), (np.arange(0, 7, dtype = int)*np.ones((7, 1), dtype = int)).transpose())
    def get_move(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] < 80 and mouse_pos[1] > 0:
            if mouse_pos[0] < 850 and mouse_pos[0] > 150 :
                return (mouse_pos[0] - 150) // 100
        return -1