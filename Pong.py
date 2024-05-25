'''''''''''IMPORTS'''''''''
from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameimage import *
from PPlay.mouse import *
import random



'''''''''''VARIÁVEIS'''''''''

# Variáveis Numéricas
velocidade_pad = 550
cont = 2
aux = False
velocidadex = 500
velocidadey = 500
player_score_1 = 0
player_score_2 = 0
movimentacao_inicial = random.randint(0,2)
colisoes_barra = random.randint(1,8)
pad_anda = 0

# Variáveis de texto
jogador1 = input("Digite o nome do primeiro jogador: ")
jogador2 = "Computador"
padRightNormal = "Imagens/pad-right-normal.png"
padRightMetade = "Imagens/pad-right-metade.png"
padLeftNormal = "Imagens/pad-left-normal.png"
padLeftMetade = "Imagens/pad-left-metade.png"

# Definindo os sprites
bola = Sprite("Imagens/bola.png", 1)
pad_left = Sprite(padLeftNormal, 1)
pad_right = Sprite(padRightNormal, 1)
plano_de_fundo = Sprite("Imagens/plano-de-fundo.jpg", 1)
plano_de_fundo_menu = Sprite("Imagens/plano-de-fundo-menu.jpg", 1)
botao_play = Sprite("Imagens/botao-play.png", 1)
botao_play_hover = Sprite("Imagens/botao-play-hover.png", 1)

# Definindo a fonte
font = pygame.font.SysFont("Arial", 100, bold=True, italic=True)

# Obter a resolução da tela
resolution = pygame.display.Info()

# Criando a Janela
janela = Window(resolution.current_w, resolution.current_h)

# Inicialidando o recebimento de entrada do teclado
teclado = Window.get_keyboard()

# Inicialidando o recebimento de entrada do mouse
mouse_object = Window.get_mouse()

# Definindo as paredes da janela
par_esq = 0
par_bai = janela.height
par_dir = float(janela.width - bola.width)
par_cima = 0



'''''''''''FUNÇÕES'''''''''

def menu(cont):
    if cont == 2:

        hover_button = mouse_object.is_over_object(botao_play)
        click = mouse_object.is_button_pressed(1)

        # Desenhando os sprites
        plano_de_fundo_menu.draw()           

        if hover_button == True:
            botao_play_hover.draw()
            botao_play_hover.set_position((janela.width - botao_play.width)/2, (janela.height - botao_play.height)/2)
            if click == True:
                cont = 0

        if hover_button == False: 
            botao_play.draw()
            botao_play.set_position((janela.width - botao_play.width)/2, (janela.height - botao_play.height)/2)

    
    return cont

                


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
        janela.draw_text(f"{jogador1}: {player_score_1}", 100, 50, size=50, color=(151, 0, 71), font_name="Arial", bold=True, italic=True)
        janela.draw_text(f"{jogador2}: {player_score_2}", janela.width - (len(jogador2)*24) -  200, 50, size=50, color=(151, 0, 71), font_name="Arial", bold=True, italic=True)



#2 Definição das posições de início de partida
def posicoes():
        bola.set_position((janela.width - bola.width)/2, (janela.height - bola.height)/2)
        pad_left.set_position((1.5), (janela.height - pad_left.height)/2)
        pad_right.set_position((janela.width - pad_right.width), (janela.height - pad_right.height)/2)

        return ()



#3 Função dque recebe as entradas do teclado
def inputs(velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2, cont):
    if aux == True:
        # Movimentação dos pads
        if(teclado.key_pressed("w") == True):
            if pad_left.y >= 10:
                pad_left.y += - velocidade_pad * janela.delta_time()

        if(teclado.key_pressed("s") == True):
            if pad_left.y <= par_bai - pad_left.height -8:
                pad_left.y += velocidade_pad * janela.delta_time()
        
        
        '''if(teclado.key_pressed("UP") == True):
            if pad_right.y >= 10:
                pad_right.y += - velocidade_pad * janela.delta_time()

        if(teclado.key_pressed("DOWN") == True):
            if pad_right.y <= par_bai - pad_right.height -7:
                pad_right.y += velocidade_pad * janela.delta_time()'''
            
    # Inicilização do jogo
    if(teclado.key_pressed("space") == True):
        aux = True

    # Fechamento do jogo
    if(teclado.key_pressed("ESC")): 
        janela.close()
    
    # Reinicialização do jogo
    if(teclado.key_pressed("r")): 
        aux = False
        velocidadex = 500
        velocidadey = 500
        player_score_1 = 0
        player_score_2 = 0
        #jogador1 = input("Digite o nome do primeiro jogador: ")
        #jogador2 = input("Digite o nome do segundo jogador: ")
        aux == True
        bolay = bola.y
        janela.update
        cont = 2
        cont = menu(cont)

    return(velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2, cont)



#4 "Play"
def inicializacao_de_rodada(aux, velocidadey, velocidadex, bolax, bolay):

    # Condições Iniciais
    if(aux == True):
        #Bola começa a andar
        bolax += velocidadex * janela.delta_time()
        bolay += velocidadey * janela.delta_time()

    return aux, velocidadey, velocidadex, bolax, bolay



