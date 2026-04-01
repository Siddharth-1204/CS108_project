import pygame

class Gameplay :
    def __init__(self, background, screen, gameclass):
        self.background_surf = background
        self.gameclass = gameclass
        self.screen = screen
        self.is_active = False
        self.board_surf = self.gameclass.board_surf()
    def display(self, boat_array):
        self.screen.blit(self.background_surf, (0, 0))
        self.board_state_surf = self.gameclass.board_state_surf(boat_array)
        self.board_state_rect = self.board_state_surf.get_rect(center = (500, 400))
        self.screen.blit(self.board_state_surf, self.board_state_rect)
    def get_move(self):
        move_rects = self.gameclass.move_rects()
        for possible_move_rect_index in len(move_rects):
            mouse_pos = pygame.mouse.get_pos()
            if move_rects[possible_move_rect_index].collidepoint(mouse_pos):
                if pygame.mouse.get_pressed() == (True, False, False):
                    return self.gameclass.get_move(possible_move_rect_index)