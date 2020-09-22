import os

import tkinter as tk
import tkinter.ttk as ttk

from PIL import ImageTk, Image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_PATH = os.path.join(BASE_DIR, 'images')



root = tk.Tk()
root.title("Image Gallery")
root.geometry("600x500")

mainframe = ttk.Frame(root, padding=10)
info_frame = ttk.Frame(mainframe)
image_frame = ttk.Frame(mainframe, relief=tk.SOLID)
tool_frame = ttk.Frame(mainframe)
mainframe.pack(expand=True, fill=tk.BOTH)
info_frame.grid(stick=(tk.E, tk.W))
image_frame.grid(row=1, column=0, sticky=(tk.E, tk.W, tk.S, tk.N))
tool_frame.grid(row=2, column=0, sticky=(tk.E, tk.W))

img_filename_label = ttk.Label(info_frame, text="Image filename")
img_filename_label.pack(side=tk.LEFT, padx=3)


# Image
size = (300, 300)
img = Image.open(os.path.join(IMAGES_PATH, 'img1.jpg'))
img.thumbnail(size)
img_tk = ImageTk.PhotoImage(img)
label = ttk.Label(image_frame, image=img_tk)
label.pack(expand=True)


previous_button = ttk.Button(tool_frame, text="Previous")
next_button = ttk.Button(tool_frame, text="Next")
previous_button.grid(row=0, column=0, sticky=tk.W)
next_button.grid(row=0, column=1, sticky=tk.E)
tool_frame.columnconfigure(0, weight=1)
tool_frame.columnconfigure(1, weight=1)

for child in mainframe.winfo_children():
	child.grid_configure(padx=10, pady=10)

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)

root.mainloop()