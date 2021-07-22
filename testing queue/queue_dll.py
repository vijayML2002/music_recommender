class Node():
  def __init__(self, path, hp):
    self.prev = None
    self.data = [path,hp]
    self.next = None

class Queue():
  def __init__(self):
    self.top = None
    self.back = None

def display_top(s): 
  temp = s.top
  a = ''
  while temp != None: 
    print(temp.data)
    temp = temp.prev

def display_back(s):
  temp = s.back
  a = ''
  while temp != None:
    print(temp.data)
    temp = temp.next


def is_empty(s):
  if s.top == None:
    return 1
  return 0

def push(s, n):
  if is_empty(s): 
    s.top = n
    s.back = n
  else:
    s.back.prev = n
    temp = s.back
    s.back = n
    s.back.next = temp

def pop(s):
  if is_empty(s):
    return 0
  else:
    x = s.top.data
    if s.top.prev == None: 
      s.top = None
      s.back = None
    else:
      temp = s.top.prev
      temp.next = None
      #del s.top
      s.top = temp
    return x
