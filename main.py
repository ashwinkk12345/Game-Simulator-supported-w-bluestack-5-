from pynput.keyboard import Controller
import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import serial
import warnings
from PIL import Image, ImageTk

# ------------------------------------ GUI ------------------------------------

# create window
window = tk.Tk()
window.title("Game Simulator V1.0")
window.geometry("600x400")
window.resizable(width=False, height=False)
window.attributes('-alpha', 0.95)

# set style
style = ttk.Style()
window.tk.call('source', 'Azure-ttk-theme-main/azure.tcl')
window.tk.call("set_theme", "dark")

# add bg image
img = Image.open('bg_img.png')
photo = ImageTk.PhotoImage(img)
bg_label = tk.Label(window, image=photo)
bg_label.image = photo  # Keep reference to avoid garbage collection
bg_label.place(x=0, y=0)


# even when item selected from drop-down menu
def on_select(event):
    global val
    val = drop.get()
    if val:
        messagebox.askokcancel(type='ok',
                               message="invalid COM port",
                               icon='warning')
        window.destroy()


# add drop-down menu
drop = ttk.Combobox(window, values=["1", "2", "3", "4", "5", "6"], width=30)
drop.pack(pady=180)

drop.bind("<<ComboboxSelected>>", on_select)
window.mainloop()

# ----------------------------------- Serial -----------------------------------

try:
    bus = serial.Serial(port=f"COM{int(val)}", baudrate=115200, timeout=.1)
except:
    warnings.warn("entered COM port is incorrect or device not connected !!!")
else:
    keyboard = Controller()
    k = 'd'
    x, y = 960, 540  # aspect ratio: 1920, 1080
    temp_x, temp_y = 0, 0


    def value_press(key):
        if key != 'd':
            keyboard.press(key)
            keyboard.release(key)


    def move_cursor(x, y):
        pyautogui.moveTo(x, y)


    def map_range(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


    while True:
        data = str(bus.readline())
        # print(len(data))
        if data[2:4].isdigit():
            x = map_range(int(data[2]), 0, 9, 480, 1440)
            y = map_range(int(data[3]), 0, 9, 270, 810)
        elif data[2].isalpha():
            k = data[2]
            x = map_range(int(data[3]), 0, 9, 480, 1440)
            y = map_range(int(data[4]), 0, 9, 270, 810)

        print(f"x : {x}, y : {y}, key : {k}")
        if len(data) == 8:
            value_press(k)
            k = 'd'

        if temp_x != x or temp_y != y:
            temp_x = x
            temp_y = y
            move_cursor(x, y)
