from tkinter import *
from tkinter import ttk

root = Tk()

root.attributes("-alpha", 0.9)
root.title('Music Recommender')
root.geometry("1000x480")
root.resizable(width=False,height=False)
root.iconbitmap('D:/studies/cse/music recommendation/headphone_icon_151736.ico')

my_notebook = ttk.Notebook(root)
my_notebook.pack()

tab1 = Frame(my_notebook, width=1000, height=480, bg = "black")
tab2 = Frame(my_notebook, width=1000, height=480)

tab1.pack(fill="both",expand=1)
tab2.pack(fill="both",expand=1)

my_notebook.add(tab1,text="home")
my_notebook.add(tab2,text="recommendation")

img_play = PhotoImage(file="./play.png")
play = Button(tab1,text="play",borderwidth=0).place(x=30,y=170)

scrollbar = Scrollbar(tab1) 
scrollbar.pack(side = RIGHT, fill = BOTH) 
listbox = Listbox(tab1,width=40,font=('MS Gothic',15),borderwidth=0)
listbox.pack(side = RIGHT, fill = BOTH,pady=15,padx=10)
listbox.config(yscrollcommand = scrollbar.set) 
scrollbar.config(command = listbox.yview)

root.mainloop()
