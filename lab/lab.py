class whiteKnight:
  def __init__(self, pos, colour, moves):
    self.pos = pos
    self.colour = colour
    self.moves = moves


n1 = whiteKnight(2, True, [17, 19])

class blackKnight:
  def __init__(self, pos, colour, moves):
    self.pos = pos
    self.colour = colour
    self.moves = moves

n2 = blackKnight(17, False, [2, 11, 17,34])

n1col = n1.colour
n2col = n2.colour
def opp (n1col, n2col):
  print (n1col)
  print (n2col)
return