import numpy as np
import pygame

class Othello_class:
    def __init__(self, board):
        self.board = board
        self.board_rect = self.board.get_rect(center = (500, 400))
    def board_generate(self):
        board_array = np.zeros((8, 8))
        board_array[3][3], board_array[4][4], board_array[3][4], board_array[4][3] = 2, 2, 1, 1
        return board_array
    def is_valid_move(self, current_turn, board_array, current_move):
        if board_array[current_move[0]][current_move[1]] == 0:
            horizontal_line = board_array[current_move[0],:]
            vertical_line = board_array[:,current_move[1]]
            current_turn = board_array[current_move[0]][current_move[1]]

            horizontal_1st_array = horizontal_line[ : current_move[1]]
            horizontal_2nd_array = horizontal_line[current_move[1]+1 : ]
            if np.argwhere(horizontal_1st_array == current_turn).size > 0 :
                horizontal_1st_neighbour = np.argwhere(horizontal_1st_array == current_turn)[-1][0]
                horizontal_left_part = horizontal_line[horizontal_1st_neighbour+1 : current_move[1]]
                if (horizontal_left_part == (3-current_turn)).all() :
                    return True
            if np.argwhere(horizontal_2nd_array == current_turn).size > 0 :
                horizontal_2nd_neighbour = np.argwhere(horizontal_2nd_array == current_turn)[0][0]
                horizontal_right_part = horizontal_line[current_move[1]+1:horizontal_2nd_neighbour]
                if (horizontal_right_part == (3-current_turn)).all() :
                    return True
            
            vertical_1st_array = vertical_line[ : current_move[0]]
            vertical_2nd_array = vertical_line[current_move[0]+1 : ]
            if np.argwhere(vertical_1st_array == current_turn).size > 0 :
                vertical_1st_neighbour = np.argwhere(vertical_1st_array == current_turn)[-1][0]
                vertical_left_part = vertical_line[vertical_1st_neighbour+1 : current_move[0]]
                if (vertical_left_part == (3-current_turn)).all() :
                    return True
            if np.argwhere(vertical_2nd_array == current_turn).size > 0 :
                vertical_2nd_neighbour = np.argwhere(vertical_2nd_array == current_turn)[0][0]
                vertical_right_part = vertical_line[current_move[0]+1:vertical_2nd_neighbour]
                if (vertical_right_part == (3-current_turn)).all() :
                    return True          
            
            no_of_diagonal_cells_left_top = 8 - abs(current_move[1] - current_move[0])
            if current_move[1] >= current_move[0]:
                diagonal_array_top_left = board_array[np.linspace(0, no_of_diagonal_cells_left_top-1, no_of_diagonal_cells_left_top, dtype = int), np.linspace(current_move[1] - current_move[0], 7, no_of_diagonal_cells_left_top, dtype = int)]
                current_move_left = current_move[0]
            else :
                diagonal_array_top_left = board_array[np.linspace(current_move[0] - current_move[1], 7, no_of_diagonal_cells_left_top, dtype = int), np.linspace(0, no_of_diagonal_cells_left_top-1, no_of_diagonal_cells_left_top, dtype = int)]
                current_move_left = current_move[1]
            
            top_left_1st_array = diagonal_array_top_left[ : current_move_left]
            top_left_2nd_array = diagonal_array_top_left[current_move_left+1 : ]
            if np.argwhere(top_left_1st_array == current_turn).size > 0 :
                top_left_1st_neighbour = np.argwhere(top_left_1st_array == current_turn)[-1][0]
                top_left_left_part = diagonal_array_top_left[top_left_1st_neighbour+1 : current_move_left]
                if (top_left_left_part == (3-current_turn)).all() :
                    return True
            if np.argwhere(horizontal_2nd_array == current_turn).size > 0 :
                top_left_2nd_neighbour = np.argwhere(top_left_2nd_array == current_turn)[0][0]
                top_left_right_part = diagonal_array_top_left[current_move_left+1:top_left_2nd_neighbour]
                if (top_left_right_part == (3-current_turn)).all() :
                    return True

            no_of_diagonal_cells_top_right = 8 - abs(current_move[1] + current_move[0] - 7)
            if current_move[1] + current_move[0] <= 7:
                diagonal_array_top_right = board_array[np.linspace(0, no_of_diagonal_cells_top_right-1, no_of_diagonal_cells_top_right, dtype = int), np.linspace(no_of_diagonal_cells_top_right-1, 0, no_of_diagonal_cells_top_right, dtype = int)]
                current_move_right = current_move[0]
            else :
                diagonal_array_top_right = board_array[np.linspace(current_move[1] + current_move[0] - 7, 7, no_of_diagonal_cells_top_right, dtype = int), np.linspace(7, current_move[1] + current_move[0] - 7, no_of_diagonal_cells_top_right, dtype = int)]
                current_move_right = 7 - current_move[1]

            top_right_1st_array = diagonal_array_top_right[ : current_move_right]
            top_right_2nd_array = diagonal_array_top_right[current_move_right+1 : ]
            if np.argwhere(top_right_1st_array == current_turn).size > 0 :
                top_right_1st_neighbour = np.argwhere(top_right_1st_array == current_turn)[-1][0]
                top_right_left_part = diagonal_array_top_left[top_right_1st_neighbour+1 : current_move_right]
                if (top_right_left_part == (3-current_turn)).all() :
                    return True
            if np.argwhere(horizontal_2nd_array == current_turn).size > 0 :
                top_right_2nd_neighbour = np.argwhere(top_right_2nd_array == current_turn)[0][0]
                top_right_right_part = diagonal_array_top_right[current_move_right+1:top_right_2nd_neighbour]
                if (top_right_right_part == (3-current_turn)).all() :
                    return True 
        return False
    def next_board_state(self, current_turn, board_array, current_move):
        if board_array[current_move[0]][current_move[1]] == 0:
            pass
    def is_game_ended(self, board_array, current_move):
        return
    def display_board(self, screen):
        screen.blit(self.board, self.board_rect)
    def display_coin(self, screen, center_x, center_y, board_array):
        if board_array[int((center_y-137.5) / 75)][int((center_x-237.5)/75)] == 1:
            pygame.draw.circle(screen, (64, 64, 64), (center_x, center_y), 37, width = 0)
        elif board_array[int((center_y-137.5) / 75)][int((center_x-237.5)/75)] == 2:
            pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), 37, width = 0)
    def display(self, screen, board_array):
        screen.blit(self.board, self.board_rect)
        self.screen = screen
        center_x_array = np.linspace(237.5, 762.5, 8)*np.ones((8, 1))
        center_y_array = (np.linspace(137.5, 662.5, 8)*np.ones((8, 1))).transpose()
        for i in range(8):
            for j in range(8) :
                self.display_coin(screen, center_x_array[i][j], center_y_array[i][j], board_array)
    def get_move(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] < 700 and mouse_pos[1] > 100:
            if mouse_pos[0] < 800 and mouse_pos[0] > 200 :
                return ((mouse_pos[1]-100)//75 , (mouse_pos[0]-200)//75)
        return -1
    