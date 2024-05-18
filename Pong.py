'''''''''''IMPORTS'''''''''
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.collision import *
import random

'''''''''''VARIÁVEIS'''''''''
#Variáveis Numéricas
aux = False
cont = 0
velocidadex = 500
velocidadey = 500
num = random.randint(0,2)

# Obter a resolução da tela
resolution = pygame.display.Info()

# Definindo os sprites
bola = Sprite("Imagens/bola.png", 1)

# Criando a Janela
janela = Window(resolution.current_w, 700)

#1 Função que gera o cenário
def gerando_cenário():
    if cont == 0:
        
        # Cor da Janela
        janela.set_background_color([255,174,183])

        # Desenhando os sprites
        bola.draw()

#2 Definição das posições iniciais
def posicoes():
        bola.set_position((janela.width - bola.width)/2, (janela.height - bola.height)/2)

        return ()


#3 Função dque recebe as entradas do teclado
def inputs(aux):
    if(teclado.key_pressed("ESC")): 
        janela.close()
        
    # Inicilização do jogo
    if(teclado.key_pressed("space") == True):
        aux = True

    return(aux)


#4 "Play"
def inicializacao_de_rodada(num, aux, velocidadey, velocidadex, bolax, bolay):

    # Condições Iniciais
    if(aux == True):

        #Bola começa a andar
        bolax += velocidadex * janela.delta_time()
        bolay += velocidadey * janela.delta_time()
        
        #Bola quica na parede de cima e de baixo
        num, bolay, velocidadex, velocidadey, bolax = contem_sem_patinacao(num, bolay, velocidadex, velocidadey,bolax)

    return num, aux, velocidadey, velocidadex, bolax, bolay


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
    
    if bolax <= 0:
        bolax = 0
        velocidadex *= -1

    if (bolax + bola.width) > janela.width:
        velocidadex *= -1

    
        
    return num, bolay, velocidadex, velocidadey, bolax

# Inicialidando o recebimento de entrada do teclado
teclado = Window.get_keyboard()

#Inicializando a posicao
posicoes()


while True:
    
    #Gerando número aleatório para movimentação da bola
    num = random.randint(0,50)

    #Pegando entradas
    aux = inputs(aux)

    #Inicializando rodada
    num, aux, velocidadey, velocidadex, bola.x, bola.y = inicializacao_de_rodada(num, aux, velocidadey, velocidadex, bola.x, bola.y)
    

    # Cenário é criado
    gerando_cenário()
   

    # Atualizando a tela
    janela.update()