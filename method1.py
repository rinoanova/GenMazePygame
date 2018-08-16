import pygame
from pygame.locals import *
from sys import exit
from random import randint, randrange
import math

# CONSTS
max_size = 400
path_size = 11
space_size = 15
Black = (0, 0, 0)

# SUB
'''
function: Generate a room
input: None
return: room(Rect)
'''
def GenRoom():
	# left_top 
	x1 = randrange(1, 395, 2)
	y1 = randrange(1, 395, 2)
	w = randrange(1, 51, 2)
	h = randrange(1, 51, 2)
	# right_bottom
	x2 = x1+w if(x1+w<401) else 401
	y2 = y1+h if(y1+h<401) else 401

	return Rect((x1, y1), (x2, y2))


'''
function: Make rooms valid 
input: roomList(list)
return: validRoomList(list)
'''
def ValidateRooms(roomList):
	validRoomList = []
	validRoomList.append(roomList[0])
	for i in range(1, len(roomList)):
		appendFlag = True
		for r in validRoomList:
			if pygame.Rect.colliderect(roomList[i], r):
				appendFlag = False
				break
		if appendFlag:
			validRoomList.append(roomList[i])

	return validRoomList


'''
function: Generate paths
input: start(tuple), screen(pygame.Surface)
return: None
'''
def GenPaths(start, surface):
	# random color
	color = (randint(200, 250), randint(200, 250), randint(0, 60))
	# init
	path = [start]
	# stack is not empty
	while len(path)>0:
		print(path)
		# Draw this block
		thisPoint = path[-1] # path.top(), topleft of block
		block = Rect((thisPoint[0], thisPoint[1]), (path_size, path_size))
		#print(block.center)
		pygame.draw.rect(surface, color, block, 0)
		# Generate next block
		nextPoint = RandomDirection(thisPoint, surface)
		print(nextPoint)
		if nextPoint == (-1, -1):
			path = path[:-1] # path.pop()
		else:
			path.append(nextPoint)

'''
function: Find a random direction to go on
input: point(tuple), screen(pygame.Surface)
return: nextPoint(tuple) # (-1, -1) for False
'''
def RandomDirection(point, surface):
	#      ② x
	#       ----
	#  ① x | x | x ③
	#       ----
	#      ④ x
	x, y = point
	direction = []
	if isValidateBlock((x-11, y), surface):
		direction.append((x-11, y))
	if isValidateBlock((x, y-11), surface):
		direction.append((x, y-11))
	if isValidateBlock((x+11, y), surface):
		direction.append((x+11, y))
	if isValidateBlock((x, y+11), surface):
		direction.append((x, y+11))

	if len(direction)==0:
		return (-1, -1)
	else:
		return direction[randint(0, 20)%len(direction)]


'''
function: If block is valid
input: point, screen
return: Boolean
'''
def isValidateBlock(point, surface):
	x, y = point
	if x<11 or x>390 or y<11 or y>390:
		return False
	#print(str(x)+','+str(y))
	print('======')
	for i in range(11): 
		for j in range(11):
			color = surface.get_at((x+i-6, y+j-6))
			#print(color)
			if color != (0, 0, 0, 255):
				return False
	return True


# MAIN
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((401, 401), 0, 32)
	pygame.display.set_caption('GenMaze 1')

	surface = screen.subsurface((0, 0), (401, 401)) # same as screen
	screen.fill((0, 0, 0)) # black

	drawnOnce = True

	# Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		if drawnOnce:
			# Draw Rooms
			roomList = []
			for i in range(50):
				roomList.append(GenRoom())
			#print(roomList)
			validRoomList = ValidateRooms(roomList)
			#print(validRoomList)
			for r in validRoomList:
				# random color
				color = (randint(0, 70), randint(1, 254), randint(180, 220))
				pygame.draw.rect(screen, color, r, 0)

			# Draw paths
			# a block of path: 3*3
			#  ---  topleft: x-1, y-1
			# |   |
			#  ---  bottomright: x+1, y+1
			for i in range(10):
				start = (randrange(11, 391, 2), randrange(11, 391, 2))
				while isValidateBlock(start, screen)==False:
					start = (randrange(11, 391, 2), randrange(11, 391, 2))
				GenPaths(start, screen)

			drawnOnce = False

		pygame.display.update()


