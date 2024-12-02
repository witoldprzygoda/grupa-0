import pygame, sys

pygame.init()
 
def main():
	clock = pygame.time.Clock()

	pygame.display.set_caption('Zadanie 1 - piłka i grawitacja!')
	icon = pygame.image.load('favicon.ico')
	pygame.display.set_icon(icon)
	 
	pygame.mixer.music.load(r'music.mp3')
	pygame.mixer.music.play(-1)
 
	size = width, height = 800, 800
	screen = pygame.display.set_mode(size)

	speed = [0, 0]
	accel = [0.1, 0.1]

	image=pygame.image.load(r'moon.jpg')
	image = pygame.transform.scale(image, size)
 
	surf_center = (
		(width-image.get_width())/2,
		(height-image.get_height())/2
	)
 
	screen.blit(image, surf_center)
	ball = pygame.image.load('ball.gif')
	ball = pygame.transform.scale(ball, (ball.get_width()//2, ball.get_height()//2))
 
	screen.blit(ball, (width/2, height/2))
 
	ballrect = ball.get_rect(center=(width/2, height/2))
	pygame.display.flip()

	while True:
		clock.tick(60)
		pygame.time.delay(50)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]: sys.exit()

			if keys[pygame.K_UP]:
				pass # zamienić na jakieś przeliczenie
			elif keys[pygame.K_DOWN]:
				pass
			elif keys[pygame.K_LEFT]:
				pass
			elif keys[pygame.K_RIGHT]:
				pass
    
			ballrect = ballrect.move(speed)
			if ballrect.left < 0 or ballrect.right > width:
				speed[0] = -speed[0]
			if ballrect.top < 0 or ballrect.bottom > height:
				speed[1] = -speed[1]
 
			screen.blit(image,surf_center)
			screen.blit(ball,ballrect)
			pygame.display.flip()


 
if __name__ == '__main__':
	main()
	pygame.quit()
	sys.exit()
