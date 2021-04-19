from tkinter import *
from pytube import YouTube
import time

root = Tk()
root.geometry("500x450")
root.title("Youtube video downloader")
root.config(bg="red")


def download():
    #entry.delete(0, END)
    bidiyo = entry.get()
    info_label.config(text="Starting to download...")
    YouTube(bidiyo).streams.first().download()
    info_label2.config(text="Download Successfull")
    time.sleep(2)
    #root.destroy()

header = Label(root, text="YouTube Video Downloader", font=("Helvetica", 25, "bold"), fg="red")
header.pack(pady=20)

label = Label(root, text="Enter the video link below", font=("Arial", 20, "bold")) #https://youtu.be/37L1eMd16RU
label.pack(pady=20)

entry = Entry(root, font=("times", 15), width=30)
entry.pack(pady=20)

button = Button(root, text="Download", bd=3, command=download)
button.pack(pady=20)

info_label = Label(root, text="", font=("times", 15, "bold"))
info_label.pack(pady=20)

info_label2 = Label(root, text="", font=("times", 15, "bold"))
info_label2.pack(pady=20)


root.mainloop()