from tkinter import*
import math
import random
from math import factorial
import re

def preprocess_expression(expr):
    if "^" in expr:
        expr=expr.replace("^","**")
    if "rem" in expr:
        expr=expr.replace("rem","%")
    expr = HandleRan(expr)
    expr = handle_combinatorics(expr)
    return expr

def handle_combinatorics(expr):
    expr = re.sub(r'(\d+)C(\d+)', r'nCr(\1,\2)', expr)
    expr = re.sub(r'(\d+)P(\d+)', r'nPr(\1,\2)', expr)
    return expr

def HandleRan(text):
    if "RAN#" in text:
        return text.replace("RAN#",str(random.randint(0,100)))
    else:
        return text
    
def Reciprocal(text):
    try:
        value=eval(HandleRan(scvalue.get()),{"builtins": None}, allowed_functions)
    except Exception as e:
        print(e)
        value="Error"
        return value
    value=eval("1/"+str(value))
    return value

def nCr(n, r):
    try:
        return factorial(n) // (factorial(r) * factorial(n - r))
    except:
        return "Error"

def nPr(n, r):
    try:
        return factorial(n) // factorial(n - r)
    except:
        return "Error"
    
allowed_functions = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'asin': math.asin,
    'acos': math.acos,
    'atan': math.atan,
    'π': math.pi,
    "exp":math.exp,
    "ln": math.log,
    "log":math.log10,
    "sqrt":math.sqrt,
    "e":math.e,
    'rad': math.radians,
    "RAN#": random.randint(1, 10),
    "fact": math.factorial,
    "nCr":nCr,
    "nPr":nPr

}

root=Tk()
root.geometry("636x500")
root.title("Calculator GUI")
root.wm_iconbitmap("C:/Users/mrinm/Downloads/2.ico")# Add the path to your .ico file here

def click(event):
    global scvalue
    tags = event.widget.gettags(event.widget.find_withtag("current"))
    text= str(tags[0])
    if text=="=":

        if scvalue.get().isdigit():
            value=int(scvalue.get())
        elif scvalue.get()=="Error":
            scvalue.set("")
            screen.update()
        else:
             try:
                 expr = preprocess_expression(scvalue.get())
                 value = eval(expr, {"builtins": None}, allowed_functions)
                 
             except Exception as e:
                 print(e)
                 value="Error"
            
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    elif text=="1/x":
         value=Reciprocal(text)
         scvalue.set(value)
         screen.update()
        
    elif text == "nCr":
        scvalue.set(scvalue.get() + "C")

    elif text == "nPr":
        scvalue.set(scvalue.get() + "P")
        
    elif text=="del":
        strdel=scvalue.get()
        scvalue.set(strdel[:-1])
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
              
scvalue=StringVar()
scvalue.set("")
screen= Entry(root, textvar=scvalue, font="lucida 40",bg="light blue")
screen.pack(fill=X, ipadx=10, padx=18, pady=10)

f1=Frame(root,bg="black", borderwidth=20, relief=SUNKEN)
f1.pack( fill="y", pady=5)

def create_circle_button(parent, text, row, col):
    canvas = Canvas(parent, width=60, height=60, highlightthickness=0)
    canvas.grid(row=row, column=col, padx=5, pady=5)
    if text=="C" or text=="del":
        colour="IndianRed1"
    elif text=="=":
        colour="light green"
    else:
        colour="gray"
    circle = canvas.create_oval(5, 5, 55, 55, fill=colour, outline="")
    label = canvas.create_text(30, 30, text=text, fill="Black", font=("Arial", 12, "bold"))
    
    # Taging both with the button text so we can identify them later
    canvas.addtag_withtag(text, circle)
    canvas.addtag_withtag(text, label)

    # Bind the click function to both the circle and label
    canvas.tag_bind(circle, "<Button-1>", click)
    canvas.tag_bind(label, "<Button-1>", click)

Buttons = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","rem","^",".","(",")","sqrt(","log(","ln(","sin(","cos(","tan(","asin(","acos(","atan(","e","π","nCr","nPr","fact(","rad(","RAN#","^2","1/x","C","del","="]

for i in range(5):
    for j in range(8):
        p = i * 8 + j
        create_circle_button(f1, Buttons[p], i, j)

root.mainloop()
