import pygame
pygame.init()
 
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while True:
    for event in pygame.event.get():
	        axes = joystick.get_numaxes()
	        for i in range(axes):
	            axis = joystick.get_axis(i)
        	    print("Axis {} value: {:>6.3f}".format(i, axis))
            
	        buttons = joystick.get_numbuttons()
	        for i in range(buttons):
        	    button = joystick.get_button(i)
	            print("Button {:>2} value: {}".format(i,button))
            
	        hats = joystick.get_numhats()
	        print("Number of hats: {}".format(hats))

	        for i in range( hats ):
	            hat = joystick.get_hat( i )
        	    print("Hat {} value: {}".format(i, str(hat)))
