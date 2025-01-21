if __name__ == '__main__':

    x = 2
    y = "Ahoj LALALA"

    print(x)
    print(type(x), type(y))
    print(len(y))

    a = [1, 4, "bob", 5, 5, 6, 5]
    print(a)
    print(len(a))

    s = {1, 2, 3, 4, 4, 4, 4}
    print(s)

    print(set(a))

import pygame
import random
import sys

# Inicializace Pygame
pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Barvy
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Nastavení Pac-Mana
pacman_size = 20
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_speed = 4

# Nastavení nepřátel
enemy_size = 20
enemy_speed = 2
num_enemies = 4
enemies = []
for _ in range(num_enemies):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT - enemy_size)
    enemies.append({"rect": pygame.Rect(x, y, enemy_size, enemy_size), "dir": [enemy_speed, enemy_speed]})

# Tečky k sebrání
dots = []
for i in range(10, WIDTH, 40):
    for j in range(10, HEIGHT, 40):
        dots.append(pygame.Rect(i, j, 8, 8))

# Herní smyčka
clock = pygame.time.Clock()
running = True
direction = (0, 0)

while running:
    # Události
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ovládání
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -pacman_speed)
    elif keys[pygame.K_DOWN]:
        direction = (0, pacman_speed)
    elif keys[pygame.K_LEFT]:
        direction = (-pacman_speed, 0)
    elif keys[pygame.K_RIGHT]:
        direction = (pacman_speed, 0)

    # Pohyb Pac-Mana
    pacman_x += direction[0]
    pacman_y += direction[1]

    # Omezení pohybu na okno
    pacman_x = max(0, min(WIDTH - pacman_size, pacman_x))
    pacman_y = max(0, min(HEIGHT - pacman_size, pacman_y))

    # Pohyb nepřátel
    for enemy in enemies:
        enemy_rect = enemy["rect"]
        enemy_dir = enemy["dir"]

        # Pohyb nepřítele
        enemy_rect.x += enemy_dir[0]
        enemy_rect.y += enemy_dir[1]

        # Změna směru při nárazu na stěnu
        if enemy_rect.left <= 0 or enemy_rect.right >= WIDTH:
            enemy_dir[0] = -enemy_dir[0]
        if enemy_rect.top <= 0 or enemy_rect.bottom >= HEIGHT:
            enemy_dir[1] = -enemy_dir[1]

    # Detekce kolizí mezi Pac-Manem a tečkami
    pacman_rect = pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)
    dots = [dot for dot in dots if not pacman_rect.colliderect(dot)]

    # Detekce kolizí s nepřáteli
    for enemy in enemies:
        if pacman_rect.colliderect(enemy["rect"]):
            print("Prohra! Narazil jsi do nepřítele.")
            running = False

    # Vykreslení
    win.fill(BLACK)
    pygame.draw.ellipse(win, YELLOW, pacman_rect)  # Pac-Man
    for dot in dots:
        pygame.draw.ellipse(win, WHITE, dot)  # Tečky
    for enemy in enemies:
        pygame.draw.rect(win, RED, enemy["rect"])  # Nepřátelé

    pygame.display.flip()

    # Konec hry, pokud jsou všechny tečky sebrány
    if not dots:
        print("Vítězství! Sebral jsi všechny body!")
        running = False

    clock.tick(30)

# Ukončení hry
pygame.quit()
sys.exit()

