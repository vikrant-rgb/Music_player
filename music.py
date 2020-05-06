from pygame import mixer
import tkinter as tk
from tkinter import *


def Play_music():
    mixer.init()
    global E1
    string = E1.get()
    
    mixer.music.load(string)
    volume = slider.get()
    mixer.music.set_volume(volume/100)
    mixer.music.play()
    while True:
        print("Press p to pause and r to resume")
        print("Press s to stop and exit the program")
        query = input(">>>>>")
        if query == 'p':
            mixer.music.pause()
            print("music paused")
        elif query == 'r':
            mixer.music.unpause()
        elif query == 's':
            mixer.music.stop()
            print("music stopped")
            break
        else:
            print("Please enter a valid input")        

root=tk.Tk()
w = tk.Label(root, text="Music Player")
w.grid(row=0, column=1, columnspan=1)
E1 = tk.Entry(root, bd=20)
E1.grid(row=1, column=1, columnspan=1)
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider.grid(row=2, column=1, columnspan=1)

button = tk.Button(root, text="Play", fg="blue", command=Play_music)
button.grid(row=5, column=0)

button2 = tk.Button(root, text="Quit", fg="red", command=root.destroy)
button2.grid(row=5, column=1)


root.mainloop()



