import pygame

pygame.init()

screenInfo = pygame.display.Info()
dim = screenInfo.current_h/15
color = (255, 255, 255)

screen = pygame.display.set_mode((dim, dim), pygame.NOFRAME)
screen.fill(color)
pygame.display.flip()  

movingW = False
movingA = False
movingS = False
movingD = False

posX = screenInfo.current_w/2
posY = screenInfo.current_h/2
velX = screenInfo.current_w/10000
velY = screenInfo.current_h/10000

running = True
while running:
    pygame.display.set_window_position((posX-dim/2, posY-dim/2)) # update movement

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # key pressed down

            if event.key == pygame.K_ESCAPE: # exits the program
                running = False

            if event.key == pygame.K_w: 
                movingW = True
            if event.key == pygame.K_a:
                movingA = True    
            if event.key == pygame.K_s:
                movingS = True
            if event.key == pygame.K_d:
                movingD = True   
        
        if event.type == pygame.KEYUP: # key NOT pressed down

            if event.key == pygame.K_w:
                movingW = False
            if event.key == pygame.K_a:
                movingA = False
            if event.key == pygame.K_s:
                movingS = False
            if event.key == pygame.K_d:
                movingD = False

    if movingW == True: # change position
        posY-=velY
    if movingS == True:
        posY+=velY
    if movingA == True:
        posX-=velX
    if movingD == True:
        posX+=velX

    if posX > screenInfo.current_w-dim/2: # over the edge check
        posX = screenInfo.current_w-dim/2
    if posX < 0+dim/2:
        posX = 0+dim/2

    if posY > screenInfo.current_h-dim/2:
        posY = screenInfo.current_h-dim/2
    if posY < 0+dim/2:
        posY = 0+dim/2

pygame.quit()