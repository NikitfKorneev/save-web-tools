import random
import tkinter
import tkinter.ttk

canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="grey11")
canvas.pack()

d = []
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []


def generate():
    global d
    global d2
    global d3
    global d4
    global d5
    global d6
    global d7
    entry_2.delete(0,tkinter.END)
    a = int(entry.get())
    h = len(f"{a}")
    h = h - 2
    entry.delete(0,h)
    if a > 40:
        entry.delete(0,tkinter.END)
        entry.insert(0,"40")
        a = int(entry.get())
    b = cbtn_variable.get()
    b2 = cbtn2_variable.get()
    b3 = cbtn3_variable.get()
    b4 = cbtn4_variable.get()
    b5 = cbtn5_variable.get()
    b6 = cbtn6_variable.get()
    b7 = cbtn7_variable.get()
    if b == True:
        d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if b2 == True:
        d2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if b3 == True:
        d3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if b4 == True:
        d4 = ["$", "@", "&", "?"]
    if b5 == True:
        d5 = ["+", "-", "*", "/"]
    if b6 == True:
        d6 = ["%", "=", "!", "№"]
    if b7 == True:
        d7 = ["_", "^", ",", "."]
    if b == False:
        d.clear()
    if b2 == False:
        d2.clear()
    if b3 == False:
        d3.clear()
    if b4 == False:
        d4.clear()
    if b5 == False:
        d5.clear()
    if b6 == False:
        d6.clear()
    if b7 == False:
        d7.clear()
    d_all = d + d2 + d3 + d4 + d5 + d6 + d7
    for x in range(a):
        c = random.choice(d_all)
        entry_2.insert(tkinter.END,c)


cbtn_variable = tkinter.BooleanVar()
cbtn2_variable = tkinter.BooleanVar()
cbtn3_variable = tkinter.BooleanVar()
cbtn4_variable = tkinter.BooleanVar()
cbtn5_variable = tkinter.BooleanVar()
cbtn6_variable = tkinter.BooleanVar()
cbtn7_variable = tkinter.BooleanVar()

text = tkinter.Label(canvas,
                     text="Генератор",
                     bg="grey11",
                     foreground="white",
                     font=("bold script", 35, "bold"))
text.place(x=270, y=30)

text_2 = tkinter.Label(canvas,
                       text="Паролей",
                       bg="grey11",
                       foreground="white",
                       font=("bold script", 35, "bold"))
text_2.place(x=287, y=100)

cool = canvas.create_rectangle(50, 450, 700, 180, fill="grey95")

cbtn = tkinter.Checkbutton(canvas,
                           text="0-9",
                           variable=cbtn_variable,
                           offvalue=False,
                           onvalue=True)
cbtn.place(x=60, y=350)

cbtn2 = tkinter.Checkbutton(canvas,
                            text="a-z",
                            variable=cbtn2_variable,
                            offvalue=False,
                            onvalue=True)
cbtn2.place(x=120, y=350)

cbtn3 = tkinter.Checkbutton(canvas,
                            text="A-Z",
                            variable=cbtn3_variable,
                            offvalue=False,
                            onvalue=True)
cbtn3.place(x=180, y=350)

cbtn4 = tkinter.Checkbutton(canvas,
                            text="$@&?",
                            variable=cbtn4_variable,
                            offvalue=False, onvalue=True)
cbtn4.place(x=240, y=350)

cbtn5 = tkinter.Checkbutton(canvas,
                            text="+-*/",
                            variable=cbtn5_variable,
                            offvalue=False,
                            onvalue=True)
cbtn5.place(x=305, y=350)

cbtn6 = tkinter.Checkbutton(canvas,
                            text="%=№!",
                            variable=cbtn6_variable,
                            offvalue=False,
                            onvalue=True)
cbtn6.place(x=370, y=350)

cbtn7 = tkinter.Checkbutton(canvas,
                            text="_^,.",
                            variable=cbtn7_variable,
                            offvalue=False,
                            onvalue=True)
cbtn7.place(x=435, y=350)

btn = tkinter.ttk.Button(canvas,
                         text="Сгенерировать пароль",
                         width=50, command=generate)
btn.place(x=200, y=300)

entry = tkinter.Entry(canvas, width=2)
entry.place(x=80, y=300)

entry_2 = tkinter.Entry(canvas,
                        width=50,
                        justify=tkinter.RIGHT,
                        font=("Arial", 15, "bold"))
entry_2.place(x=100, y=250)


window.mainloop()