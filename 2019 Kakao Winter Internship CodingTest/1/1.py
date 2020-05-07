
def solution(board, moves):
  q = [[] for _ in range(len(board))]
  bucket = [0]
  popped_count = 0

  for i in board:
    for j in range(len(i)):
      if i[j] != 0:
        q[j].append(i[j])
  print(q)

  for i in moves:
    if len(q[i-1]) > 0:
      target = q[i-1].pop(0)
      if bucket[-1] == target:
        bucket.pop()
        popped_count += 2
      else:
        bucket.append(target)
  print(q)
  print(popped_count)
  return popped_count

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
