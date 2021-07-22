import socket,time                
from image_process import required_image,get_emotion_details


print("Setting up the server for emotion detection")
import emotion_detection

def get_data(num):
   image = required_image(num)
   data = emotion_detection.emotions(image)
   data = get_emotion_details(data)
   return data

def server_on(num,data):
   s = socket.socket()
   port = 12345                
     
   s.bind(('', port))   
   s.listen(5)                  
     
   start = time.time()

   while True:
      c, addr = s.accept()
      print("Request accepted - {}".format(addr))
      c.send(data.encode()) 
      c.close()
      if time.time()-start>num:
         break

   s.close()


while True:
   print("Data collection")
   data = get_data(3)
   print("Server - on")
   server_on(30,data)
   print("Server - off")

