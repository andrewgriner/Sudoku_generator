import pygame #Importing the files and programs we need
import numpy as np
from sudoku_generator import SudokuGenerator, generate_sudoku
from Cell import Cell
#GUI INFORMATION that helps with the visual effects of the board
BG_COLOR = (240, 255, 255)
WIDTH = 630
HEIGHT = 720
LINE_WIDTH = 2
BOARD_ROWS = 9
BOARD_COLS = 9
SQUARE_SIZE = 70
LINE_COLOR = (0, 181, 181)


pygame.init() #initializes pygame
pygame.display.set_caption("Sudoku")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)



def game_screen(): #GUI function that prints the visuals
  # draw horizontal lines
  for i in range(0, BOARD_ROWS + 1):
    pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE),
                     (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

  # draw vertical lines
  for i in range(0, BOARD_COLS + 1):
    pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0),
                     (i * SQUARE_SIZE, HEIGHT - 90), LINE_WIDTH)

  # draw some lines thicker
  for i in range(0, 4):
    pygame.draw.line(screen, LINE_COLOR, (0, i * 3 * SQUARE_SIZE),
                     (WIDTH, i * 3 * SQUARE_SIZE), 10)
  for i in range(0, 4):
    pygame.draw.line(screen, LINE_COLOR, (i * 3 * SQUARE_SIZE, 0),
                     (i * 3 * SQUARE_SIZE, HEIGHT), 10)
  # draws the buttons on bottom of screen
  font = pygame.font.Font(None, 40)
  reset_surf = font.render('RESET', 0, LINE_COLOR)
  restart_surf = font.render('RESTART', 0, LINE_COLOR)
  exit_surf = font.render('EXIT', 0, LINE_COLOR)
  reset_rect = reset_surf.get_rect(center=(105, 675))
  restart_rect = restart_surf.get_rect(center=(315, 675))
  exit_rect = exit_surf.get_rect(center=(525, 675))
  screen.blit(reset_surf, reset_rect)
  screen.blit(restart_surf, restart_rect)
  screen.blit(exit_surf, exit_rect)


def start_screen(): #this initializes the start screen
  # creates surfaces for various texts
  font = pygame.font.Font(None, 70)
  welcome_surf = font.render("Welcome to Sudoku!", 0, LINE_COLOR)
  font = pygame.font.Font(None, 50)
  select_surf = font.render("Select Game Mode:", 0, LINE_COLOR)
  font = pygame.font.Font(None, 40)
  easy_surf = font.render('EASY', 0, LINE_COLOR)
  medium_surf = font.render('MEDIUM', 0, LINE_COLOR)
  hard_surf = font.render('HARD', 0, LINE_COLOR)
  font = pygame.font.Font(None, 150)
  face_surf = font.render('^_^', 0, (0, 0, 0))
  # creates rects for various texts
  welcome_rect = welcome_surf.get_rect(center=(315, 200))
  select_rect = select_surf.get_rect(center=(315, 450))
  easy_rect = easy_surf.get_rect(center=(160, 550))
  medium_rect = medium_surf.get_rect(center=(315, 550))
  hard_rect = hard_surf.get_rect(center=(470, 550))
  face_rect = face_surf.get_rect(center=(315, 320))
  # blits the various texts onto the starting screen
  screen.blit(welcome_surf, welcome_rect)
  screen.blit(select_surf, select_rect)
  screen.blit(easy_surf, easy_rect)
  screen.blit(medium_surf, medium_rect)
  screen.blit(hard_surf, hard_rect)
  screen.blit(face_surf, face_rect)
  # horizontal lines
  pygame.draw.line(screen, (0, 0, 0), (100, 580), (540, 580), 5)
  pygame.draw.line(screen, (0, 0, 0), (100, 520), (540, 520), 5)
  pygame.draw.line(screen, (0, 0, 0), (70, 230), (560, 230), 8)
  # vertical lines
  pygame.draw.line(screen, (0, 0, 0), (100, 580), (100, 520), 5)
  pygame.draw.line(screen, (0, 0, 0), (540, 520), (540, 580), 5)
  pygame.draw.line(screen, (0, 0, 0), (230, 580), (230, 520), 5)
  pygame.draw.line(screen, (0, 0, 0), (400, 520), (400, 580), 5)


