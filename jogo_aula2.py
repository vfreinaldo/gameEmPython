#Importando e iniciando a biblioteca pygame
import pygame
pygame.init()

#Declarando variáveis
x = 380
y = 300
velocidade = 10
fundo = pygame.image.load('pista.PNG')
carro = pygame.image.load('carro.PNG')

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
        
    #Criando movimentos no objeto
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
        
    #Atualiza a cor de fundo para não haver rastro do objeto   
    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))
    
    #Criando um objeto na tela        
    #pygame.draw.circle(janela, (0,240,15),(x,y),30)
    
    #Atualizando a tela
    pygame.display.update()
    
pygame.quit()
