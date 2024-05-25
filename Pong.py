'''''''''''IMPORTS'''''''''
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameimage import *
import random

'''''''''''VARIÁVEIS'''''''''

# Variáveis Numéricas
velocidade_pad = 800
cont = 0
aux = False
velocidadex = 500
velocidadey = 500
player_score_1 = 0
player_score_2 = 0
num = random.randint(0,2)

# Variáveis de texto
jogador1 = input("Digite o nome do primeiro jogador: ")
jogador2 = input("Digite o nome do segundo jogador: ")
padRightNormal = "Imagens/pad-right-normal.png"
padLeftNormal = "Imagens/pad-left-normal.png"

# Definindo os sprites
bola = Sprite("Imagens/bola.png", 1)
pad_left = Sprite(padLeftNormal, 1)
pad_right = Sprite(padRightNormal, 1)
plano_de_fundo = Sprite("Imagens/plano-de-fundo.jpg", 1)

# Definindo a fonte
font = pygame.font.SysFont("Arial", 100, bold=True, italic=True)

# Obter a resolução da tela
resolution = pygame.display.Info()

# Criando a Janela
janela = Window(resolution.current_w, resolution.current_h)

# Inicialidando o recebimento de entrada do teclado
teclado = Window.get_keyboard()

# Definindo as paredes da janela
par_esq = janela.height - janela.height
par_bai = janela.height
par_dir = float(janela.width - bola.width)
par_cima = 0

'''''''''''FUNÇÕES'''''''''

#1 Função que gera o cenário
def gerando_cenário():
    if cont == 0:
        
        # Cor da Janela
        janela.set_background_color([255,174,183])

        #Título da janela
        janela.set_title("Pong da Júlia")

        # Desenhando os sprites
        plano_de_fundo.draw()
        bola.draw()
        pad_left.draw()
        pad_right.draw()
        
        
        # Criando pontuação
        janela.draw_text(f"{jogador1}: {player_score_1}", 50, 50, size=50, color=(151, 0, 71), font_name="Arial", bold=True, italic=True)
        janela.draw_text(f"{jogador2}: {player_score_2}", 1600, 50, size=50, color=(151, 0, 71), font_name="Arial", bold=True, italic=True)



#2 Definição das posições de início de partida
def posicoes():
        bola.set_position((janela.width - bola.width)/2, (janela.height - bola.height)/2)
        pad_left.set_position((1.5), (janela.height - pad_left.height)/2)
        pad_right.set_position((janela.width - pad_right.width), (janela.height - pad_right.height)/2)

        return ()


#3 Função dque recebe as entradas do teclado
def inputs(pad_left, pad_right, velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2):

    # Movimentação dos pads
    if(teclado.key_pressed("w") == True):
        if pad_left.y >= 10:
            pad_left.y += - velocidade_pad * janela.delta_time()

    if(teclado.key_pressed("s") == True):
        if pad_left.y <= par_bai - pad_left.height -8:
            pad_left.y += velocidade_pad * janela.delta_time()
    
    if(teclado.key_pressed("UP") == True):
        if pad_right.y >= 10:
            pad_right.y += - velocidade_pad * janela.delta_time()

    if(teclado.key_pressed("DOWN") == True):
        if pad_right.y <= par_bai - pad_right.height -7:
            pad_right.y += velocidade_pad * janela.delta_time()
        
    # Inicilização do jogo
    if(teclado.key_pressed("space") == True):
        aux = True

    # Fechamento do jogo
    if(teclado.key_pressed("ESC")): 
        janela.close()
    
    # Reinicialização do jogo
    if(teclado.key_pressed("r")): 
        aux = False
        velocidadex = 600
        velocidadey = 600
        player_score_1 = 0
        player_score_2 = 0
        #jogador1 = input("Digite o nome do primeiro jogador: ")
        #jogador2 = input("Digite o nome do segundo jogador: ")
        aux == True
        janela.update

    return(pad_left, pad_right, velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2)


