import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Constantes
LARGURA, ALTURA = 448, 496
FPS = 60
TAMANHO_BLOCO = 16
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)

# Criação da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Carregando o labirinto
labirinto = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Posição inicial do Pac-Man
pacman_x = 13 * TAMANHO_BLOCO
pacman_y = 23 * TAMANHO_BLOCO
velocidade = TAMANHO_BLOCO // 4
direcao_x = 0
direcao_y = 0

def desenhar_labirinto():
    for y, linha in enumerate(labirinto):
        for x, caractere in enumerate(linha):
            if caractere == "#":
                pygame.draw.rect(tela, AZUL, (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))
            elif caractere == ".":
                pygame.draw.circle(tela, (255, 255, 255), (x * TAMANHO_BLOCO + TAMANHO_BLOCO // 2, y * TAMANHO_BLOCO + TAMANHO_BLOCO // 2), 2)
            elif caractere == "o":
                pygame.draw.circle(tela, (255, 255, 255), (x * TAMANHO_BLOCO + TAMANHO_BLOCO // 2, y * TAMANHO_BLOCO + TAMANHO_BLOCO // 2), 5)

# Loop principal
while True:
    tela.fill(PRETO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                direcao_x = -velocidade
                direcao_y = 0
            elif evento.key == pygame.K_RIGHT:
                direcao_x = velocidade
                direcao_y = 0
            elif evento.key == pygame.K_UP:
                direcao_x = 0
                direcao_y = -velocidade
            elif evento.key == pygame.K_DOWN:
                direcao_x = 0
                direcao_y = velocidade

    # Atualizar posição
    novo_x = pacman_x + direcao_x
    novo_y = pacman_y + direcao_y
    col = novo_x // TAMANHO_BLOCO
    lin = novo_y // TAMANHO_BLOCO

    if labirinto[lin][col] != "#":
        pacman_x = novo_x
        pacman_y = novo_y

    # Desenhar tudo
    desenhar_labirinto()
    pygame.draw.circle(tela, AMARELO, (pacman_x + TAMANHO_BLOCO // 2, pacman_y + TAMANHO_BLOCO // 2), TAMANHO_BLOCO // 2)

    pygame.display.update()
    clock.tick(FPS)
