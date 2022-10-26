import pygame, sys
import time

row = 0
col = 0
remove_row = 0
remove_col = 0
list7 = []
Turn = True
condition1 = False
condition2 = False
list8 = []
undo_x = -1
undo_y = -1
undo_row = -1
undo_col = -1
undo1_row = -1
undo1_col = -1

def Pause():
    while True:
        s = pygame.Surface((1000,750), pygame.SRCALPHA)  
        s.fill((255,255,255,1))                         
        SCREEN.blit(s, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(40).render("PAUSED", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(350, 250),text_input="RESUME", font=get_font(40), base_color="#d7fcd4", hovering_color="red")
        PLAY_BUTTON.changeColor(MENU_MOUSE_POS)
        PLAY_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return
        pygame.display.update()

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)

		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class pawns:
    def __init__(self,x,y,label):
        global list8
        self.black = pygame.transform.scale(pygame.image.load("assets/noir.png"),(50,50))
        self.white = pygame.transform.scale(pygame.image.load("assets/blanc.png"),(50,50))
        self.x = x
        self.y = y
        self.label = label
        self.condition = True
        self.row = 0
        self.col = 0
        self.move = False
        self.condition1 = True
        self.set = set()
        
    def update(self):
        global list6,col,row,remove_row,remove_col,condition1,condition2,list8,Turn
        if self.label == 1:
            SCREEN.blit(self.white,(self.x,self.y))
        elif self.label == 2:
            SCREEN.blit(self.black,(self.x,self.y))
            
        keys=pygame.key.get_pressed()
        self.condition1 = True
        if keys[pygame.K_u] and undo_row!=-1 :
            self.condition1= False
            for i in list7:
                if i.row == undo_row and i.col == undo_col:
                    list6[i.col][i.row]=0
                    list6[undo1_row][undo1_col]=i.label
                    i.x = undo_x
                    i.y = undo_y
                    i.col-=1
            condition1 = False
            condition2 = False

        if self.condition:
            list6[row][col] = self.label
            self.row = row
            self.col = col
            self.condition = False
            if row == 2 and col == 1:
               col+=2
            else:
                col+=1
        if col>4:
            col=0 
            row+=1
        try:
            if (list6[self.row-2][self.col] == 0 and  list6[self.row-1][self.col] == 1 and list6[self.row][self.col]==2 and self.row-1>=0 and self.row-2>=0) and Turn or (list6[self.row+2][self.col] == 0 and self.label==2 and list6[self.row+1][self.col] == 1 and list6[self.row][self.col]==2) and Turn or (list6[self.row+2][self.col] == 0 and self.label==2 and list6[self.row+1][self.col] == 1 and list6[self.row][self.col]==2) and Turn or (list6[self.row][self.col-2] == 0 and self.label==2 and list6[self.row][self.col-1] == 1 and list6[self.row][self.col]==2 and self.col-1>=0 and self.col-2>=0) and Turn or (list6[self.row][self.col+2] == 0 and list6[self.row][self.col+1] == 1 and list6[self.row][self.col]==2) and Turn or (list6[self.row+2][self.col+2] == 0 and list6[self.row+1][self.col+1] == 1 and list6[self.row][self.col]==2) and Turn or (list6[self.row-2][self.col-2] == 0 and list6[self.row-1][self.col-1] == 1 and list6[self.row][self.col]==2) and self.col-1>=0 and self.col-2>=0 and self.row-1>=0 and self.row-2>=0 and Turn or (list6[self.row-2][self.col+2] == 0 and list6[self.row-1][self.col+1] == 1 and list6[self.row][self.col]==2) and self.row-1>=0 and self.row-2>=0 and Turn or (list6[self.row+2][self.col-2] == 0 and list6[self.row+1][self.col-1] == 1 and list6[self.row][self.col]==2) and self.col-1>=0 and self.col-2>=0 and Turn:
                remove_col = self.col
                remove_row = self.row
                condition1 = True
                
        except:
            pass
        try:
            if (list6[self.row-2][self.col] == 0 and  list6[self.row-1][self.col] == 2 and list6[self.row][self.col]==1 and self.row-1>=0 and self.row-2>=0) and not Turn or (list6[self.row+2][self.col] == 0  and list6[self.row+1][self.col] == 2 and list6[self.row][self.col]==1) and not Turn or (list6[self.row][self.col-2] == 0 and list6[self.row][self.col-1] == 2 and list6[self.row][self.col]==1 and self.col-1>=0 and self.col-2>=0) and not Turn or (list6[self.row][self.col+2] == 0 and list6[self.row][self.col+1] == 2 and list6[self.row][self.col]==1) and not Turn or (list6[self.row+2][self.col+2] == 0 and list6[self.row+1][self.col+1] == 2 and list6[self.row][self.col]==1) and not Turn or (list6[self.row-2][self.col-2] == 0 and list6[self.row-1][self.col-1] == 2 and list6[self.row][self.col]==1) and self.col-1>=0 and self.col-2>=0 and self.row-1>=0 and self.row-2>=0 and not Turn or (list6[self.row-2][self.col+2] == 0 and list6[self.row-1][self.col+1] == 2 and list6[self.row][self.col]==1) and self.row-1>=0 and self.row-2>=0 and not Turn or (list6[self.row+2][self.col-2] == 0 and list6[self.row+1][self.col-1] == 2 and list6[self.row][self.col]==1) and self.col-1>=0 and self.col-2>=0 and not Turn:
                remove_col = self.col
                remove_row = self.row
                condition2 = True
        except:
            pass
        if condition1 and not Turn:
            for i in list7:
                if remove_row == i.row and remove_col == i.col:
                    i.x=1000
            list6[remove_row][remove_col] = 0
            condition1 = False
        elif condition2 and Turn:
            for i in list7:
                if remove_row == i.row and remove_col == i.col:
                    i.x=1000
            list6[remove_row][remove_col] = 0
            condition2 = False
        
    def movement(self,x,y):
        global Turn,condition1,condition2,remove_row,remove_col,undo_x,undo_col,list8,undo_y,undo_row,undo1_col,undo1_row
        
        if x>self.x and x<self.x+47 and y>self.y and y<self.y+47:
            self.move = True

        elif self.move and x>self.x and x<self.x+197 and y>self.y and y<self.y+47 and list6[self.row][self.col+1] == 0 and (((self.row*5)+self.col+1)not in self.set):
            
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.x+=150
            list6[self.row][self.col] = 0
            list6[self.row][self.col+1] =  self.label
            self.col+=1
            self.move = False
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row
            
        elif self.move and x>self.x-197 and x<self.x and y>self.y and y<self.y+47 and list6[self.row][self.col-1] == 0 and (((self.row*5)+self.col-1)not in self.set):
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.x-=150
            list6[self.row][self.col] = 0
            list6[self.row][self.col-1] =  self.label
            self.col-=1
            self.move = False
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row


        elif self.move and x>self.x and x<self.x+47 and y>self.y and y<self.y+197 and list6[self.row+1][self.col] == 0 and ((((self.row+1)*5)+self.col)not in self.set):
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.y+=150
            list6[self.row][self.col] = 0
            list6[self.row+1][self.col] =  self.label
            self.row+=1
            self.move = False
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row

        elif self.move and x>self.x and x<self.x+47 and y>self.y-197 and y<self.y and list6[self.row-1][self.col] == 0 and ((int(((self.row-1)*5)/2)+self.col)not in self.set):
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.y-=150
            list6[self.row][self.col] = 0
            list6[self.row-1][self.col] =  self.label
            self.row-=1
            self.move = False
          
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row

        elif self.move and x>self.x and x<self.x+197 and y>self.y and y<self.y+197 and list6[self.row+1][self.col+1] == 0 and (self.row!=1 or self.col!=0) and (self.row!=3 or self.col!=0) and (self.row!=0 or self.col!=1) and (self.row!=0 or self.col!=3) and (self.row!=2 or self.col!=3) and (self.row!=2 or self.col!=1) and (self.row!=3 or self.col!=2) and (self.row!=1 or self.col!=2) :
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.y+=150
            self.x+=150
            list6[self.row][self.col] = 0
            list6[self.row+1][self.col+1] =  self.label
            self.row+=1
            self.col+=1
            self.move = False
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row

        elif self.move and x>self.x-197 and x<self.x and y>self.y and y<self.y+197 and list6[self.row+1][self.col-1] == 0 and (self.row!=1 or self.col!=4) and (self.row!=3 or self.col!=4) and (self.row!=0 or self.col!=1) and (self.row!=0 or self.col!=3) and (self.row!=3 or self.col!=4) and (self.row!=1 or self.col!=2) and (self.row!=2 or self.col!=3) and (self.row!=2 or self.col!=1) and (self.row!=3 or self.col!=2) :
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.y+=150
            self.x-=150
            list6[self.row][self.col] = 0
            list6[self.row+1][self.col-1] =  self.label
            self.row+=1
            self.col-=1
            self.move = False
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row

        elif self.move and x>self.x-197 and x<self.x and y>self.y-197 and y<self.y and list6[self.row-1][self.col-1] == 0 and (self.row!=2 or self.col!=1) and (self.row!=1 or self.col!=4) and (self.row!=3 or self.col!=4) and (self.row!=3 or self.col!=2) and (self.row!=4 or self.col!=1) and (self.row!=4 or self.col!=3) and (self.row!=2 or self.col!=3) :
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.y-=150
            self.x-=150
            list6[self.row][self.col] = 0
            list6[self.row-1][self.col-1] =  self.label
            self.row-=1
            self.col-=1
            self.move = False
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row

        elif self.move and x>self.x and x<self.x+197 and y>self.y-197 and y<self.y and list6[self.row-1][self.col+1] == 0 and (self.row!=1 or self.col!=4) and (self.row!=3 or self.col!=4) and (self.row!=0 or self.col!=1) and (self.row!=3 or self.col!=4) and (self.row!=2 or self.col!=1) and (self.row!=1 or self.col!=2) and (self.row!=1 or self.col!=0) and (self.row!=3 or self.col!=2) and (self.row!=3 or self.col!=0) and (self.row!=4 or self.col!=1) and (self.row!=4 or self.col!=3) :
            undo_x = self.x
            undo_y = self.y
            undo1_col = self.col
            undo1_row = self.row
            self.set.add((self.row*5)+self.col)
            self.y-=150
            self.x+=150
            list6[self.row][self.col] = 0
            list6[self.row-1][self.col+1] =  self.label
            self.row-=1
            self.col+=1
            self.move = False
            if Turn :
                Turn = False
            else:
                Turn = True
            remove_col = self.col
            remove_row = self.row
            undo_col = self.col
            undo_row = self.row

        elif self.move and x>self.x and x<self.x+47 and y>self.y-347 and y<self.y and ((list6[self.row-2][self.col] == 0 and self.label==1 and  list6[self.row-1][self.col] == 2) or (list6[self.row-2][self.col] == 0 and self.label==2 and  list6[self.row-1][self.col] == 1)):
            undo_row=-1
            self.y-=300
            list6[self.row][self.col] = 0
            list6[self.row-2][self.col] =  self.label
            self.row-=2
            self.move = False
            
            for i in list7:
                if i.row == self.row+1 and i.col == self.col:
                    i.x=1000
            list6[self.row+1][self.col] = 0
            
            if Turn :
                Turn = False
                condition1 = False
            else:
                Turn = True
                condition2 = False

        elif self.move and x>self.x and x<self.x+47 and y>self.y and y<self.y+347 and ((list6[self.row+2][self.col] == 0 and self.label==1 and  list6[self.row+1][self.col] == 2) or (list6[self.row+2][self.col] == 0 and self.label==2 and  list6[self.row+1][self.col] == 1)):
            undo_row=-1
            self.y+=300
            list6[self.row][self.col] = 0
            list6[self.row+2][self.col] =  self.label
            self.row+=2
            self.move = False
            
            for i in list7:
                if i.row == self.row-1 and i.col == self.col:
                    i.x=1000
            list6[self.row-1][self.col] = 0
            if Turn :
                condition1 = False
                Turn = False
            else:
                Turn = True
                condition2 = False
        
        elif self.move and x>self.x and x<self.x+347 and y>self.y and y<self.y+47 and ((list6[self.row][self.col+2] == 0 and self.label==1 and  list6[self.row][self.col+1] == 2) or (list6[self.row][self.col+2] == 0 and self.label==2 and  list6[self.row][self.col+1] == 1)):
            undo_row=-1
            self.x+=300
            list6[self.row][self.col] = 0
            list6[self.row][self.col+2] =  self.label
            self.col+=2
            self.move = False
            
            for i in list7:
                if i.row == self.row and i.col == self.col-1:
                    i.x=1000
            list6[self.row][self.col-1] = 0
            if Turn :
                Turn = False
                condition1 = False
            else:
                Turn = True
                condition2 = False

        elif self.move and x>self.x-347 and x<self.x and y>self.y and y<self.y+47 and ((list6[self.row][self.col-2] == 0 and self.label==1 and  list6[self.row][self.col-1] == 2) or (list6[self.row][self.col-2] == 0 and self.label==2 and  list6[self.row][self.col-1] == 1)):
            undo_row=-1
            self.x-=300
            list6[self.row][self.col] = 0
            list6[self.row][self.col-2] =  self.label
            self.col-=2
            self.move = False
            
            for i in list7:
                if i.row == self.row and i.col == self.col+1:
                    i.x=1000
            list6[self.row][self.col+1] = 0
            if Turn :
                condition1 = False
                Turn = False
            else:
                Turn = True
                condition2 = False

        elif self.move and x>self.x-347 and x<self.x and y>self.y-347 and y<self.y and (self.row!=2 or self.col!=1) and (self.row!=1 or self.col!=4) and (self.row!=3 or self.col!=4) and (self.row!=3 or self.col!=2) and (self.row!=4 or self.col!=1) and (self.row!=4 or self.col!=3) and (self.row!=2 or self.col!=3) and ((list6[self.row-2][self.col-2] == 0 and self.label==1 and  list6[self.row-1][self.col-1] == 2) or (list6[self.row-2][self.col-2] == 0 and self.label==2 and  list6[self.row-1][self.col-1] == 1)):
            undo_row=-1
            self.y-=300
            self.x-=300
            list6[self.row][self.col] = 0
            list6[self.row-2][self.col-2] =  self.label
            self.row-=2
            self.col-=2
            self.move = False
            for i in list7:
                if i.row == self.row+1 and i.col == self.col+1:
                    i.x=1000
            list6[self.row+1][self.col+1] = 0
            if Turn :
                Turn = False
                condition1 = False
            else:
                Turn = True
                condition2 = False

        elif self.move and x>self.x and x<self.x+347 and y>self.y and y<self.y+347 and (self.row!=1 or self.col!=0) and (self.row!=3 or self.col!=0) and (self.row!=0 or self.col!=1) and (self.row!=0 or self.col!=3) and (self.row!=2 or self.col!=3) and (self.row!=2 or self.col!=1) and (self.row!=3 or self.col!=2) and (self.row!=1 or self.col!=2) and ((list6[self.row+2][self.col+2] == 0 and self.label==2 and  list6[self.row+1][self.col+1] == 1) or  (list6[self.row+2][self.col+2] == 0 and self.label==1 and  list6[self.row+1][self.col+1] == 2)):
            undo_row=-1
            self.y+=300
            self.x+=300
            list6[self.row][self.col] = 0
            list6[self.row+2][self.col+2] =  self.label
            self.row+=2
            self.col+=2
            self.move = False
            for i in list7:
                if i.row == self.row-1 and i.col == self.col-1:
                    i.x=1000
            list6[self.row-1][self.col-1] = 0
            if Turn :
                condition1 = False
                Turn = False
            else:
                Turn = True
                condition2 = False

        elif self.move and x>self.x-347 and x<self.x and y>self.y and y<self.y+347 and (self.row!=1 or self.col!=4) and (self.row!=3 or self.col!=4) and (self.row!=0 or self.col!=1) and (self.row!=0 or self.col!=3) and (self.row!=3 or self.col!=4) and (self.row!=1 or self.col!=2) and (self.row!=2 or self.col!=3) and (self.row!=2 or self.col!=1) and (self.row!=3 or self.col!=2)  and ((list6[self.row+2][self.col-2] == 0 and self.label==2 and list6[self.row+1][self.col-1] == 1) or  (list6[self.row+2][self.col-2] == 0 and self.label==1 and  list6[self.row+1][self.col-1] == 2)):
            undo_row=-1
            self.y+=300
            self.x-=300
            list6[self.row][self.col] = 0
            list6[self.row+2][self.col-2] =  self.label
            self.row+=2
            self.col-=2
            self.move = False
            for i in list7:
                if i.row == self.row-1 and i.col == self.col+1:
                    i.x=1000
            list6[self.row-1][self.col+1] = 0
            if Turn :
                condition1 = False
                Turn = False
            else:
                Turn = True
                condition2 = False
        
        elif self.move and x>self.x and x<self.x+347 and y>self.y-347 and y<self.y  and (self.row!=1 or self.col!=4) and (self.row!=3 or self.col!=4) and (self.row!=0 or self.col!=1) and (self.row!=3 or self.col!=4) and (self.row!=2 or self.col!=1) and (self.row!=1 or self.col!=2) and (self.row!=1 or self.col!=0) and (self.row!=3 or self.col!=2) and (self.row!=3 or self.col!=0) and (self.row!=4 or self.col!=1) and (self.row!=4 or self.col!=3) and ((list6[self.row-2][self.col+2] == 0 and self.label==2 and list6[self.row-1][self.col+1] == 1) or  (list6[self.row-2][self.col+2] == 0 and self.label==1 and  list6[self.row-1][self.col+1] == 2)):
            undo_row=-1
            self.y-=300
            self.x+=300
            list6[self.row][self.col] = 0
            list6[self.row-2][self.col+2] =  self.label
            self.row-=2
            self.col+=2
            self.move = False
            for i in list7:
                if i.row == self.row+1 and i.col == self.col-1:
                    i.x=1000
            list6[self.row+1][self.col-1] = 0
            if Turn :
                condition1 = False
                Turn = False
            else:
                Turn = True
                condition2 = False
        else:
            self.move = False
        
        if 1 not in list6[0] and 1 not in list6[1] and 1 not in list6[2] and 1 not in list6[3] and 1 not in list6[4]:
            victory('Black')

        if 2 not in list6[0] and 2 not in list6[1] and 2 not in list6[2] and 2 not in list6[3] and 2 not in list6[4]:
            victory('white')

            
