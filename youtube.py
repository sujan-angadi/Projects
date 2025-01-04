from pytubefix import YouTube   #use pip install pytube to install the library and also install pytubefix using pip instal pytubefix
from tkinter import *          #use pip install tk to install tkinter libraries

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("600x250")

def get():
    url = urlvar.get()
    video = YouTube(url)
    down = video.streams.get_highest_resolution(f'{resvar.get()}').download()
    print("Download Complete!!")
      
lab = Label(root, text="Enter url: ")
lab.place(x= 120, y= 50)
lab2 = Label(root, text= "Choose Resolution (Only supported by videos!)\nYou can add your own resolution in the list box if you wish!!").place(x= 170, y= 0)
urlvar = StringVar()
resvar = StringVar()

enrty = Entry(root, textvariable= urlvar, width= 40)
enrty.place(x= 200, y= 50)

res = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p']
for i in res:
    Radiobutton(root, text= i, padx= 10, value= i, variable= resvar).pack(anchor='w')

btn = Button(root, text= "Download Now!", command= get)
btn.place(x= 220 , y= 90)

root.mainloop()