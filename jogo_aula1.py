#Importando e iniciando a biblioteca pygame
import pygame
pygame.init()

#Declarando variáveis
x = 400
y = 300
velocidade = 10


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
    janela.fill((0,0,0))
    
    #Criando um objeto na tela        
    pygame.draw.circle(janela, (0,240,15),(x,y),30)
    
    #Atualizando a tela
    pygame.display.update()
    
pygame.quit()
