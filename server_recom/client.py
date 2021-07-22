import socket,time                
import pygame


def request_song(num):
    s = socket.socket()          
    port = 123                

    try:  
        s.connect(('127.0.0.1', port))
        s.sendall(str(num).encode('utf8'))
    except:
        return 0

    s.close()  
