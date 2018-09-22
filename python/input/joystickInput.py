import pygame
pygame.init()
 
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
    for event in pygame.event.get():

            command = ''
            axes = joystick.get_numaxes()
            for i in range(axes):
                command += str(joystick.get_axis(i)) + ','

            buttons = joystick.get_numbuttons()
            for i in range(buttons):
                command += str(joystick.get_button(i)) + ','

            hats = joystick.get_numhats()
            for i in range( hats ):
                command += str(joystick.get_hat(i)) + ','
            print(command)
