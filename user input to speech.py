from gtts import gTTS
import os
from tkinter import *
root= Tk()
canvas=Canvas(root,height=300,width=400)
canvas.pack()

def texttospeech():
    text= entry.get()
    output=gTTS(text=text, lang="en",slow=False)
    output.save("output1.mp3")
    os.system("start output1.mp3")
entry=Entry()
canvas.create_window(200,180,window=entry)
button=Button(text="start", command=texttospeech)
canvas.create_window(200,230,window=button)
root.mainloop()