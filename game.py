from config import Config
from snake import Snake
from apple import Apple
import pygame


class Game():
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode(
        (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    self.clock = pygame.time.Clock()
    self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')
    self.apple = Apple()
    self.snake = Snake()

  def drawGrid(self):
    # draw vertical lines
    for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY,
                       (x, 0), (x, Config.WINDOW_HEIGHT))
    # draw horizontal lines
    for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY,
                       (0, y), (Config.WINDOW_WIDTH, y))

  def drawWorm(self):
    for coord in self.snake.wormCoords:
      x = coord['x'] * Config.CELLSIZE
      y = coord['y'] * Config.CELLSIZE
      wormSegmentReact = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
      pygame.draw.rect(self.screen, Config.DARKGREEN, wormSegmentReact)
      wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8)
      pygame.draw.rect(self.screen, Config.GREEN, wormInnerSegmentRect)

  def drawApple(self):
    x = self.apple.x * Config.CELLSIZE
    y = self.apple.y * Config.CELLSIZE
    appleRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
    pygame.draw.rect(self.screen, Config.DARKRED, appleRect)
    appleInnerRect = pygame.Rect(x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8)
    pygame.draw.rect(self.screen, Config.RED, appleInnerRect)

  def draw(self):
    self.screen.fill(Config.BG_COLOR)
    # in here well draw snake, grid, apple, scroe
    self.drawGrid()
    self.drawWorm()
    self.drawApple()
    pygame.display.update()
    self.clock.tick(Config.FPS)

  def handleKeyEvents(self, event):
    if(event.key == pygame.K_LEFT or event.key == pygame.K_a) and (self.snake.direction != self.snake.RIGHT):
      self.snake.direction = self.snake.LEFT
    elif(event.key == pygame.K_RIGHT or event.key == pygame.K_d) and (self.snake.direction != self.snake.LEFT):
      self.snake.direction = self.snake.RIGHT
    elif(event.key == pygame.K_UP or event.key == pygame.K_w) and (self.snake.direction != self.snake.DOWN):
      self.snake.direction = self.snake.UP
    elif(event.key == pygame.K_DOWN or event.key == pygame.K_s) and (self.snake.direction != self.snake.UP):
      self.snake.direction = self.snake.DOWN
    elif event.key == pygame.K_ESCAPE:
      pygame.quit()

  def resetGame(self):
    del self.snake
    del self.apple
    self.snake = Snake()
    self.apple = Apple()

    return True

  def isGameOver(self):
    if(self.snake.wormCoords[self.snake.HEAD]['x'] == -1 or
            self.snake.wormCoords[self.snake.HEAD]['x'] == Config.CELLWIDTH or
            self.snake.wormCoords[self.snake.HEAD]['y'] == -1 or
            self.snake.wormCoords[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
      return self.resetGame()
    for wormBody in self.snake.wormCoords[1:]:
      if wormBody['x'] == self.snake.wormCoords[self.snake.HEAD]['x'] and wormBody['y'] == self.snake.wormCoords[self.snake.HEAD]['y']:
        return self.resetGame()

  def run(self):
    while True:  # main game loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          self.handleKeyEvents(event)

      self.snake.update(self.apple)
      self.draw()
      if self.isGameOver():
        break
