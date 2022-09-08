import pygame 

pygame.init()
width = 800
height = 600
window=pygame.display.set_mode(size=(width, height))


running = True
while running:
        for event in pygame.event.get():
                if event.type ==pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE:
                                running=False
                if event.type==pygame.QUIT:
                        running = False
        window.fill("#9AE594")
        pygame.draw.circle(window,"#D2C567",(250,250),75)
        surf = pygame.Surface((50,50))
        surf.fill("#C45942")
        
        rect =surf.get_rect()
        window.blit(surf,(width/2,height/2))
        
        
        
        pygame.display.flip()

pygame.quit()