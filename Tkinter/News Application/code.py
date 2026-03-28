import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
import io
import webbrowser

class NewsApp:
    def __init__(self):

        # fetch data
        self.photo = None
        self.root = None
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8db135d97e084f25836260f3a0278255").json()
        # print(self.data)
        #initial GUI load
        self.load_GUI()
        #load the 1st news item
        self.load_news_item(0)
        #load the engine
        self.root.mainloop()

    def load_GUI(self):
        self.root = Tk()
        self.root.title("News App")
        self.root.geometry("350x600")
        self.root.resizable(0,0)
        self.root.config(bg="black")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        #clear the screen for next item
        self.clear()

        #upload image
        try:
            img_url = self.data["articles"][index]["urlToImage"]
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            self.photo = ImageTk.PhotoImage(im)
        except:
            img_url = "https://www.shutterstock.com/image-vector/image-not-found-failure-network-260nw-2330163829.jpg"
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            self.photo = ImageTk.PhotoImage(im)

        label = Label(self.root,image=self.photo)
        label.pack()

        #show the headline of the news
        heading = Label(self.root,text = self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify="center")
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        #show news details
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=350,
                        justify="center")
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        #buttons container
        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill='both')

        #button
        if index != 0:
            prev = Button(frame,text="Previous",bg='white',fg='black',width=16,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side="left")

        if index != len(self.data["articles"])-1:
            next_b = Button(frame,text="Next",bg='white',fg='black',width=16,height=3,command=lambda :self.load_news_item(index+1))
            next_b.pack(side="right")

        read = Button(frame, text="Read", bg='blue', fg='white', width=16, height=3,command= lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side="right")

    def open_link(self,url):
        webbrowser.open(url)

obj = NewsApp()