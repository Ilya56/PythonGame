import os
from tkinter import *  # GUI
from random import shuffle  # random for lists
from tkinter import messagebox

print("Game")

SIDE = 8  # size
QSIDE = SIDE ** 2 // 2  # unique pictures
prev = None  # nothing
score = 0


def cmd():
    print("Something")
    print('...')


def hide_all(buttons):
    """hide all buttons"""
    for btn in buttons:
        btn.configure(image=faq)


def hide_both(prev, btn):
    """hide activated buttons"""
    if not prev.double:
        prev.configure(image=faq)
    if not btn.double:
        btn.configure(image=faq)


def change(btn, l):
    """change img if clicked"""
    global prev, score
    btn.configure(image=btn.img)
    if prev is None:
        prev = btn
    else:
        if prev.x != btn.x:
            main_window.after(500, hide_both, prev, btn)
            score += 1
        elif prev is btn:
            hide_both(prev, btn)
        else:
            prev.double = True
            btn.double = True
            if score > 5:
                score -= 5
            else:
                score = 0
        prev = None

    l.configure(text="Score " + str(score))

    # winning
    win = True
    for btn in buttons:
        if not btn.double:
            win = False
    if win:
        messagebox._show("Message", "You win!")


# create window
main_window = Tk()
main_window.title("The game")
main_window.resizable(width=False, height=False)

files = [os.path.join("gif", f) for f in os.listdir("gif")]
shuffle(files)
files = files[0:QSIDE] * 2
shuffle(files)

faq = PhotoImage(file="FAQ.gif")
images = [PhotoImage(file=f) for f in files]
l = Label(main_window, text="Score " + str(score))

buttons = []
for i in range(SIDE):
    for j in range(SIDE):
        btn = Button(main_window,
                     image=images[i * SIDE + j],
                     relief=FLAT)
        btn.configure(command=lambda b=btn: change(b, l))  # lambda for each button
        btn.img = images[i * SIDE + j]
        btn.x = files[i * SIDE + j]
        btn.double = False
        btn.grid(row=i, column=j)
        buttons.append(btn)

l.grid(row=SIDE, column=0)
main_window.after(2000, hide_all, buttons)

main_window.mainloop()
