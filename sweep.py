def validate( block_data ):
  bombs = 0
  for i in range(0,3):
    for t in range(0,3):
      if block_data[i][t] == -1:
        bombs = bombs + 1
  if block_data[1][1] == -1:
    return "Bomb"
  if block_data[1][1] == bombs:
    return "Valid"
  else:
    return "Invalid"
  

grid = [
  [-1,1,0],
  [1,1,0],
  [0,0,0]
]

print (validate(grid))