from tkinter import *
from tkinter import filedialog
from pytube import YouTube


def download():
    video = YouTube(textbox.get())
    stream = video.streams.get_highest_resolution()
    stream.download(output_path= filedialog.askdirectory())

tk = Tk()
tk.title("Youtube Download")
Label(tk,text="Cole o link aqui").pack()

textbox = Entry(tk,width=49)
textbox.place(x=1, y= 20)


Botao = Button(tk, width=10,text= 'Download', command= download).place(x=110, y=50)

tk.geometry("300x100")
tk.mainloop()