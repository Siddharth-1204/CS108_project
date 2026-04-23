import pygame

class Analytics :
    def __init__(self, background, screen, font, game_name):
        self.background_surf = background
        self.screen = screen
        self.font = font
        self.game_name = game_name
    def display(self, player1, player2, winner)
        self.screen.blit(self.background_surf, (0,0))
        text_surf1 = self.font.render(f"{self.game_name} {player1} vs {player2}", False, "#6fa1d7")
        text_rect1 = pygame.Surface.get_rect(text_surf1, midtop = (500, 100))
        winner_name = player1 if winner == 0 else player2
        if winner != 0 :
            text_surf2 = self.font.render(f" Winner : {winner_name}", False, "#fdd56c")
        else :
            text_surf2 = self.font.render(f" Game is a Draw", False, "#fdd56c")
        text_rect2 = pygame.Surface.get_rect(text_surf2, midtop = (500, 200))
        self.screen.blit(text_surf1, text_rect1)
        self.screen.blit(text_surf2, text_rect2)
        leaderboard_surf = self.font.render("Leaderboard sorts", False, (0, 0, 0))
        leaderboard_rect = pygame.Surface.get_rect(leaderboard_surf, midtop = (500, 300))
        self.screen.blit(leaderboard_surf, leaderboard_rect)
        option1_surf = self.font.render("Wins", False, (0, 0, 0))
        option2_surf = self.font.render("Loses", False, (0, 0, 0))
        option3_surf = self.font.render("W/L ratio", False, (0, 0, 0))
        option1_rect = pygame.Surface.get_rect(option1_surf, midtop = (200, 400))
        option2_rect = pygame.Surface.get_rect(option2_surf, midtop = (500, 400))
        option3_rect = pygame.Surface.get_rect(option3_surf, midtop = (700, 400))
        self.screen.blit(option1_surf, option1_rect)
        self.screen.blit(option2_surf, option2_rect)
        self.screen.blit(option3_surf, option3_rect)

        