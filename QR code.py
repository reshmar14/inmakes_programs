from tkinter import*
import pyqrcode
from PIL import ImageTk,Image
root=Tk()

def generate():
    link_name=entry_name.get()
    link=entry_link.get()
    file_name=link_name + ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=5)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image =image)
    image_label.image=image
    canvas.create_window(200,400,window=image_label)
canvas=Canvas(root,width=400,height=600)
canvas.pack()
app_label=Label(root,text='QR CODE GENERATOR', fg="blue")
canvas.create_window(200,50,window=app_label)
name_label=Label(root,text="LINK NAME")
link_label=Label(root,text="LINK")
canvas.create_window(200,150,window=name_label)
canvas.create_window(200,200,window=link_label)
entry_name=Entry(root)
entry_link=Entry(root)
canvas.create_window(300,150,window=entry_name)
canvas.create_window(300,200,window=entry_link)
button=Button(root,text="Generate QR Code", command=generate)
canvas.create_window(300,250,window=button)





root.mainloop()