#!/usr/bin/python
# Change 'python' above to python2 or python3 to detect which version you use.

N = 15

# The main routine of AI.
def Think(field):
  # // is not defined in python2
  CENTER = (int(N / 2), int(N / 2))

  best_hand = (0, 0)
  for i in range(N):
    for j in range(N):
      if field[i][j] != '.':
        continue

      hand = (i, j)
      if CanGetFiveStones(field, hand):
        return hand
      if GetDistance(best_hand, CENTER) > GetDistance(hand, CENTER):
        best_hand = hand
  return best_hand

# Returns true if you can get five stones from |position|. Returns false otherwise.
def CanGetFiveStones(field, hand):
  # Checks all 8 directions.
  return any(CountStones(field, hand, diffs[0]) + CountStones(field, hand, diffs[1]) + 1 >= 5
             for diffs in [[(-1, -1), (1, 1)], [(-1, 0), (1, 0)],
                           [(-1, 1), (1, -1)], [(0, -1), (0, 1)]])

# Returns the number of stones on the direction |diff| from the next position of |position|.
def CountStones(field, hand, diff):
  count = 1
  while True:
    row, col = (hand[0] + count * diff[0], hand[1] + count * diff[1])
    if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
      return count - 1
    count = count + 1
  # Not reached
  return 0

# Returns the Manhattan distance from |a| to |b|.
def GetDistance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

# =============================================================================
# DO NOT EDIT FOLLOWING FUNCTIONS
# =============================================================================

def main():
  field = Input()
  hand = Think(field)
  Output(hand)

def Input():
  try:
    # python2.7
    field = [raw_input() for i in range(N)]
  except NameError:
    # python3.x does not have raw_input() definition
    field = [input() for i in range(N)]

  return field

def Output(hand):
  print(str(hand[0]) + ' ' + str(hand[1]))

if __name__  == '__main__':
  main()
