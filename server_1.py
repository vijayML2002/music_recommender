import pygame
import socket
import time

from recom_queue import fill_queue
from queue_dll import push,pop,Node

pygame.mixer.init()
q = fill_queue()

def refresh_queue():
   global q
   q = fill_queue()

def music_on():   
      song = pop(q)
      pygame.mixer.music.load(song[0])
      pygame.mixer.music.play(loops=0)
      push(q,Node(song[0],song[1],song[2]))
         

def server_manual():
   s = socket.socket()
   port = 123               
     
   s.bind(('', port))   
   s.listen(5)                  
     
   while True:
      c, addr = s.accept()
      print("Request accepted - {}".format(addr))
      music_on()
      c.close()
      
   s.close()

def server_auto():
   s = socket.socket()
   port = 123                
     
   s.bind(('', port))   
   s.listen(5)

   start = time.time()
   
   while True:
      try:

         flag = 1
         
         c, addr = s.accept()
         s.settimeout(2)
         print("Request accepted - {}".format(addr))
         data = c.recv(1024)
         string = data.decode('utf8')
         c.close()

         if int(string) == 0:
            pygame.mixer.music.stop()
            return

         if int(string) == 1:
            flag = 0

         if int(string) == 2:
            refresh_queue()

         if addr and flag == 0:
            music_on()
            
      except:
         pass

      if not pygame.mixer.music.get_busy():
         music_on()

               
      
   s.close()

server_auto()
