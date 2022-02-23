#Importando e iniciando a biblioteca pygame
import pygame
from random import randint
pygame.init()


#Declarando variáveis
x = 375                #LIMITE MAXIMO=480 LIMITE MINIMO=250
y = 100
pos_x = 265
pos_y = 800
pos_y_a = 800
pos_y_c = 800
velocidade = 15
velocidade_outros = 10
timer = 0
tempo_segundo = 0

fundo = pygame.image.load('cenario.PNG')
carroamarelo = pygame.image.load('carroamarelo.PNG')
carropolicia = pygame.image.load('carropolicia.PNG')
carroambulancia = pygame.image.load('carroambulancia.PNG')
carrobranco = pygame.image.load('carrobranco.PNG')


font = pygame.font.SysFont('arial black', 30)
texto = font.render('Tempo: ', True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)


#Abrindo e renomeando a janela do jogo
janela_aberta = True
pygame.display.set_caption('Meu Primeiro Jogo')
janela = pygame.display.set_mode((800,600))


#Looping, mantendo a janela aberta até ser fechada pelo usuário.
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            janela_aberta = False
        
        
    #Criando movimentos no carro principal
    comandos = pygame.key.get_pressed()
    
    if comandos[pygame.K_RIGHT] and x <= 475:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 260:
        x -= velocidade
    
    
    #Criando a movimentação dos outros carros    
    if (pos_y <= -180) and (pos_y_a <= 180) and (pos_y_c <= 180):
        pos_y = randint (800,2000)
        pos_y_a = randint (800,2000)
        pos_y_c = randint (800,2000)

    #Executando o timer
    if (timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render('Tempo: ' + str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0
    
    #Ajuste de velocidade dos carros secundários
    pos_y -= velocidade_outros          #CARRO DA POLICIA
    pos_y_a -= velocidade_outros + 6    #CARRO BRANCO
    pos_y_c -= velocidade_outros + 2    #AMBULANCIA
           
        
    #Atualiza a cor de fundo para não haver rastro do objeto, bem como insere os carros em sua posição 
    #exata, de acordo com os parametros das variáveis.   
    janela.blit(fundo, (0,0))
    janela.blit(carroamarelo, (x,y))
    janela.blit(carropolicia, (pos_x,pos_y))
    janela.blit(carrobranco, (pos_x + 110,pos_y_a))
    janela.blit(carroambulancia, (pos_x + 217,pos_y_c))
    janela.blit(texto, pos_texto)
   
    #Criando um objeto na tela        
    #pygame.draw.circle(janela, (0,240,15),(x,y),30)
    
    #Atualizando a tela
    pygame.display.update()
    
pygame.quit()
