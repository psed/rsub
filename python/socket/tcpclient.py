import socket, pygame

pygame.init()
 
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
 
def Main():
	host = '127.0.0.1'
	port = 5000
 
	mySocket = socket.socket()
	mySocket.connect((host,port))

	message = ''
	while True:
		for event in pygame.event.get():
			axes = joystick.get_numaxes()
			for i in range(axes):
				axis = joystick.get_axis(i)
				message += "{:>6.3f}".format(axis)

			buttons = joystick.get_numbuttons()
			for i in range(buttons):
				button = joystick.get_button(i)
				message += str(button)

			hats = joystick.get_numhats()
			for i in range( hats ):
				hat = joystick.get_hat(i)
				message += str(hat)

			mySocket.send(message.encode())
#			data = mySocket.recv(1024).decode()
#			print ('Received from server: ' + data)
                 
	mySocket.close()
 
if __name__ == '__main__':
    Main()