import pygame

class Analytics :
    def __init__(self, background, screen, font):
        self.background_surf = background
        self.screen = screen
        self.font = font
        self.is_active = False
        self.pressed = False
    def display(self, player1, player2, winner, game_name):
        self.screen.blit(self.background_surf, (0,0))
        text_surf1 = self.font.render(f"{game_name}:{player1} vs {player2}", False, (64, 64, 64))
        text_rect1 = pygame.Surface.get_rect(text_surf1, midtop = (500, 200))
        winner_name = player1 if winner == 1 else player2
        if winner != 0 :
            text_surf2 = self.font.render(f"Winner : {winner_name}", False, (64, 64, 64))
        else :
            text_surf2 = self.font.render(f"Game is a Draw", False, (64, 64, 64))
        text_rect2 = pygame.Surface.get_rect(text_surf2, midtop = (500, 300))
        self.screen.blit(text_surf1, text_rect1)
        self.screen.blit(text_surf2, text_rect2)
        leaderboard_surf = self.font.render("How to sort leaderboard", False, (0, 0, 0))
        leaderboard_rect = pygame.Surface.get_rect(leaderboard_surf, midtop = (500, 400))
        self.screen.blit(leaderboard_surf, leaderboard_rect)
        self.option1_surf = self.font.render(" Wins ", False, (0, 0, 0))
        self.option2_surf = self.font.render(" Losses ", False, (0, 0, 0))
        self.option3_surf = self.font.render(" W/L ratio ", False, (0, 0, 0))
        self.option1_rect = pygame.Surface.get_rect(self.option1_surf, midtop = (300, 600))
        self.option2_rect = pygame.Surface.get_rect(self.option2_surf, midtop = (480, 600))
        self.option3_rect = pygame.Surface.get_rect(self.option3_surf, midtop = (710, 600))
        self.screen.blit(self.option1_surf, self.option1_rect)
        self.screen.blit(self.option2_surf, self.option2_rect)
        self.screen.blit(self.option3_surf, self.option3_rect)
    def leaderboard(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.option1_rect.collidepoint(mouse_pos):
            return "wins"
        if self.option2_rect.collidepoint(mouse_pos):
            return "losses"
        if self.option3_rect.collidepoint(mouse_pos):
            return "ratio"
        return "Nothing"
    def released(self):
        if pygame.mouse.get_pressed() == (True, False, False):
            return False
        return True