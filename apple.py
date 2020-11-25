import random
from config import Config


class Apple():
  def __init__(self):
    self.setNewLocation()
  # 사과 생성 메소드
  def setNewLocation(self):
    self.x = random.randint(0, Config.CELLWIDTH - 1) # 0부터 31사이에 난수생성 및 x에 저장
    self.y = random.randint(0, Config.CELLHEIGHT - 1) # 0부터 23사이에 난수생성 및 y에 저장
    
    #사과의 생성의 뱀과 겹칠시 사과 위치를 재설정하여 사과 생성
    #for i in range(len(snake.wormCoords)):
      #if(self.x == snake.wormCoords[i]['x'] and self.y == snake.wormCoords[i]['y']):
        #self.setNewLocation(snake)
