# Ball Physics in pygame

import pygame, asyncio
from random import randint

pygame.init()

class Ball:
	def __init__(self, x_pos, y_pos, radius, colour, mass, retention):
		self.pos = pygame.Vector2(x_pos, y_pos)
		self.radius = radius
		self.colour = colour
		self.speed = pygame.Vector2()
		self.mass = mass
		self.retention = retention
		self.circle = ''
		self.selected = False

	def check_select(self, mouse_pos, mouse_vel=(0,0)):
		if self.circle.collidepoint(mouse_pos):
			self.selected = True
		else:
			self.selected = False
		return self.selected

	def update_gravity(self):
		if not self.selected:
			if self.pos.y < WINDOWHEIGHT - self.radius - (wall_thickness/2):
				# apply gravity if in air
				self.speed.y += gravity
			else:
				# if ball hits the ground with enough speed not to stop
				if self.speed.y > bounce_limit:
					self.speed.y = self.speed.y * self.retention * -1
				else:
					if abs(self.speed.y) <= bounce_limit:
						# stop bouce if speed is less than bounce_limit
						self.speed.y = 0
			if (self.pos.x < 0 + self.radius + (wall_thickness/2) and self.speed.x < 0) or \
					(self.pos.x > WINDOWWIDTH - self.radius + (wall_thickness/2) and self.speed.x > 0):
				self.speed.x = self.speed.x * self.retention * -1
				if abs(self.speed.x) < bounce_limit:
					self.speed.x = 0
		else:
			self.speed.x, self.speed.y = mouse_vel


	def update(self, mouse_pos):
		self.update_gravity()
		if not self.selected:
			self.pos += self.speed
		else:
			self.pos.x, self.pos.y = mouse_pos
		self.circle = pygame.draw.circle(display, self.colour, self.pos, self.radius)

def draw_walls():
	colour = 'white'
	left = pygame.draw.line(display, colour, (-2,-2), (-2,WINDOWHEIGHT), wall_thickness)
	right = pygame.draw.line(display, colour, (WINDOWWIDTH,0), (WINDOWWIDTH,WINDOWHEIGHT), wall_thickness)
	bottom = pygame.draw.line(display, colour, (0,WINDOWHEIGHT), (WINDOWWIDTH,WINDOWHEIGHT), wall_thickness)

def get_mouse_vel():
	vel_x, vel_y = 0, 0
	vel_x = (mouse_tracker[-1][0] - mouse_tracker[0][0]) / len(mouse_tracker)
	vel_y = (mouse_tracker[-1][1] - mouse_tracker[0][1]) / len(mouse_tracker)
	return vel_x, vel_y


# general setup
WINDOWWIDTH, WINDOWHEIGHT = 800, 600
display = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Pygame Ball Physics')
clock = pygame.time.Clock()

# entity setup
wall_thickness = 6
gravity = 0.4
bounce_limit = 1
active_select = False
mouse_tracker = []
mouse_vel = pygame.Vector2()
ball1 = Ball(100, 100, 30, 'blue', 100, 0.7)
ball2 = Ball(300, 100, 35, 'red', 150, 0.8)
ball3 = Ball(700, 100, 20, 'orange', 75, 0.75)
ball4 = Ball(500, 100, 15, 'lime', 50, 0.9)
ball_lst = [ball1, ball2, ball3, ball4]

# asyncio function for website compatibility
async def main():
	running = True

	# main event loop
	while running:
		mouse_pos = pygame.mouse.get_pos()
		mouse_tracker.append(mouse_pos)
		if len(mouse_tracker) > 5:
			mouse_tracker.pop(0)
		mouse_vel.x, mouse_vel.y = get_mouse_vel()
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for ball in ball_lst:
					if ball.check_select(event.pos, mouse_vel):
						active_select = True
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				active_select = False
				for ball in ball_lst:
					ball.check_select((-1,-1))
	
		display.fill('black')
	
		# draw
		walls = draw_walls()
		for ball in ball_lst:
			ball.update(mouse_pos)
	
		# update
		pygame.display.flip()
		clock.tick(60)

		await asyncio.sleep(0)
	
	pygame.quit()
asyncio.run(main())