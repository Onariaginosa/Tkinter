from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Fuck da Police in my Gucci flip flops", entrytxt)

def addtolist():
    entrytxt = entry1.get()
    listbox1.insert(END, entrytxt)    
    entry1.delete(0,END)

def addtolist2(event):
    entrytxt = entry1.get()
    listbox1.insert(END, entrytxt)
    entry1.delete(0,END)

def clearlist(event):
    listbox1.delete(0, END)











root = Tk() #gives us a blank canvas object to work with
root.title("my first GUI program ")

button1 = Button(root, text="bitches be crazy", command=addtolist)
button1.grid(row=1, column= 1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)
entry1.bind("<Return>", addtolist2)


label1 = Label(root, text="beyonce runs the world", bg="pink", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=2)

listbox1 = Listbox(root)
listbox1.grid(row=2, column=0, columnspan=2, sticky=EW)
listbox1. bind("<Button-1>", clearlist)

listbox1.insert(END, "Ona", "is", "a", "boss", "ass", "bitch")



mainloop() #causes the windows to display on the screen until program closes