import pygame
from pygame.locals import *
from sys import exit
from random import randint

# CONSTS
max_size = 400
Black = (0, 0, 0)

# SUB
'''
function: Generate a room
input: None
return: room(Rect)
'''
def GenRoom():
	# left_top 
	x1 = randint(0, 395)
	y1 = randint(0, 395)
	w = randint(1, 50)
	h = randint(1, 50)
	# right_bottom
	x2 = x1+w if(x1+w<400) else 400
	y2 = y1+h if(y1+h<400) else 400

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
			if isIntersected(roomList[i], r):
				appendFlag = False
				break
		if appendFlag:
			validRoomList.append(roomList[i])

	return validRoomList


'''
function: If two rooms are intersected
input: room1, room2 (rooms are Rect)
return: bool (True for intesected)
'''
def isIntersected(roomA, roomB):
	if roomA.right < roomB.left or roomB.right < roomA.left:
		return False
	if roomA.top > roomB.bottom or roomB.top > roomA.bottom:
		return False
	else:
		return True



# MAIN
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((400, 400), 0, 32)
	pygame.display.set_caption('GenMaze 1')

	#surface = pygame.Surface((400, 400)) # same size as screen
	screen.fill((0, 0, 0)) # black

	drawnFlag = True

	# Game Loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()

		if drawnFlag:
			roomList = []
			for i in range(30):
				roomList.append(GenRoom())
			#print(roomList)
			validRoomList = ValidateRooms(roomList)
			#print(validRoomList)
			for r in validRoomList:
				# random color
				color = (randint(0, 255), randint(0, 255), randint(0, 255))
				pygame.draw.rect(screen, color, r, 0)
			drawnFlag = False

		pygame.display.update()


