from tkinter import *

root = Tk()

#Creating a text input box named "e" and assigning it a width along with changing the foreground color and backround color.
e = Entry(root, width = 50, fg="red", bg="blue", borderwidth= 5)
e.pack()

#Inserts pre written text within the box
e.insert(0,"Enter your name")


#Creating a function called "MyClick"
#This function starts by creating the "TestVal" Variable, inserting text and then grabbing the inputed data from the e variable above in which it puts them together.
def Myclick():
    TestVal = "hello Adventurer" + e.get()
    MyLabel = Label(root, text=TestVal )
    MyLabel.pack()


#Creates button within "root" and names in "click me"
MyButton = Button(root, text= "click me",command=Myclick, fg="red", bg="blue")

MyButton.pack()

#Creates a loop
root.mainloop()