import pygame
import random

# Inicializar o pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Definir tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Tiro Melhorado")

# Definir o FPS
clock = pygame.time.Clock()
FPS = 60

# Carregar imagens
player_img = pygame.image.load('player.png')  # Substitua com o caminho da sua imagem
enemy_img = pygame.image.load('enemy.png')    # Substitua com o caminho da sua imagem
bullet_img = pygame.Surface((5, 10))
bullet_img.fill(RED)

# Classe para o Jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Classe para os tiros
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Classe para os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 5)
        self.player = None

    def follow_player(self):
        if self.player:
            # Movimento simples de perseguição
            if self.rect.centerx < self.player.rect.centerx:
                self.rect.x += 2
            elif self.rect.centerx > self.player.rect.centerx:
                self.rect.x -= 2

            if self.rect.centery < self.player.rect.centery:
                self.rect.y += 2
            elif self.rect.centery > self.player.rect.centery:
                self.rect.y -= 2

    def update(self):
        self.follow_player()
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 50)
            self.rect.y = random.randint(-100, -40)

# Função principal do jogo
def game_loop():
    running = True
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(5):
        enemy = Enemy()
        enemy.player = player  # Passar o jogador para os inimigos seguirem
        all_sprites.add(enemy)
        enemies.add(enemy)

    while running:
        clock.tick(FPS)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # Atualizar sprites
        all_sprites.update()

        # Checar colisão entre tiros e inimigos
        for bullet in bullets:
            enemy_hit = pygame.sprite.spritecollide(bullet, enemies, True)
            for enemy in enemy_hit:
                bullet.kill()  # Destruir o tiro
                enemy = Enemy()  # Criar novo inimigo
                enemy.player = player
                all_sprites.add(enemy)
                enemies.add(enemy)

        # Preencher a tela com fundo branco
        screen.fill(WHITE)

        # Desenhar todos os sprites
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()

# Iniciar o jogo
game_loop()