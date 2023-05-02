import pygame
import pygame.camera
from pygame.locals import *
pygame.init()
print('cam init...')
pygame.camera.init()
print('cam find...')
#cameras = pygame.camera.list_cameras()
#print(cameras)

naklon = 0.8
sdvig = 0
shirPolos = 20

width = 320
height = 240
size = (width,height)

cam = pygame.camera.Camera(0, size)
print('cam start...')
cam.start()
print('window setup...')
window = pygame.display.set_mode((320,240*2 ))
snapshot = pygame.surface.Surface(size, 0, window)

graphic = pygame.surface.Surface(size, 0, window)
print('cycle')
while True:
    # опрос событий, обработка событий 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
             cam.stop()
             pygame.quit()
             exit()
    #получение кортинки
    snapshot = cam.get_image(snapshot)
    graphic.fill((0,0,0))
    #анализ изображения
    for x in range(0,width//2):
        y = int(-naklon*x + height-sdvig - 1)
        if y<0:
            y=0
        pos =(x,y)
        color = snapshot.get_at(pos) # считываем цвет пикселя на изображении snapshot и сохроняем значение цвета в переменную color 

        Yarkost = height*(color[0]+ color[1]+color[2])//(255*3)
        pointColor =(255,255,255)
        posG = (x,Yarkost)
        graphic.set_at(posG,pointColor )
        
        #вывод изображений на экран
        #print(color) # печатаем в консоль цвет анализироемого пикселя
        snapshot.set_at(pos, pointColor) # закрашиваем пиксель на изображении snapshot на позиции pos цветом pointColor ( что бы понимать где м ищем свет на картинке snapshot)
        
    window.blit(snapshot,(0,0))
    window.blit(graphic,(0,240))
    pygame.display.update()



"""


while True:
    snapshot = cam.get_image(snapshot)
    #graphik.set_at((40,20), (255,250,250))
    window.blit(snapshot, (0,0))
    pygame.display.flip()
    """
