from tkinter import *
from PIL import Image, ImageTk
import os

def next_image():
    global counter
    img_label.config(image=image_array[counter%len(image_array)])
    counter = counter + 1

def previous_image():
    global counter
    counter = counter - 1
    img_label.config(image=image_array[counter%len(image_array)])

counter = 1
root = Tk()
root.geometry("500x500")
root.title("Wallpaper Viewer")
root.configure(bg="black")

files = os.listdir("Wallpaper")
image_array = []
for file in files:
    img = Image.open(os.path.join("Wallpaper",file))
    resized_img = img.resize((200,250))
    image_array.append(ImageTk.PhotoImage(resized_img))
# print(image_array)

img_label = Label(root, image=image_array[0])
img_label.pack(pady=(15,10))

next_button = Button(root,text="Next",bg="white",fg="black",width=25,height=2,command=next_image)
next_button.pack()

next_button = Button(root,text="Previous",bg="white",fg="black",width=25,height=2,command=previous_image)
next_button.pack(pady=(5,5))

root.mainloop()