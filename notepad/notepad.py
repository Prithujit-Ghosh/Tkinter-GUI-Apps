from tkinter import *
from tkinter import font
import os
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import re

root=Tk()
root.title("Untitled Notepad")
root.wm_iconbitmap("C:/Users/mrinm/Downloads/notes_2_43442.ico")# Add the path to your .ico file here
root.geometry("800x600")

def newFile():
    global file
    root.title("Untitled Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        TextArea.delete(1.0,END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("all Files", "*.*"),("Text Documents","*.txt")])

        if file=="":
            file=None
        else:
            #save as a new file
            f= open(file,"w")
            f.write(TextArea.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(file)+"-Notepad")
            print("File saved")
            
    else:
        #save the file
        f= open(file,"w")
        f.write(TextArea.get(1.0, END))
        f.close()
            
def Quit():
    root.destroy()

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("About Notepad", "This is a simple notepad built with Tkinter. Enjoy note taking! ")

def Size(size):
    current_font.configure(size=size)

def Color(color):
    TextArea.config(fg=color)
    
def count_words(event):
    text=TextArea.get(1.0,END)

    status_var.set("Word Count: "+str(len(re.findall(r"\b[\w'-]+\b",text))))
    statusbar_label.update()

#Current font size
current_font = font.Font(size=14)

#Adding Scrollbar using rules
Scroll=Scrollbar(root)
Scroll.pack(side=RIGHT, fill=Y)

#status bar
f2=Frame(root,bg="grey")
f2.pack(side="bottom",fill="x")
status_var=StringVar()
status_var.set("Word Count: 0")

#Initializing this variable with none
file=None

#Add text area
TextArea= Text(root, font=current_font)
TextArea.pack(expand=True, fill=BOTH)

#word count
statusbar_label = Label(f2, textvariable=status_var, bg="grey", fg="white", anchor="w")
statusbar_label.grid(row=0,column=2)
TextArea.bind("<KeyRelease>", count_words)

#Let's create a menubar
Menubar=Menu(root)
FileMenu=Menu(Menubar, tearoff=0)

#Scroll bar
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

#To open a new File
FileMenu.add_command(label="New", command=newFile)

#To open already existing file
FileMenu.add_command(label="Open", command= openFile)

#To save the current file
FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=Quit)
Menubar.add_cascade(label="File", menu=FileMenu)

#EditMenu
EditMenu=Menu(Menubar, tearoff=0)
#To give a feature of cut
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)

Menubar.add_cascade(label="Edit", menu=EditMenu)

#Help Menu
HelpMenu=Menu(Menubar, tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
Menubar.add_cascade(label="Help", menu=HelpMenu)

#Font menu
FontMenu=Menu(Menubar,tearoff=0)

Menubar.add_cascade(label="Font", menu=FontMenu)

#Font size submenu
Font_Size=Menu(FontMenu,tearoff=0)

FontMenu.add_cascade(label="Font Size", menu=Font_Size)

for size in [4, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40]:
    Font_Size.add_command(label=str(size), command=lambda s=size: Size(s))

#Font color submenu
Font_Colour = Menu(FontMenu, tearoff=0)
FontMenu.add_cascade(label="Font Colour", menu=Font_Colour)

for color in ["black", "blue", "red", "green", "purple", "orange", "brown", "gray"]:
    Font_Colour.add_command(label=color.capitalize(), command=lambda c=color: Color(c))
root.config(menu=Menubar)

root.mainloop()
