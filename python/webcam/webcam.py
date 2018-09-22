import pygame, sys
import pygame.camera
from pygame.locals import *
pygame.init()
pygame.camera.init()
screen = pygame.display.set_mode((320,240))
cam = pygame.camera.Camera("/dev/video4",(320,240))

cam.start()
while 1:
    image = cam.get_image()
    screen.blit(image,(0,0))
    pygame.display.set_caption(str("TUX PLOT CAM"))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()