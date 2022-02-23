#Importando e iniciando a biblioteca pygame
import pygame
pygame.init()


#Declarando variáveis
x = 378
y = 300
pos_x = 265
pos_y = 450
velocidade = 15
velocidade_outros = 10
fundo = pygame.image.load('cenario.PNG')
carroamarelo = pygame.image.load('carroamarelo.PNG')
carropolicia = pygame.image.load('carropolicia.PNG')
carroambulancia = pygame.image.load('carroambulancia.PNG')
carrobranco = pygame.image.load('carrobranco.PNG')


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
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    
    
    #Criando a movimentação dos outros carros    
    if (pos_y <= -200):
        pos_y = 600
    
    pos_y -= velocidade_outros
    
    if (pos_y <= -200):
        pos_y = 600
    
    pos_y -= velocidade_outros
    
    if (pos_y <= -200):
        pos_y = 600
    
    pos_y -= velocidade_outros
    
           
        
    #Atualiza a cor de fundo para não haver rastro do objeto, bem como insere os carros em sua posição 
    #exata, de acordo com os parametros das variáveis.   
    janela.blit(fundo, (0,0))
    janela.blit(carroamarelo, (x,y))
    janela.blit(carropolicia, (pos_x,pos_y))
    janela.blit(carrobranco, (pos_x + 110,pos_y))
    janela.blit(carroambulancia, (pos_x + 217,pos_y))
    
   
    #Criando um objeto na tela        
    #pygame.draw.circle(janela, (0,240,15),(x,y),30)
    
    #Atualizando a tela
    pygame.display.update()
    
pygame.quit()
