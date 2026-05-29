import tkinter as tk
from PIL import Image, ImageTk
import random
root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'black')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0, bg='black')
canvas.pack()
img = Image.open('error.png')
spider_img = ImageTk.PhotoImage(img)
def add_spider():
    x = random.randint(0, width)
    y = random.randint(0, height)
    canvas.create_image(x, y, image=spider_img)
    root.after(200, add_spider)

add_spider()
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.mainloop()
