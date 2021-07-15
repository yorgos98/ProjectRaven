from tkinter import *

root = Tk()

#Creating a function called "MyClick"
#the purpose of this function is to display text saying "test" under the button after it is clicked.
def Myclick():
    MyLabel = Label(root, text="test")
    MyLabel.pack()


#Creates button within "root" and names in "click me"
MyButton = Button(root, text= "click me",command=Myclick, fg="red", bg="blue")

MyButton.pack()

#Creates a loop
root.mainloop()