#5 Checa se colidiu com as barras, e então chama a função que faz a bola quicar
def colisao_barras(velocidadex, colisoes_barra):
    if Collision.collided(bola, pad_right):
        colisoes_barra = random.randint(1, 4)
        bola.x = par_dir - pad_right.width
        velocidadex *= -1

    if Collision.collided(bola, pad_left):
        colisoes_barra = random.randint(1, 4)
        bola.x = par_esq + pad_left.width
        velocidadex *= -1  
            
    return(velocidadex, colisoes_barra)



#6 Colisão com as paredes
def colidindo_paredes(velocidadex, velocidadey, player_score_1, player_score_2, aux, colisoes_barra):
    if (bola.x >= par_dir or bola.x <= par_esq):
        colisoes_barra = random.randint(1, 4)
        #Colidiu com a parede direita - pontuacao jogador 1
        if(bola.x >= par_dir):
            player_score_1 += 1
        #Colidiu com a parede esquerda - pontuacao jogador 2 
        if(bola.x <= par_esq):
            player_score_2 += 1
        
        #A cada colisão, aumenta a velocidade da bola
        velocidadex = velocidadex * 1.05
        velocidadey = velocidadey * 1.05
        
        #Bola para de andar
        aux = False

        #Posições voltam ao estágio inicial
        posicoes()

        # Para qual lado a bola irá andar na nova partida é definido
        movimentacao_inicial = random.randint(0,3)
        if movimentacao_inicial % 2 == 0:
            velocidadex *= -1
        
    return (velocidadex, velocidadey, player_score_1, player_score_2, aux, colisoes_barra)



#7 Contendo a Bola dentro da Janela sem Patinação
def contem_sem_patinacao(velocidadey, colisoes_barra):

    #Se a posição y da bola for menor ou igual que a parede de cima (0) + a altura da bola, bola não irá ultrapassar o limite da tela e inverta a velocidade de y
    if bola.y <= 2:
        colisoes_barra = random.randint(1, 4)
        bola.y = 10
        velocidadey *= -1
  
    #Se a posição y da bola for maior que a parede de baixo - a altura da bola, bola não irá ultrapassar o limite da tela e inverta a velocidade de y
    if((bola.y + bola.height) > janela.height):
        colisoes_barra = random.randint(1, 4)
        bola.y = janela.height - bola.height
        velocidadey *= -1
    
    '''Para quicar nas paredes do lado também
    if bolax <= 0:
        bolax = 0
        velocidadex *= -1

    if (bolax + bola.width) > janela.width:
        velocidadex *= -1'''

    return velocidadey, colisoes_barra



#8 IA

def ia(pad_anda):
    if aux == True:
        if bola.x > janela.width - (janela.width/colisoes_barra):
            pad_anda = 1

        if pad_anda == 1:
            if(pad_right.y > bola.y):
                if pad_right.y >= 10:
                    pad_right.y += - velocidade_pad * janela.delta_time()


            elif(pad_right.y < bola.y):
                if pad_right.y < par_bai - pad_right.height -7:
                    pad_right.y += velocidade_pad * janela.delta_time()
        
        pad_anda = 0

    return(pad_anda)



#9 Função que renderiza o texto de vitoria
def texto_vitoria(jogador):
    #Definindo o texto
    text_surface = font.render(f"{jogador} venceu", True, (151, 0, 71))
    #Definindo tamamnho do texto
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    #Definindo posição do texto
    text_x = (janela.width - text_width) // 2
    text_y = (janela.height - text_height) // 2
    #Printando texto na tela
    janela.screen.blit(text_surface, (text_x, text_y))

#10 Checando se algum dos jogadores chegou a 10 pontos
def checa_finalização(cont):
    if(player_score_1 >= 10):
        cont = 1
        finalizacao(jogador1)
    elif(player_score_2 >= 10):
        cont = 1
        finalizacao(jogador2)

    
    return (cont)
    
#11 Finalização do jogo
def finalizacao(vencedor):
    plano_de_fundo.draw()
    texto_vitoria(vencedor)
    janela.update()
        
    return ()  




''' EXECUÇÃO '''

#Inicializando a posicao
posicoes()

while True:
    
    #Gerando número aleatório para movimentação da bola
    num = random.randint(0,50)

    cont = menu(cont)

    #Pegando entradas
    velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2, cont = inputs(velocidadex, velocidadey, player_score_1, player_score_2, aux, jogador1, jogador2, cont)
    
    # Colisão com as barras
    velocidadex, colisoes_barra = colisao_barras(velocidadex, colisoes_barra)
    
    #Inicializando rodada
    aux, velocidadey, velocidadex, bola.x, bola.y = inicializacao_de_rodada( aux, velocidadey, velocidadex, bola.x, bola.y)
    
    #Ia trabahando 
    pad_anda = ia(pad_anda)
    
    #Bola quica na parede de cima e de baixo
    velocidadey, colisoes_barra = contem_sem_patinacao(velocidadey, colisoes_barra)
    
    # Colisão com as paredes
    velocidadex, velocidadey, player_score_1, player_score_2, aux, colisoes_barra = colidindo_paredes(velocidadex, velocidadey, player_score_1, player_score_2, aux, colisoes_barra)
    
    #Checando a finalização, e se sim, finalizando
    cont = checa_finalização(cont)
    print (cont)
    # Cenário é criado
    gerando_cenário()
    
    # Atualizando a tela
    janela.update()