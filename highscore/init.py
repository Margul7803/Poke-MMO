import pygame
from High_Score_Module import highscore
pygame.init()

X = 480
Y = 400
WHITE = ((0,128,0))
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 16)
screen = pygame.display.set_mode((X, Y))
screen.fill(WHITE)

mon_score = 12345

highscore(screen, 'score_file.txt', mon_score)

txt_surf = font.render("Patientez quelques instants...", True, BLACK)
txt_rect = txt_surf.get_rect(center=(X//2, Y//2))
screen.blit(txt_surf, txt_rect)
pygame.display.flip()