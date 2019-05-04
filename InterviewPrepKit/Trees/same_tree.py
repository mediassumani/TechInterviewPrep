
from collections import deque

  def isSameTree(self, p, q):
      if not p and not q:
          return True

      elif (p and not q) or (q and not p):
          return False

      queu_one = deque([p])
      queu_two = deque([q])

      while len(queu_one) > 0 and len(queu_two) > 0:

          curr_one = queu_one.popleft()
          curr_two = queu_two.popleft()

          if curr_one.val != curr_two.val:
              return False

          if curr_one.left and curr_two.left:
              queu_one.append(curr_one.left)
              queu_two.append(curr_two.left)

          elif (curr_one.left and not curr_two.left) or (curr_two.left and not curr_one.left):
              return False

          if curr_one.right and curr_two.right:
              queu_one.append(curr_one.right)
              queu_two.append(curr_two.right)

          elif (curr_one.right and not curr_two.left) or (curr_two.right and not curr_one.right) :
              return False
      return True
            
