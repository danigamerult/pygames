# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("-----------")
    for i in range(3):
        print(f"| {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
        print("-----------")

# Função para verificar se alguém ganhou
def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:  # Linhas
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:  # Colunas
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:  # Diagonal principal
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:  # Diagonal secundária
        return True
    
    return False

# Função para verificar se o tabuleiro está cheio
def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        if ' ' in linha:
            return False
    return True

# Função principal do jogo
def jogar():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}")
        
        # Solicita a jogada do jogador
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))
        
        # Verifica se a posição está livre
        if tabuleiro[linha][coluna] != ' ':
            print("Essa posição já está ocupada. Tente novamente.")
            continue
        
        # Marca a jogada no tabuleiro
        tabuleiro[linha][coluna] = jogador_atual
        
        # Verifica se o jogador ganhou
        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        
        # Verifica se o tabuleiro está cheio (empate)
        if tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        
        # Alterna para o próximo jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Inicia o jogo
jogar()
