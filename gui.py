from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from database import insert_music,song_bucket
from database import update_clicks,clear_mark,mark_song
from recom_queue import fill_queue
from queue_dll import push,pop,Node
import pygame,time
import socket,time

def request():
    s = socket.socket()          
    port = 12345                

    try:  
        s.connect(('127.0.0.1', port)) 
        return s.recv(1024).decode() 
    except:
        return 0

    s.close()

def request_song(num):
    
    s = socket.socket()          
    port = 123                

    try:  
        s.connect(('127.0.0.1', port))
        s.sendall(str(num).encode('utf8'))
    except:
        return 0

    s.close()  


pygame.mixer.init()

root = Tk()
current_mood = StringVar()

queue = fill_queue()

root.title('Music Recommender')
root.geometry("1000x480")
root.resizable(width=False,height=False)
root.iconbitmap('D:/studies/cse/ML-APPLICATION/music recommendation/headphone_icon_151736.ico')


#global variable
current_mood.set("neutral")

def add_song():
    
    s = filedialog.askopenfilename(initialdir="D:/studies/cse/ML-APPLICATION/music recommendation/test music/",multiple=True,title="Choose the song",filetypes=(("mp3 Files","*.mp3"),))
    for song in s:
        insert_music(song)
        song = song.replace("D:/studies/cse/ML-APPLICATION/music recommendation/test music/","")
        song = song.replace(".mp3","")
        listbox.insert(END,song)


def play_song():
    #update()
    song = listbox.get(ACTIVE)
    song = f'D:/studies/cse/ML-APPLICATION/music recommendation/test music/{song}.mp3'
    update_clicks(song)
    clear_mark()
    mark_song(song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    #update()
    pygame.mixer.music.stop()
    try:
        request_song(0)
    except:
        pass
    listbox.selection_clear(ACTIVE)

def recommendation():

    try:
        request_song(1)
    except:
        print("request denied")
        pass

        
def update():
    s = request()
    if(s):
        current_mood.set(s)
    else:
        print("no response")

e = Entry(root,width=90).place(x=30,y=50)

attach = Button(root,width=37,text="ATTACH WEIGHTS").place(x=30,y=80)
release = Button(root,width=37,text="RELEASE WEIGHTS").place(x=306,y=80)
upload = Button(root,width=76,text="UPLOAD MUSIC",command=add_song).place(x=30,y=380)
curr_text = Label(root,textvariable=current_mood).place(x=30,y=340)
recommend = Button(root,width=76,text="RECOMMEND MUSIC",command=recommendation).place(x=30,y=420)
play = Button(root,width=37,height=10,text="PLAY",command=play_song).place(x=30,y=170)
refresh = Button(root,width=2,height=1,command=update).place(x=550,y=340)
stop = Button(root,width=37,height=10,text="STOP",command=stop).place(x=306,y=170)


scrollbar = Scrollbar(root) 
scrollbar.pack(side = RIGHT, fill = BOTH) 

listbox = Listbox(root,width=60) 
listbox.pack(side = RIGHT, fill = BOTH,pady=15,padx=10)

songs = song_bucket()
for song in songs:
    try:
        song = song[1].replace("D:/studies/cse/ML-APPLICATION/music recommendation/test music/","")
        song = song.replace(".mp3","")
        listbox.insert(END,song)
    except:
        pass

listbox.config(yscrollcommand = scrollbar.set) 
scrollbar.config(command = listbox.yview)

root.mainloop()