WIDTH,HEIGHT = 720,650
C_BG = pygame.image.load("assets/Tableau.png")
C_BG = pygame.transform.scale(C_BG,(600,600))
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ALQUERQUE")
OP = '1 VS 1'
list6 = []
list1 = [0,0,0,0,0]
list2 = [0,0,0,0,0]
list3 = [0,0,0,0,0]
list4 = [0,0,0,0,0]
list5 = [0,0,0,0,0]
list6.extend((list1,list2,list3,list4,list5))


def victory(color):
    SCREEN.fill("white")
    pygame.draw.rect(SCREEN,'white',(10,10,700,110))
    if color !="draw":
        OP_TEXT = get_font(30).render(color+' has won the game!', True, 'black')
    else:
        OP_TEXT = get_font(30).render('Draw!', True, 'black')
    OP_RECT = OP_TEXT.get_rect(center=(370,250))
    SCREEN.blit(OP_TEXT,OP_RECT)
    pygame.display.update()
    time.sleep(5)
    main_menu()

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    global list6,list7,list8
    a_b = pawns(27,0,2)
    b_b = pawns(177,0,2)
    c_b = pawns(327,0,2)
    d_b = pawns(477,0,2)
    e_b = pawns(627,0,2)
    f_b = pawns(27,150,2)
    g_b = pawns(177,150,2)
    h_b = pawns(327,150,2)
    i_b = pawns(477,150,2)
    j_b = pawns(627,150,2)
    k_b = pawns(27,300,2)
    l_b = pawns(177,300,2)
    a_w = pawns(477,300,1)
    b_w = pawns(627,300,1)
    c_w = pawns(27,450,1)
    d_w = pawns(177,450,1)
    e_w = pawns(327,450,1)
    f_w = pawns(477,450,1)
    g_w = pawns(627,450,1)
    h_w = pawns(27,600,1)
    i_w = pawns(177,600,1)
    j_w = pawns(327,600,1)
    k_w = pawns(477,600,1)
    l_w = pawns(627,600,1)
    list7.extend((a_b,b_b,c_b,d_b,e_b,f_b,g_b,h_b,i_b,j_b,k_b,l_b,a_w,b_w,c_w,d_w,e_w,f_w,g_w,h_w,i_w,j_w,k_w,l_w))
    while True:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            Pause()
        x,y = pygame.mouse.get_pos()
        SCREEN.fill('white')
        SCREEN.blit(C_BG,(50,25))
        a_b.update(),b_b.update(),c_b.update(),d_b.update(),e_b.update(),f_b.update(),g_b.update(),h_b.update(),i_b.update(),j_b.update(),k_b.update(),l_b.update(),a_w.update(),b_w.update(),c_w.update(),d_w.update(),e_w.update(),f_w.update(),g_w.update(),h_w.update(),i_w.update(),j_w.update(),k_w.update(),l_w.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if Turn:
                    a_w.movement(x,y),b_w.movement(x,y),c_w.movement(x,y),d_w.movement(x,y),e_w.movement(x,y),f_w.movement(x,y),g_w.movement(x,y),h_w.movement(x,y),i_w.movement(x,y),j_w.movement(x,y),k_w.movement(x,y),l_w.movement(x,y)
                if not Turn:
                    a_b.movement(x,y),b_b.movement(x,y),c_b.movement(x,y),d_b.movement(x,y),e_b.movement(x,y),f_b.movement(x,y),g_b.movement(x,y),h_b.movement(x,y),i_b.movement(x,y),j_b.movement(x,y),k_b.movement(x,y),l_b.movement(x,y)                  
        pygame.display.update()

def main_menu():
    global OP,list1,list2,list3,list4,list5,list6,condition1,condition2,color,row,col,remove_col,remove_row,undo_col,undo_row,list7,Turn,list8,undo_x,undo_y,undo1_col,undo1_row

    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(40).render("ALQUERQUE", True, "red")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 100))
        OP_TEXT = get_font(35).render("Mode", True, "red")
        OP_RECT = OP_TEXT.get_rect(center=(350, 400))
        NAME_OP_TEXT = get_font(40).render(OP, True, "yellow")
        NAME_OP_RECT = NAME_OP_TEXT.get_rect(center=(350, 500))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Rect.png"), pos=(350, 250),text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="red")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(OP_TEXT,OP_RECT)
        SCREEN.blit(NAME_OP_TEXT,NAME_OP_RECT)

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
        pygame.display.update()
main_menu()
