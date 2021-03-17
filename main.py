from PIL import Image, ImageTk
import tkinter as tk

from pynput import keyboard
import threading


# region keyboard listener
pressed = []


def on_press(key):
    global down, up, pressed

    if(key not in pressed):
        pressed.append(key)
        print("pressed"+str(key))

        canvas.create_image((0, 0), anchor="nw", image=down)


def on_release(key):
    global up, pressed

    print("released"+str(key))
    pressed.remove(key)

    if(len(pressed) == 0):
        canvas.create_image((0, 0), anchor="nw", image=up)


def thread_function():

    print("start thread")
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()


x = threading.Thread(target=thread_function)
x.start()

# endregion

# region tkinter

root = tk.Tk()
up = ImageTk.PhotoImage(Image.open("up.jpg"))
down = tkimage = ImageTk.PhotoImage(Image.open("down2.jpg"))

root.resizable(False, False)
canvas = tk.Canvas(width=480, height=360)
canvas.pack(side="top", fill="both", expand=True)
canvas.create_image((0, 0), anchor="nw", image=up)

root.mainloop()

# endregion
