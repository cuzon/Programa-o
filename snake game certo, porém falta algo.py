import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tamanho da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Tamanho do pinguim (cobra)
PENGUIN_SIZE = 20

# Tamanho da bandeira
FLAG_SIZE = 20

# Configuração da janela do jogo
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Relógio para controlar a taxa de atualização da tela
clock = pygame.time.Clock()

# Função para desenhar o pinguim (cobra)
def draw_penguin(penguin_body):
    for penguin in penguin_body:
        pygame.draw.rect(window, BLACK, [penguin[0], penguin[1], PENGUIN_SIZE, PENGUIN_SIZE])

# Função para desenhar a bandeira
def draw_flag(flag_x, flag_y):
    pygame.draw.rect(window, BLUE, [flag_x, flag_y, FLAG_SIZE, FLAG_SIZE])

# Função principal do jogo
def game_loop():
    game_over = False
    game_exit = False

    # Posição inicial do pinguim
    penguin_x = WINDOW_WIDTH / 2
    penguin_y = WINDOW_HEIGHT / 2

    # Velocidade do pinguim
    penguin_x_change = 0
    penguin_y_change = 0

    # Corpo do pinguim (cobra)
    penguin_body = []
    penguin_length = 1

    # Posição inicial da bandeira
    flag_x = round(random.randrange(0, WINDOW_WIDTH - FLAG_SIZE) / FLAG_SIZE) * FLAG_SIZE
    flag_y = round(random.randrange(0, WINDOW_HEIGHT - FLAG_SIZE) / FLAG_SIZE) * FLAG_SIZE

    while not game_exit:
        while game_over:
            window.fill(WHITE)
            font = pygame.font.SysFont(None, 25)
            game_over_text = font.render('Game Over! Pressione Q para sair ou C para jogar novamente.', True, BLACK)
            window.blit(game_over_text, (WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2))
            pygame.display.update()

            # Verifica eventos do teclado enquanto o jogo está no modo Game Over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    penguin_x_change = -PENGUIN_SIZE
                    penguin_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    penguin_x_change = PENGUIN_SIZE
                    penguin_y_change = 0
                elif event.key == pygame.K_UP:
                    penguin_y_change = -PENGUIN_SIZE
                    penguin_x_change = 0
                elif event.key == pygame.K_DOWN:
                    penguin_y_change = PENGUIN_SIZE
                    penguin_x_change = 0

        # Atualiza a posição do pinguim
        penguin_x += penguin_x_change
        penguin_y += penguin_y_change

        # Verifica se o pinguim saiu da tela
        if penguin_x >= WINDOW_WIDTH or penguin_x < 0 or penguin_y >= WINDOW_HEIGHT or penguin_y < 0:
            game_over = True

        # Verifica se o pinguim pegou a bandeira
        if penguin_x == flag_x and penguin_y == flag_y:
            # Gera uma nova posição para a bandeira
            flag_x = round(random.randrange(0, WINDOW_WIDTH - FLAG_SIZE) / FLAG_SIZE) * FLAG_SIZE
            flag_y = round(random.randrange(0, WINDOW_HEIGHT - FLAG_SIZE) / FLAG_SIZE) * FLAG_SIZE
            penguin_length += 1

        # Limpa a janela
        window.fill(WHITE)

        # Desenha o pinguim (cobra)
        penguin_head = []
        penguin_head.append(penguin_x)
        penguin_head.append(penguin_y)
        penguin_body.append(penguin_head)

        if len(penguin_body) > penguin_length:
            del penguin_body[0]

        # Verifica colisão com o próprio corpo
        for segment in penguin_body[:-1]:
            if segment == penguin_head:
                game_over = True

        # Desenha a bandeira
        draw_flag(flag_x, flag_y)

        # Desenha o pinguim
        draw_penguin(penguin_body)

        pygame.display.update()

        # Define a taxa de atualização da tela
        clock.tick(10)

    pygame.quit()
    quit()

# Inicia o jogo
game_loop()