import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Roguelike Splash Screen')

def show_splash():
    font = pygame.font.Font(None, 74)
    text = font.render('Meu Roguelike', True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()

    pygame.quit()

show_splash()