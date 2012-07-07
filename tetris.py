import pygame, sys
from pygame.locals import *
import pdb
import random

class Tetris():

	def __init__(self):
		self.board = [[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']],
				[['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','',''],['obstacle','','']]]

	def draw_board(self):
		BLACK = (0,0,0)
		WHITE = (255,255,255)	
		RED = (255,0,0)
		GREEN = (0,255,0)
		BLUE = (0,0, 255)
		PURPLE = (150,0,150)
		TURQUOISE = (0,150,150)
		YELLOW = (255,255,0)
		GREY = (125,125,125)
		DISPLAYSURF = pygame.display.set_mode((200,400),0,32)
		for i in range(3,23): #there are 24 rows total, 3 at the top and 1 at the bottom are NOT displayed
			for j in range(1,11): #there are 12 columns total, 1 on each side is NOT displayed
				y, x = i*20 - 60, j*20 - 20 #this maps to the coordinates being displayed, excluding borders
				piece_type = self.board[i][j][1]
				if piece_type == '':
					pygame.draw.rect(DISPLAYSURF,BLACK,(x,y,20,20))
				elif piece_type == 'line':
					pygame.draw.rect(DISPLAYSURF,GREEN,(x,y,20,20))
				elif piece_type == 'T':
					pygame.draw.rect(DISPLAYSURF,BLUE,(x,y,20,20))
				elif piece_type == 'J':
					pygame.draw.rect(DISPLAYSURF,WHITE,(x,y,20,20))
				elif piece_type == 'L':
					pygame.draw.rect(DISPLAYSURF,RED,(x,y,20,20))
				elif piece_type == 'S':
					pygame.draw.rect(DISPLAYSURF,PURPLE,(x,y,20,20))
				elif piece_type == 'Z':
					pygame.draw.rect(DISPLAYSURF,TURQUOISE,(x,y,20,20))
				elif piece_type == 'box':
					pygame.draw.rect(DISPLAYSURF,YELLOW,(x,y,20,20))
		if self.you_lose():
			#print 'You lose!'
			pygame.font.init()
			myfont = pygame.font.SysFont('sawasdee', 30, bold=1)
			pygame.draw.rect(DISPLAYSURF, GREY, (30,45,140,50))
			label = myfont.render('You lose!', 1, WHITE)
			DISPLAYSURF.blit(label, (40,50))
		pygame.display.update() 		

		

	def piece_fall(self):
		obstacle_hit = False
		for row in range(22,-1,-1):
			for column in range(12):
				#print 'row: %d column: %d' %(row,column)
				if self.board[row][column][0] == 'active':
					if self.board[row+1][column][0] == 'obstacle':
						obstacle_hit = True
						#print 'obstacle found at %d %d' %(row, column)
						
		if not obstacle_hit: #keep falling as long as obstacle not hit
			for row in range(22,-1,-1):
				for column in range(12):
					if self.board[row][column][0] == 'active':
						#print "found piece in piece_fall", row, column
						color, pivot_state = self.board[row][column][1], self.board[row][column][2]
						self.board[row][column] = ['','','']
						self.board[row+1][column] = ['active',color,pivot_state]

		elif obstacle_hit: #if obstacle encountered, active piece becomes obstacle
			for row in range(22,-1,-1):
				for column in range(12):
					if self.board[row][column][0] == 'active':
						self.board[row][column][0] = 'obstacle'

		#for row in range(24): #prints to terminal - used for debugging
		#	print self.board[row]	

						

	def user_input(self, event, piece):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				self.move_right()
			elif event.key == pygame.K_LEFT:
				self.move_left()
			elif event.key == pygame.K_DOWN:
				self.piece_fall()
			elif event.key == pygame.K_UP:
				self.rotate(piece)

	def move_left(self):
		obstacle_hit = False
		for row in range(22,-1,-1): #loop backwards from bottom to top - easier to check for obstacles
			for column in range(1,11):
				state, piece_type, pivot_state = self.board[row][column] #unpack list into elements
				if state == 'active':
					if self.board[row][column-1][0] == 'obstacle': #checks state of cell to left
						obstacle_hit = True
		if not obstacle_hit: #obstacle not encountered
			for row in range(22,-1,-1):
				for column in range(1,11):			
					state, piece_type, pivot_state = self.board[row][column] #unpack list into elements
					if state == 'active':
						self.board[row][column] = ['','','']
						self.board[row][column-1] = [state,piece_type,pivot_state] 
							#assigns cell on left to values of original cell
						
	def move_right(self):
		obstacle_hit = False
		for row in range(22,-1,-1):
			for column in range(11,0,-1): #loop from right to left
				state, piece_type, pivot_state = self.board[row][column] #unpack list into elements
				if state == 'active':
					if self.board[row][column+1][0] == 'obstacle': #check state of cell to right
						obstacle_hit = True
		if not obstacle_hit: #obstacle not encountered
			for row in range(22,-1,-1):
				for column in range(11,0,-1):			
					state, piece_type, pivot_state = self.board[row][column] #unpack list into elements
					if state == 'active':
						self.board[row][column] = ['','',''] #reset cell you're moving away from
						self.board[row][column+1] = [state,piece_type,pivot_state]
	def rotate(self, piece_type):
		if piece_type == 'line':
			pass #come back later and fix this
		elif piece_type == 'box':
			pass #rotating box does nothing
		else: #other five piece types
			pivot_row, pivot_col = self.find_pivot()
			self.rotate_grid(pivot_row, pivot_col)

	def find_pivot(self):
		for row in range(23):
			for column in range(12):
				state, piece_type, pivot_state = self.board[row][column] #unpack list into elements
				if state == 'active' and pivot_state == 'pivot':
					return row, column
	
	def rotate_grid(self, pivot_row, pivot_col):
		top, bottom = pivot_row -1, pivot_row +1
		left, right = pivot_col -1, pivot_col +1
		new = [[0 for i in range(3)] for j in range(3)] #initializes 3x3 grid
		#MAPPING
		new[0][0] = self.board[bottom][left]		
		new[0][1] = self.board[pivot_row][left]		
		new[0][2] = self.board[top][left]
		new[1][0] = self.board[bottom][pivot_col]
		new[1][1] = self.board[pivot_row][pivot_col]	
		new[1][2] = self.board[top][pivot_col]
		new[2][0] = self.board[bottom][right]
		new[2][1] = self.board[pivot_row][right]
		new[2][2] = self.board[top][right]
		for line in new:
			print line
		#Assign to self.board
		obstacle_hit = False
		for new_row in range(3):
			for new_column in range(3):
				if new[new_row][new_column][0] == 'active' and self.board[new_row+top][new_column+left][0] == 'obstacle':
					obstacle_hit = True
		if not obstacle_hit:
			for new_row in range(3):
				for new_column in range(3): #place new onto self.board
					if new[new_row][new_column][0] != 'obstacle':
						self.board[top+new_row][left+new_column] = new[new_row][new_column]


		


		


	def piece_is_active(self):  #returns True if any active cells on the board
		for row in range(23):
			for column in range(12):
				if self.board[row][column][0] == 'active':
					return True
		else: 
			return False

	def generate_piece(self):
		random_seed = random.randint(1,7)
		if random_seed == 1: #build line
			self.board[3][6] = ['active','line','']
			self.board[2][6] = ['active','line','']
			self.board[1][6] = ['active','line','']
			self.board[0][6] = ['active','line','']		
		elif random_seed == 2: #build T
			self.board[3][5] = ['active','T','']
			self.board[3][6] = ['active','T','pivot']
			self.board[3][7] = ['active','T','']
			self.board[2][6] = ['active','T','']
		elif random_seed == 3: #build J
			self.board[3][5] = ['active','J','']
			self.board[3][6] = ['active','J','pivot']
			self.board[3][7] = ['active','J','']
			self.board[2][5] = ['active','J','']
		elif random_seed == 4: #build L
			self.board[3][5] = ['active','L','']
			self.board[3][6] = ['active','L','pivot']
			self.board[3][7] = ['active','L','']
			self.board[2][7] = ['active','L','']
		elif random_seed == 5: #build square
			self.board[3][6] = ['active','box','']
			self.board[3][7] = ['active','box','']
			self.board[2][6] = ['active','box','']
			self.board[2][7] = ['active','box','']
		elif random_seed == 6: #build S
			self.board[3][5] = ['active','S','']
			self.board[3][6] = ['active','S','pivot']
			self.board[2][6] = ['active','S','']
			self.board[2][7] = ['active','S','']
		elif random_seed == 7: #build Z
			self.board[3][6] = ['active','Z','pivot']
			self.board[3][7] = ['active','Z','']
			self.board[2][5] = ['active','Z','']
			self.board[2][6] = ['active','Z','']
		return self.board[3][6][1] #returns piece type

	def line_drop(self):
		newline = [['obstacle','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],['obstacle','','']]
		lines_dropped = 0
		for row in range(23): #must use range(23), not range(24), to avoid knocking out bottom row, which is just an obstacle.
			filled = 0
			for column in range(12):
				if self.board[row][column][0] == 'obstacle':
					filled += 1
			if filled == 12:
				self.board.pop(row)
				self.board.insert(0,newline)
				lines_dropped += 1
		return lines_dropped

	def score(self, lines_dropped):
		if lines_dropped == 1:
			score = 100
		elif lines_dropped == 2:
			score = 300
		elif lines_dropped == 3:
			score = 600
		elif lines_dropped == 4:
			score = 1000	
		return score

	def you_lose(self):
		lose = False
		for column in range(1,11):
			if self.board[3][column][0] == 'obstacle':
				lose = True	
		return lose			
				

#STEPDOWN = USEREVENT + 2 	
#steptime = pygame.event.Event(STEPDOWN)
#pygame.event.post(steptime)	
#pygame.time.set_timer(STEPDOWN, 500)
#clock = pygame.Clock.time()

board = Tetris()

frames = 0

points = 0

while True:
	if not board.piece_is_active() and not board.you_lose():
		piece = board.generate_piece()
	board.draw_board()
	lines_dropped = board.line_drop()
	if lines_dropped > 0:
		points = points + board.score(lines_dropped)
		print points
	frames += 1	
	if frames % 50 == 0:
		board.piece_fall()
		#pdb.set_trace()
	for event in pygame.event.get():
		board.user_input(event, piece)
		#print event.type, event 
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		

