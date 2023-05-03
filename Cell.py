
import pygame
import math
#Importing needed modules
class Cell:

  def __init__(self, value, row, col, screen):  #Seting attributes
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen
    self.selected = False
    self.font = pygame.font.SysFont('Arial', 40)
    self.width = 70
    self.height = 70

    self.generated = True #Setting generated value to true
    self.sketched_value = value

    self.line_width=2 #Width assigned
    self.xoff=0
    self.yoff=0

    self.xpos = self.col * self.width + self.xoff + self.line_width*math.floor((self.col)/3)
    self.ypos = self.row * self.height + self.yoff +self.line_width*math.floor((self.row)/3)
  def set_cell_value(self, value):  #Sets the value of the cell
    self.value = value

  def set_sketched_value(self, value):  #Set a sketched value for the cell
    self.sketched_value = value

  def draw(self):  #Draw cell witha while rectangle to show th sell then a red outlin if selected
    pygame.draw.rect(self.screen, (240, 255, 255),
                     (self.xpos, self.ypos, self.width, self.height))
    if self.selected:
      pygame.draw.rect(self.screen, (255, 0, 0),
                       (self.xpos, self.ypos, self.width, self.height), 2)
    else:
      pygame.draw.rect(self.screen, (0, 181, 181),
                       (self.xpos, self.ypos, self.width, self.height), 2)

    if self.value != self.sketched_value: #this is for sketched cell rendering

      text = self.font.render(str(self.sketched_value), True, (125, 125, 125))
      text_rect = text.get_rect(center=(self.xpos + self.width / 2,
                                        self.ypos + self.height / 2))
      self.screen.blit(text, text_rect)
    elif self.value == self.sketched_value and self.value!=0: #Redenders and displays the cells value

      text = self.font.render(str(self.value), True, (0, 0, 0))
      text_rect = text.get_rect(center=(self.xpos + self.width / 2,
                                        self.ypos + self.height / 2))
      self.screen.blit(text, text_rect)