def game_won_screen(): #This is the function for the game one screen
  # prepares and blits a couple texts for the game won screen
  screen.fill(BG_COLOR)
  font = pygame.font.Font(None, 70)
  won_surf = font.render('Game Won!', 0, LINE_COLOR) #Game won screen
  won_rect = won_surf.get_rect(center=(315, 200))
  screen.blit(won_surf, won_rect)
  font = pygame.font.Font(None, 40)
  exit_surf = font.render('EXIT', 0, LINE_COLOR) #exit button to allow user to leave the game
  exit_rect = exit_surf.get_rect(center=(315, 450))
  screen.blit(exit_surf, exit_rect)
  # draw lines around exit button
  pygame.draw.line(screen, LINE_COLOR, (255, 475), (375, 475), 5)
  pygame.draw.line(screen, LINE_COLOR, (255, 420), (375, 420), 5)
  pygame.draw.line(screen, LINE_COLOR, (255, 475), (255, 420), 5)
  pygame.draw.line(screen, LINE_COLOR, (375, 475), (375, 420), 5)
  pygame.draw.line(screen, (0, 0, 0), (160, 230), (470, 230), 8)


def game_over_screen(): #Function for the game over screen
  # prepares and blits a couple texts for the game over screen
  screen.fill(BG_COLOR)
  font = pygame.font.Font(None, 70)
  lost_surf = font.render('Game Over :(', 0, LINE_COLOR)
  lost_rect = lost_surf.get_rect(center=(315, 200))
  screen.blit(lost_surf, lost_rect)
  font = pygame.font.Font(None, 40)
  restart_surf = font.render('RESTART', 0, LINE_COLOR)
  restart_rect = restart_surf.get_rect(center=(315, 450))
  screen.blit(restart_surf, restart_rect)
  # draw lines around restart button
  pygame.draw.line(screen, LINE_COLOR, (240, 475), (390, 475), 5)
  pygame.draw.line(screen, LINE_COLOR, (240, 420), (390, 420), 5)
  pygame.draw.line(screen, LINE_COLOR, (240, 475), (240, 420), 5)
  pygame.draw.line(screen, LINE_COLOR, (390, 475), (390, 420), 5)
  pygame.draw.line(screen, (0, 0, 0), (160, 230), (430, 230), 8)

#Below are just loop variables and other global variables that are defined
start_screen()
game_over = False
not_started = True
selection=0
cell_list = []
win=False
filled=False
submit=False

def is_actually_valid(nums): #set up so you can only input 1-9
  for i in range(9):
    if i+1 not in list(nums) or list(nums).count(i+1) != 1:
      return False
  return True

while True: #THIS IS THE MAIN EVENT HANDLER THAT CONTROL THE GAME
  # event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() #This is for the exit function
      exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = event.pos
      if win and game_over:  # win condition
        """This ensures when the user wins and tries to click exit they actually quit pygame"""
        if 245<x<385 and 400<y<500:
          pygame.quit()
          exit()
      elif not win and game_over:  # lose condition
        if 245 < x < 385 and 400 < y < 500:
          """Allows the user to select restart when the user loses and the lose screen shows"""
          not_started = True
          game_over = False
          win = False
          for i in range(len(cell_list)):
            cell_list[i].generated = True
          screen.fill(BG_COLOR)
          start_screen()

      if not_started:

        # DIFFICULTY SELECTION
        if 90 < x < 230 and 500 < y < 600:
          removed_cells = 30 #EASY difficulty
          not_started = False
        elif 245 < x < 385 and 500 < y < 600:
          removed_cells = 40 #MEDIUM difficulty
          not_started = False
        elif 400 < x < 540 and 500 < y < 600:
          removed_cells = 50 #HARD difficulty
          not_started = False

        if not not_started: #this is to start a new puzzle and update the display with the new board
          screen.fill(BG_COLOR)
          game_screen()
          board = generate_sudoku(9, removed_cells)
          pygame.display.update()

          for i in range(9): #Creates cell value in a 3 dimentional board
            for j in range(9):
              cell_list.append(Cell(board[i][j],i,j,screen))
              cell_list[-1].draw()
              if cell_list[-1].value == 0:
                cell_list[-1].generated = False

