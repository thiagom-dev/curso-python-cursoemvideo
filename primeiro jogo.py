import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu primeiro jogo")

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()