#4 "Play"
def inicializacao_de_rodada(aux, velocidadey, velocidadex, bolax, bolay):

    # Condições Iniciais
    if(aux == True):

        #Bola começa a andar
        bolax += velocidadex * janela.delta_time()
        bolay += velocidadey * janela.delta_time()

    return aux, velocidadey, velocidadex, bolax, bolay

#6 Função que faz a bola quicar ao tocar nas barras
def quicando_barras(velocidadex, velocidadey):

    #Numa alta probabilidade, mude as duas direções ao colidir
    if (num < 30):
        velocidadex *= -1
        velocidadey *= -1

    #Numa pequena probabilidade, mude apenas a velocidade y
    else:
        velocidadex *= -1  
    
    return(velocidadex, velocidadey)

#7 Checa se colidiu com as barras, e então chama a função que faz a bola quicar
def colisao_barras(bolay, velocidadex, velocidadey):
    if Collision.collided(bola, pad_right) or Collision.collided(bola, pad_left):
        velocidadex, velocidadey = quicando_barras(velocidadex, velocidadey)
            
    return(bolay, velocidadex, velocidadey)

#9 Colisão com as paredes
def colidindo_paredes(velocidadex, velocidadey, pad_right, pad_left, player_score_1, player_score_2, aux):
    if (bola.x >= par_dir or bola.x <= par_esq):
        #Colidiu com a parede direita - pontuacao jogador 1
        if(bola.x >= par_dir):
            player_score_1 += 1
        #Colidiu com a parede esquerda - pontuacao jogador 2 
        if(bola.x <= par_esq):
            player_score_2 += 1
        
        #A cada colisão, aumenta a velocidade da bola
        velocidadex = velocidadex * 1.05
        velocidadey = velocidadey * 1.05
        
        #Rodada termina
        aux = False

        posicoes()
        
    return (velocidadex, velocidadey, pad_right, pad_left, player_score_1, player_score_2, aux)

#10 Contendo a Bola dentro da Janela sem Patinação
def contem_sem_patinacao(num, bolay, velocidadex, velocidadey, bolax):

    #Se a posição y da bola for menor ou igual que a parede de cima (0) + a altura da bola, bola não irá ultrapassar o limite da tela e inverta a velocidade de y
    if bolay <= 2:
        bolay = 10
        velocidadey *= -1
  
    #Se a posição y da bola for maior que a parede de baixo - a altura da bola, bola não irá ultrapassar o limite da tela e inverta a velocidade de y
    if((bola.y + bola.height) > janela.height):
        bolay = janela.height - bola.height
        velocidadey *= -1
    
    '''Para quicar nas paredes do lado também
    if bolax <= 0:
        bolax = 0
        velocidadex *= -1

    if (bolax + bola.width) > janela.width:
        velocidadex *= -1'''

    
    return num, bolay, velocidadex, velocidadey, bolax


#Inicializando a posicao
posicoes()

while True:
    
    #Gerando número aleatório para movimentação da bola
    num = random.randint(0,50)

    #Pegando entradas
    pad_left, pad_right, velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2 = inputs(pad_left, pad_right, velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2)

    # Colisão com as barras
    bola.y, velocidadex, velocidadey = colisao_barras(bola.y, velocidadex, velocidadey)
    
    #Inicializando rodada
    aux, velocidadey, velocidadex, bola.x, bola.y = inicializacao_de_rodada( aux, velocidadey, velocidadex, bola.x, bola.y)

    #Bola quica na parede de cima e de baixo
    num, bola.y, velocidadex, velocidadey, bola.x = contem_sem_patinacao(num, bola.y, velocidadex, velocidadey, bola.x)

    # Colisão com as paredes
    (velocidadex, velocidadey, pad_right, pad_left, player_score_1, player_score_2, aux) = colidindo_paredes(velocidadex, velocidadey, pad_right, pad_left, player_score_1, player_score_2, aux)
    

    # Cenário é criado
    gerando_cenário()
   

    # Atualizando a tela
    janela.update()