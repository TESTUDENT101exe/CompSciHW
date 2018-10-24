import pygame

screen = pygame.display.set_mode((500,500))
y=110
running =True
drawn=False
screen.fill((255,255,255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while drawn==False:
        for i in range(0,5):
            if i==1 or i==3:
                x=180
                for g in range(0,2):
                    pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
                    x+=100
            elif i==0 or i==2 or i==4:
                x=130
                for j in range(0,3):
                    pygame.draw.rect(screen, (0, 0, 0), ((x, y), (50, 50)))
                    x+=100
            y+=50
        drawn=True
    pygame.display.update()
pygame.quit()