#The block of code below if initialed checks if the mouse was clicked in the regions of the cell list and there cordinates
#and it selts value and sketched value attribures to 0 for any cell that has not been previouslt generated
      if not not_started:
        if event.type == pygame.MOUSEBUTTONDOWN:
          if 0 < x < 210 and 635 < y < 720:
            for i in range(len(cell_list)):
              if not cell_list[i].generated:
                cell_list[i].value = 0
                cell_list[i].sketched_value = 0
                cell_list[i].draw()



          elif 210 < x < 420 and 635 < y < 720:
            not_started=True
            for i in range(len(cell_list)): #this is for the restart button which will allow users to go back
              cell_list[i].generated=True
            screen.fill(BG_COLOR)
            start_screen()


          elif 420 < x < 630 and 635 < y < 720:
            pygame.quit() #This is for the exit button and allows hte user to end the game
            exit()


          for i in range(len(cell_list)):
            cell=cell_list[i]
            true_x = cell.xpos+int(cell.width/2)
            true_y = cell.ypos+int(cell.height/2)
            """The code below takes a cell from cell list based on the
            cordinates of the cell, and the cell selction is updated by changing
            selected attribute to false for old cell True for current ce,ll"""
            if x<=(true_x+int(cell.width/2)) and x>=(true_x-int(cell.width/2)):
              if y<=(true_y+int(cell.height/2)) and y>=(true_y-int(cell.height/2)):
                #print(cell.value)
                if cell.generated==False:
#                 cell_list[selection].sketched_value = cell_list[selection].value
                  cell_list[selection].selected = False
                  cell_list[selection].draw()

                  cell_list[i].selected = True
                  cell_list[i].draw()

                  selection = i

    if not not_started and event.type == pygame.KEYDOWN and not game_over:
      shift=0
      num="whats up"

      if event.key == pygame.K_LEFT: #PYGAME COMMANDS TO ALLOW THE ARROW KEYS TO MOVE ON THE BOARD
        shift-=1
      elif event.key == pygame.K_RIGHT: #Allow arrow keys to be moved
        shift+=1
      elif event.key == pygame.K_UP: #allows arrow keys to be moved
        shift-=9
      elif event.key == pygame.K_DOWN:#allows arrow keys to be moved
        shift+=9
      if shift!=0:
        if selection+shift>=len(cell_list) or selection+shift<0:
          shift=0 #If not = 0 then shift operation, this sets shift to 0

#        cell_list[selection].sketched_value = cell_list[selection].value
        cell_list[selection].selected = False #Selection indec makes it as false for the previously selected cell
        cell_list[selection].draw()

        cell_list[selection+shift].selected = True #true for the new selected cell
        cell_list[selection+shift].draw()

        selection+=shift #changes the value of the shift varaible
      else:
        num=chr(event.key)
#if statement for the sketched cell
      if num.isnumeric() and num != '0':
        if cell_list[selection].value == 0: #looking in the list for the bounds of the cell
          cell_list[selection].sketched_value = int(num) #if there is something in the cell, the code updates the cell selected
          cell_list[selection].draw()
      if event.key==13:
        cell_list[selection].value = cell_list[selection].sketched_value
        cell_list[selection].draw()

  if not not_started and not game_over:
    filled=True
    for i in cell_list:
      if i.value == 0 or i.value!=i.sketched_value:
        filled=False
    """This checks if the  game has been completed
    and if the solution is correct it first checks the fgrids with filled and if
    all the cells have been filled it runs is_actually valid function depending
    on the results it will show one of two end screens"""
    if filled and not game_over:
      win = True
      rows = np.array([x.value for x in cell_list]).reshape(9,9)
      cols=[rows[:, x] for x in range(9)]
      boxes=[rows[:,[0,1,2]][:3],rows[:,[0,1,2]][3:6],rows[:,[0,1,2]][6:9],
             rows[:,[3,4,5]][:3],rows[:,[3,4,5]][3:6],rows[:,[3,4,5]][6:9],
             rows[:,[6,7,8]][:3],rows[:,[6,7,8]][3:6],rows[:,[6,7,8]][6:9]]

      boxes=[i.flatten() for i in boxes]

      for i in rows:
        if not is_actually_valid(i): win=False
      for i in cols:
        if not is_actually_valid(i): win=False
      for i in boxes:
        if not is_actually_valid(i): win=False

      if win:
        game_won_screen() #displays the win screen
      else:
        game_over_screen() #the losing screen
      game_over=True

  pygame.display.update()
