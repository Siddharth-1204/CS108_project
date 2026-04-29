import numpy as np
import pygame

class Connectfour_class :
    def __init__(self, board):
        self.board = board
        self.board_rect = self.board.get_rect(center = (500, 430))
    def board_generate(self):
        # create empty 7x7 board (Connect Four grid)
        return np.zeros((7, 7))
    def is_valid_move(self, current_turn, board_array, current_move):
        # move is valid if top cell of that column is empty
        # (means column is not full)
        if int(board_array[0][current_move]) == 0 :
            return True
        return False
    def next_board_state(self, current_turn, board_array, current_move):
        # simulate gravity: piece falls to lowest empty cell in that column
        board_transpose_array = board_array.transpose()
        board_1d_array = board_transpose_array[current_move]

        # find last empty spot in column and place coin there
        board_array[board_1d_array[board_1d_array == 0].size-1][current_move] = current_turn
        return board_array, 3-current_turn

    def is_game_ended(self, board_array, current_move):
        # get column and row affected by last move
        board_changed_vertical_line = (board_array.transpose())[current_move]

        # index where last coin landed (first non-zero from top)
        first_index_of_move = board_changed_vertical_line[board_changed_vertical_line == 0].size

        board_changed_horizontal_line = board_array[first_index_of_move]
        current_turn = board_array[first_index_of_move][current_move]

        # target pattern: 4 same coins
        winning_array = np.ones(4)*current_turn

        # ---------- vertical check ----------
        # only check downward if enough space
        if first_index_of_move <= 3 :
            if (board_changed_vertical_line[first_index_of_move: first_index_of_move + 4] == winning_array).all():
                return True, current_turn
        
        # ---------- horizontal check ----------
        # padding helps detect continuous segments easily
        new_board_changed_horizontal_line = np.hstack((np.zeros(1), board_changed_horizontal_line, np.zeros(1)))

        is_horizontal_line_cell_current_turn = (new_board_changed_horizontal_line == current_turn)

        # indices where sequence breaks
        not_matching_indices_list_horizontal = np.argwhere(is_horizontal_line_cell_current_turn == False)

        # difference between breaks gives length of continuous segments
        not_matching_indices_list_horizontal_diff = not_matching_indices_list_horizontal[1:,0] - not_matching_indices_list_horizontal[:-1,0]

        # >=5 → means 4 continuous coins (due to padding)
        if (not_matching_indices_list_horizontal_diff >= 5).any() :
            return True, current_turn
        
        # ---------- diagonal (top-left → bottom-right) ----------
        no_of_diagonal_cells_left_top = 7 - abs(current_move - first_index_of_move)

        # extract correct diagonal
        if current_move >= first_index_of_move:
            diagonal_array_top_left = board_array[np.arange(0, no_of_diagonal_cells_left_top, dtype = int), np.arange(current_move - first_index_of_move, 7, dtype = int)]
        else :
            diagonal_array_top_left = board_array[np.arange(first_index_of_move - current_move, 7, dtype = int), np.arange(0, no_of_diagonal_cells_left_top, dtype = int)]

        # same padding + gap logic
        new_diagonal_array_top_left = np.hstack((np.zeros(1), diagonal_array_top_left, np.zeros(1)))
        is_diagonal_top_left_array_cell_current_turn = (new_diagonal_array_top_left == current_turn)
        not_matching_indices_list_diagonal_top_left = np.argwhere(is_diagonal_top_left_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_left_diff = not_matching_indices_list_diagonal_top_left[1:,0] - not_matching_indices_list_diagonal_top_left[:-1,0]

        if (not_matching_indices_list_diagonal_top_left_diff >= 5).any() :
            return True, current_turn
        
        # ---------- diagonal (top-right → bottom-left) ----------
        no_of_diagonal_cells_top_right = 7 - abs(current_move + first_index_of_move - 6)

        if current_move + first_index_of_move <= 6:
            diagonal_array_top_right = board_array[np.arange(0, no_of_diagonal_cells_top_right, dtype = int), np.arange(no_of_diagonal_cells_top_right-1, -1, -1, dtype = int)]
        else :
            diagonal_array_top_right = board_array[np.arange(current_move + first_index_of_move - 6, 7, dtype = int), np.arange(6, current_move + first_index_of_move - 7, -1, dtype = int)]

        new_diagonal_array_top_right = np.hstack((np.zeros(1), diagonal_array_top_right, np.zeros(1)))
        is_diagonal_top_right_array_cell_current_turn = (new_diagonal_array_top_right == current_turn)
        not_matching_indices_list_diagonal_top_right = np.argwhere(is_diagonal_top_right_array_cell_current_turn == False)
        not_matching_indices_list_diagonal_top_right_diff = not_matching_indices_list_diagonal_top_right[1:,0] - not_matching_indices_list_diagonal_top_right[:-1,0]

        if (not_matching_indices_list_diagonal_top_right_diff >= 5).any() :
            return True, current_turn
        
        # ---------- draw condition ----------
        # if top row is filled (no zeros), game is draw
        if first_index_of_move == 0 :
            if np.argwhere(board_changed_horizontal_line == 0).size == 0 :
                return True, 0
        
        return False, 0

    def display_coin(self, i, j):
        # draw blue (player 1) or orange (player 2) coin
        if self.board_array[j][i] == 1:
            pygame.draw.circle(self.screen, "#039BE5", (217+94*i, 146+88*j), 37, width = 0)
        elif self.board_array[j][i] == 2:
            pygame.draw.circle(self.screen, "#F4511E", (217+94*i, 146+88*j), 37, width = 0)

    def display(self, screen, board_array, font, username1, username2, turn, is_game_ended, winner):
        # draw board + turn/winner text
        screen.blit(self.board, self.board_rect)
        if not is_game_ended:
            player = username1 if turn == 1 else username2
            colour = "#039BE5" if turn == 1 else "#F4511E"
            text_surface = font.render(f"{player}'s turn", False, colour)
        elif winner != 0:
            player = username1 if turn == 2 else username2
            colour = "#039BE5" if turn == 2 else "#F4511E"
            text_surface = font.render(f"{player} won", False, colour)
            text_surface_2 = font.render("Press space to continue", False, (64, 64, 64))
        else:
            text_surface = font.render("Match tied", False, (64, 64, 64))
            text_surface_2 = font.render("Press space to continue", False, (64, 64, 64))

        text_rect = pygame.Surface.get_rect(text_surface, midtop = (500, 10))
        screen.blit(text_surface, text_rect)
        if is_game_ended :
            text_rect_2 = pygame.Surface.get_rect(text_surface_2, midtop = (500, 40))
            screen.blit(text_surface_2, text_rect_2)

        self.screen = screen
        self.board_array = board_array

        # draw all coins using vectorization
        display_vector = np.vectorize(self.display_coin)
        work = display_vector(np.arange(0, 7, dtype = int)*np.ones((7, 1), dtype = int), (np.arange(0, 7, dtype = int)*np.ones((7, 1), dtype = int)).transpose())

    def get_move(self):
        # detect column from mouse position
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[1] < 80 and mouse_pos[1] > 0:
            if mouse_pos[0] < 850 and mouse_pos[0] > 150 :
                return (mouse_pos[0] - 150) // 100
        return -1

    def animate(self, screen, board_array, selected_move, current_turn, started_animating):
        # falling animation of coin
        global x, y, dy

        board_changed_vertical_line = (board_array.transpose())[selected_move]

        # find final row where coin will land
        j = board_changed_vertical_line[board_changed_vertical_line == 0].size - 1

        if started_animating:
            # initial position (top)
            x = 217+94*selected_move
            y = 40
            dy = 0
        else:
            # simulate acceleration (gravity effect)
            y+=dy
            if y+dy+1 <= (146+88*j)/2 :
                dy+=1
            elif y+dy <= 146+88*j :
                dy+=0
            else :
                dy=146+88*j-y

        colour = "#039BE5" if current_turn == 1 else "#F4511E"

        pygame.draw.circle(self.screen, colour, (x, y), 37, width = 0)

        # stop animation when coin reaches final position
        if y == 146+88*j:
            return False
        return True

    def animate_win(self, board_array, current_move, win_animation_started, winner):
        # animate line showing winning sequence
        global x, y, l, dl, mx, my

        if winner == 0:
            return False

        if win_animation_started :
            board_changed_vertical_line = (board_array.transpose())[current_move]
            first_index_of_move = board_changed_vertical_line[board_changed_vertical_line == 0].size
            board_changed_horizontal_line = board_array[first_index_of_move]
            current_turn = board_array[first_index_of_move][current_move]
            winning_array = np.ones(4)*current_turn

            # ---------- vertical win ----------
            if first_index_of_move <= 3 :
                if (board_changed_vertical_line[first_index_of_move: first_index_of_move + 4] == winning_array).all():
                    mx, my = 0, 88/94
                    coins_left_side = 0
            
            # ---------- horizontal win ----------
            new_board_changed_horizontal_line = np.hstack((np.zeros(1), board_changed_horizontal_line, np.zeros(1)))
            is_horizontal_line_cell_current_turn = (new_board_changed_horizontal_line == current_turn)
            not_matching_indices_list_horizontal = np.argwhere(is_horizontal_line_cell_current_turn == False)
            not_matching_indices_list_horizontal_diff = not_matching_indices_list_horizontal[1:,0] - not_matching_indices_list_horizontal[:-1,0]

            if (not_matching_indices_list_horizontal_diff >= 5).any() :
                mx, my = 1, 0
                horizontal_left = np.argwhere(new_board_changed_horizontal_line[:current_move+1] != current_turn)
                coins_left_side = current_move - horizontal_left[-1][0]
            
            # ---------- diagonal TL-BR ----------
            no_of_diagonal_cells_left_top = 7 - abs(current_move - first_index_of_move)

            if current_move >= first_index_of_move:
                diagonal_array_top_left = board_array[np.arange(0, no_of_diagonal_cells_left_top, dtype = int), np.arange(current_move - first_index_of_move, 7, dtype = int)]
                current_index = first_index_of_move
            else :
                diagonal_array_top_left = board_array[np.arange(first_index_of_move - current_move, 7, dtype = int), np.arange(0, no_of_diagonal_cells_left_top, dtype = int)]
                current_index = current_move

            new_diagonal_array_top_left = np.hstack((np.zeros(1), diagonal_array_top_left, np.zeros(1)))
            is_diagonal_top_left_array_cell_current_turn = (new_diagonal_array_top_left == current_turn)
            not_matching_indices_list_diagonal_top_left = np.argwhere(is_diagonal_top_left_array_cell_current_turn == False)
            not_matching_indices_list_diagonal_top_left_diff = not_matching_indices_list_diagonal_top_left[1:,0] - not_matching_indices_list_diagonal_top_left[:-1,0]

            if (not_matching_indices_list_diagonal_top_left_diff >= 5).any() :
                mx, my = 1, 88/94
                top_left_left = np.argwhere(new_diagonal_array_top_left[:current_index+1] != current_turn)
                coins_left_side = current_index - top_left_left[-1][0]

            # ---------- diagonal TR-BL ----------
            no_of_diagonal_cells_top_right = 7 - abs(current_move + first_index_of_move - 6)

            if current_move + first_index_of_move <= 6:
                diagonal_array_top_right = board_array[np.arange(0, no_of_diagonal_cells_top_right, dtype = int), np.arange(no_of_diagonal_cells_top_right-1, -1, -1, dtype = int)]
                current_index = first_index_of_move
            else :
                diagonal_array_top_right = board_array[np.arange(current_move + first_index_of_move - 6, 7, dtype = int), np.arange(6, current_move + first_index_of_move - 7, -1, dtype = int)]
                current_index = 6 - current_move

            new_diagonal_array_top_right = np.hstack((np.zeros(1), diagonal_array_top_right, np.zeros(1)))
            is_diagonal_top_right_array_cell_current_turn = (new_diagonal_array_top_right == current_turn)
            not_matching_indices_list_diagonal_top_right = np.argwhere(is_diagonal_top_right_array_cell_current_turn == False)
            not_matching_indices_list_diagonal_top_right_diff = not_matching_indices_list_diagonal_top_right[1:,0] - not_matching_indices_list_diagonal_top_right[:-1,0]

            if (not_matching_indices_list_diagonal_top_right_diff >= 5).any() :
                mx, my = 1, -88/94
                top_right_right = np.argwhere(new_diagonal_array_top_right[current_index+2:] != current_turn)
                coins_left_side = top_right_right[0][0]
            
            # compute starting point of winning line
            x = int(217+current_move*94 - 94*coins_left_side*mx)
            y = int(146+first_index_of_move*88 - 94*coins_left_side*my)

            l = 0
            dl = 5

        else:
            # increase line length gradually (animation)
            l+=dl
            if l+dl > 370:
                dl = 370-l

        # draw animated line
        pygame.draw.line(self.screen, (64, 64, 64), (x-44*mx, y-44*my), (x -44*mx + l*mx, y - 44*my + l*my), width=8)

        if l == 370 :
            return (False, "Connectfour")
        return (True, "Connectfour")