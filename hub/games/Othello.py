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
    def is_move_present(self, board_array, turn):
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(turn, board_array, (i, j)):
                    return True
        return False
    def is_valid_move(self, current_turn, board_array, current_move):
        if board_array[current_move[0]][current_move[1]] == 0:
            horizontal_line = board_array[current_move[0],:]
            vertical_line = board_array[:,current_move[1]]
            
            horizontal_1st_array = horizontal_line[ : current_move[1]]
            horizontal_2nd_array = horizontal_line[current_move[1]+1 : ]
            if np.argwhere(horizontal_1st_array == current_turn).size > 0 :
                horizontal_1st_neighbour = np.argwhere(horizontal_1st_array == current_turn)[-1][0]
                horizontal_left_part = horizontal_1st_array[horizontal_1st_neighbour+1 : ]
                if (horizontal_left_part == (3-current_turn)).all() and horizontal_left_part.size > 0:
                    return True
            if np.argwhere(horizontal_2nd_array == current_turn).size > 0 :
                horizontal_2nd_neighbour = np.argwhere(horizontal_2nd_array == current_turn)[0][0]
                horizontal_right_part = horizontal_2nd_array[:horizontal_2nd_neighbour]
                if (horizontal_right_part == (3-current_turn)).all() and horizontal_right_part.size > 0:
                    return True
            
            vertical_1st_array = vertical_line[ : current_move[0]]
            vertical_2nd_array = vertical_line[current_move[0]+1 : ]
            if np.argwhere(vertical_1st_array == current_turn).size > 0 :
                vertical_1st_neighbour = np.argwhere(vertical_1st_array == current_turn)[-1][0]
                vertical_left_part = vertical_1st_array[vertical_1st_neighbour+1 : ]
                if (vertical_left_part == (3-current_turn)).all() and vertical_left_part.size > 0:
                    return True
            if np.argwhere(vertical_2nd_array == current_turn).size > 0 :
                vertical_2nd_neighbour = np.argwhere(vertical_2nd_array == current_turn)[0][0]
                vertical_right_part = vertical_2nd_array[:vertical_2nd_neighbour]
                if (vertical_right_part == (3-current_turn)).all() and vertical_right_part.size > 0:
                    return True          
            
            no_of_diagonal_cells_left_top = 8 - abs(current_move[1] - current_move[0])
            if current_move[1] >= current_move[0]:
                diagonal_array_top_left = board_array[np.arange(0, no_of_diagonal_cells_left_top-1), np.arange(current_move[1] - current_move[0], 7)]
                current_move_left = current_move[0]
            else :
                diagonal_array_top_left = board_array[np.arange(current_move[0] - current_move[1], 7), np.arange(0, no_of_diagonal_cells_left_top-1)]
                current_move_left = current_move[1]
            
            top_left_1st_array = diagonal_array_top_left[ : current_move_left]
            top_left_2nd_array = diagonal_array_top_left[current_move_left+1 : ]
            if np.argwhere(top_left_1st_array == current_turn).size > 0 :
                top_left_1st_neighbour = np.argwhere(top_left_1st_array == current_turn)[-1][0]
                top_left_left_part = top_left_1st_array[top_left_1st_neighbour+1 : ]
                if (top_left_left_part == (3-current_turn)).all() and top_left_left_part.size > 0:
                    return True
            if np.argwhere(top_left_2nd_array == current_turn).size > 0 :
                top_left_2nd_neighbour = np.argwhere(top_left_2nd_array == current_turn)[0][0]
                top_left_right_part = top_left_2nd_array[:top_left_2nd_neighbour]
                if (top_left_right_part == (3-current_turn)).all() and top_left_right_part.size > 0:
                    return True

            no_of_diagonal_cells_top_right = 8 - abs(current_move[1] + current_move[0] - 7)
            if current_move[1] + current_move[0] <= 7:
                diagonal_array_top_right = board_array[np.arange(0, no_of_diagonal_cells_top_right-1), np.arange(no_of_diagonal_cells_top_right-1, 0, -1)]
                current_move_right = current_move[0]
            else :
                diagonal_array_top_right = board_array[np.arange(current_move[1] + current_move[0] - 7, 7), np.arange(7, current_move[1] + current_move[0] - 7, -1)]
                current_move_right = 7 - current_move[1]

            top_right_1st_array = diagonal_array_top_right[ : current_move_right]
            top_right_2nd_array = diagonal_array_top_right[current_move_right+1 : ]
            if np.argwhere(top_right_1st_array == current_turn).size > 0 :
                top_right_1st_neighbour = np.argwhere(top_right_1st_array == current_turn)[-1][0]
                top_right_left_part = top_right_1st_array[top_right_1st_neighbour+1 : ]
                if (top_right_left_part == (3-current_turn)).all() and top_right_left_part.size > 0:
                    return True
            if np.argwhere(top_right_2nd_array == current_turn).size > 0 :
                top_right_2nd_neighbour = np.argwhere(top_right_2nd_array == current_turn)[0][0]
                top_right_right_part = top_right_2nd_array[:top_right_2nd_neighbour]
                if (top_right_right_part == (3-current_turn)).all() and top_right_right_part.size > 0:
                    return True
        return False
    def next_board_state(self, current_turn, board_array, current_move):
        if board_array[current_move[0]][current_move[1]] == 0:
            horizontal_line = board_array[current_move[0],:]
            vertical_line = board_array[:,current_move[1]]
            
            horizontal_1st_array = horizontal_line[ : current_move[1]]
            horizontal_2nd_array = horizontal_line[current_move[1]+1 : ]
            if np.argwhere(horizontal_1st_array == current_turn).size > 0 :
                horizontal_1st_neighbour = np.argwhere(horizontal_1st_array == current_turn)[-1][0]
                horizontal_left_part = horizontal_1st_array[horizontal_1st_neighbour+1 : ]
                if (horizontal_left_part == (3-current_turn)).all() and horizontal_left_part.size > 0:
                    board_array[current_move[0], np.arange(current_move[1]-horizontal_left_part.size, current_move[1]+1)] = current_turn
            if np.argwhere(horizontal_2nd_array == current_turn).size > 0 :
                horizontal_2nd_neighbour = np.argwhere(horizontal_2nd_array == current_turn)[0][0]
                horizontal_right_part = horizontal_2nd_array[:horizontal_2nd_neighbour]
                if (horizontal_right_part == (3-current_turn)).all() and horizontal_right_part.size > 0:
                    board_array[current_move[0], np.arange(current_move[1], current_move[1] + horizontal_right_part.size+1)] = current_turn
            
            vertical_1st_array = vertical_line[ : current_move[0]]
            vertical_2nd_array = vertical_line[current_move[0]+1 : ]
            if np.argwhere(vertical_1st_array == current_turn).size > 0 :
                vertical_1st_neighbour = np.argwhere(vertical_1st_array == current_turn)[-1][0]
                vertical_left_part = vertical_1st_array[vertical_1st_neighbour+1 : ]
                if (vertical_left_part == (3-current_turn)).all() and vertical_left_part.size > 0:
                    board_array[np.arange(current_move[0]-vertical_left_part.size, current_move[0]+1), current_move[1]] = current_turn
            if np.argwhere(vertical_2nd_array == current_turn).size > 0 :
                vertical_2nd_neighbour = np.argwhere(vertical_2nd_array == current_turn)[0][0]
                vertical_right_part = vertical_2nd_array[:vertical_2nd_neighbour]
                if (vertical_right_part == (3-current_turn)).all() and vertical_right_part.size > 0:
                    board_array[np.arange(current_move[0], current_move[0]+vertical_right_part.size+1), current_move[1]] = current_turn         
            
            no_of_diagonal_cells_left_top = 8 - abs(current_move[1] - current_move[0])
            if current_move[1] >= current_move[0]:
                diagonal_array_top_left = board_array[np.arange(0, no_of_diagonal_cells_left_top-1), np.arange(current_move[1] - current_move[0], 7)]
                current_move_left = current_move[0]
            else :
                diagonal_array_top_left = board_array[np.arange(current_move[0] - current_move[1], 7), np.arange(0, no_of_diagonal_cells_left_top-1)]
                current_move_left = current_move[1]
            
            top_left_1st_array = diagonal_array_top_left[ : current_move_left]
            top_left_2nd_array = diagonal_array_top_left[current_move_left+1 : ]
            if np.argwhere(top_left_1st_array == current_turn).size > 0 :
                top_left_1st_neighbour = np.argwhere(top_left_1st_array == current_turn)[-1][0]
                top_left_left_part = top_left_1st_array[top_left_1st_neighbour+1 : ]
                if (top_left_left_part == (3-current_turn)).all() and top_left_left_part.size > 0:
                    board_array[np.arange(current_move[0]-top_left_left_part.size, current_move[0]+1), np.arange(current_move[1]-top_left_left_part.size, current_move[1]+1)] = current_turn
            if np.argwhere(top_left_2nd_array == current_turn).size > 0 :
                top_left_2nd_neighbour = np.argwhere(top_left_2nd_array == current_turn)[0][0]
                top_left_right_part = top_left_2nd_array[:top_left_2nd_neighbour]
                if (top_left_right_part == (3-current_turn)).all() and top_left_right_part.size > 0:
                    board_array[np.arange(current_move[0], current_move[0]+top_left_right_part.size+1), np.arange(current_move[1], current_move[1] + top_left_right_part.size+1)] = current_turn

            no_of_diagonal_cells_top_right = 8 - abs(current_move[1] + current_move[0] - 7)
            if current_move[1] + current_move[0] <= 7:
                diagonal_array_top_right = board_array[np.arange(0, no_of_diagonal_cells_top_right-1), np.arange(no_of_diagonal_cells_top_right-1, 0, -1)]
                current_move_right = current_move[0]
            else :
                diagonal_array_top_right = board_array[np.arange(current_move[1] + current_move[0] - 7, 7), np.arange(7, current_move[1] + current_move[0] - 7, -1)]
                current_move_right = 7 - current_move[1]

            top_right_1st_array = diagonal_array_top_right[ : current_move_right]
            top_right_2nd_array = diagonal_array_top_right[current_move_right+1 : ]
            if np.argwhere(top_right_1st_array == current_turn).size > 0 :
                top_right_1st_neighbour = np.argwhere(top_right_1st_array == current_turn)[-1][0]
                top_right_left_part = top_right_1st_array[top_right_1st_neighbour+1 : ]
                if (top_right_left_part == (3-current_turn)).all() and top_right_left_part.size > 0:
                    board_array[np.arange(current_move[0]-top_right_left_part.size, current_move[0]+1), np.arange(current_move[1] + top_right_left_part.size, current_move[1]-1, -1)] = current_turn
            if np.argwhere(top_right_2nd_array == current_turn).size > 0 :
                top_right_2nd_neighbour = np.argwhere(top_right_2nd_array == current_turn)[0][0]
                top_right_right_part = top_right_2nd_array[:top_right_2nd_neighbour]
                if (top_right_right_part == (3-current_turn)).all() and top_right_right_part.size > 0:
                    board_array[np.arange(current_move[0], current_move[0]+top_right_right_part.size+1), np.arange(current_move[1], current_move[1]-top_right_right_part.size-1, -1)] = current_turn
        if self.is_move_present(board_array, 3-current_turn):
            return board_array, 3-current_turn
        return board_array, current_turn
    def is_game_ended(self, board_array, current_move):
        if  not (self.is_move_present(board_array, 1) or self.is_move_present(board_array, 2)):
            if np.argwhere(board_array == 1).size > 32:
                return True, 1
            return True, 2
        else:
            return False, 0
    def display_board(self, screen):
        screen.blit(self.board, self.board_rect)
    def display_coin(self, i, j):
        if self.board_array[j][i] == 1:
            pygame.draw.circle(self.screen, (64, 64, 64), (237.5+75*i, 137.5+75*j), 30, width = 0)
        elif self.board_array[j][i] == 2:
            pygame.draw.circle(self.screen, (255, 255, 255), (237.5+75*i, 137.5+75*j), 30, width = 0)
    def display(self, screen, board_array):
        screen.blit(self.board, self.board_rect)
        self.screen = screen
        self.board_array = board_array
        display_vector = np.vectorize(self.display_coin)
        work = display_vector(np.arange(0, 8, dtype = int)*np.ones((8, 1), dtype = int), (np.arange(0, 8, dtype = int)*np.ones((8, 1), dtype = int)).transpose())
    def get_move(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] < 700 and mouse_pos[1] > 100:
            if mouse_pos[0] < 800 and mouse_pos[0] > 200 :
                return ((mouse_pos[1]-100)//75 , (mouse_pos[0]-200)//75)
        return -1
    