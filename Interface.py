import pygame
import os


pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 720
GRID_WIDTH = WIDTH // 8
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Five In Row")
movements = []

FPS = 30
clock = pygame.time.Clock()


base_folder = os.path.dirname(__file__)
img_folder = os.path.join(base_folder, 'images')
background_img = pygame.image.load(os.path.join(img_folder, 'back.png')).convert()



def draw_background(surf):

    surf.blit(background_img, (0, 0))


    rect_lines = [
        ((GRID_WIDTH, GRID_WIDTH), (GRID_WIDTH, HEIGHT - GRID_WIDTH)),
        ((GRID_WIDTH, GRID_WIDTH), (WIDTH - GRID_WIDTH, GRID_WIDTH)),
        ((GRID_WIDTH, HEIGHT - GRID_WIDTH),
            (WIDTH - GRID_WIDTH, HEIGHT - GRID_WIDTH)),
        ((WIDTH - GRID_WIDTH, GRID_WIDTH),
            (WIDTH - GRID_WIDTH, HEIGHT - GRID_WIDTH)),
    ]
    for line in rect_lines:
        pygame.draw.line(surf, BLACK, line[0], line[1], 2)


    for i in range(5):
        pygame.draw.line(surf, BLACK,
                         (GRID_WIDTH * (2 + i), GRID_WIDTH),
                         (GRID_WIDTH * (2 + i), HEIGHT - GRID_WIDTH))
        pygame.draw.line(surf, BLACK,
                         (GRID_WIDTH, GRID_WIDTH * (2 + i)),
                         (HEIGHT - GRID_WIDTH, GRID_WIDTH * (2 + i)))







def add_coin(screen, pos, color):
    movements.append(((HEIGHT//pos[0] * GRID_WIDTH, WIDTH//pos[1] * GRID_WIDTH), color))
    pygame.draw.circle(screen, color,
        (HEIGHT//pos[0] * GRID_WIDTH, WIDTH//pos[1] * GRID_WIDTH), 16)

def draw_movements(screen):
    for m in movements:
        pygame.draw.circle(screen, m[1], m[0], 16)







running = True
while running:

    clock.tick(FPS)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            print(pos)

            grid = (int(round(pygame.mouse.get_pos()[0] / (GRID_WIDTH + .0))),
                int(round(pygame.mouse.get_pos()[1] / (GRID_WIDTH + .0))))
            add_coin(screen, pos, BLACK)
            print(movements)


    draw_background(screen)
    # draw_movements(screen)
    
    pygame.display.flip()