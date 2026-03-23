from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email == "xx@gmail.com" or password == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Login Failed")

root = Tk()
root.title("Basic Interface")
# root.iconbitmap("")
# root.minsize(400,300)
root.geometry("500x600")
root.configure(background="#0096DC")

img = Image.open("flipkart.jpg")
#resize image
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
#to create a label to place the image in the GUI
img_Label = Label(root, image=img)
#gemotry manager to decide where the image is placed(pack,grid)
img_Label.pack(pady=(10,7))

text_label = Label(root, text="Flipkart",fg="white",bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana", 20))

#create email
email_label = Label(root,text="Email Address",fg="white",bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana", 12))

email_input = Entry(root,width=50,fg="black",bg="white")
email_input.pack(ipady=6,pady=(1,15))

#create password label
password_label = Label(root,text="Enter Password",fg="white",bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana", 12))

password_input = Entry(root,width=50,fg="black",bg="white")
password_input.pack(ipady=6,pady=(1,15))

#login button
login_btn = Button(root,text="Login Here",bg="white",fg="black",width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana", 10))

root.mainloop()
