import os
import glob

import tkinter as tk
import tkinter.ttk as ttk

from PIL import ImageTk, Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_PATH = os.path.join(BASE_DIR, 'images')
# list of all image's file path with ext of jpg
IMAGES_LIST = glob.glob(os.path.join(IMAGES_PATH, "*.jpg"))

size = (300, 300)
img_index = 0

def display_img(index):
	with Image.open(IMAGES_LIST[index]) as img_file:
		img_file.thumbnail(size)
		label.img = ImageTk.PhotoImage(img_file)
		label.config(image=label.img)


def on_next():
	global img_index
	img_index += 1

	if img_index >= len(IMAGES_LIST):
		img_index = 0

	display_img(img_index)


def on_previous():
	global img_index
	img_index -= 1

	if img_index >= len(IMAGES_LIST):
		img_index = 0

	display_img(img_index)


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


# Set first image to label
img_file = Image.open(IMAGES_LIST[img_index])
img_file.thumbnail(size)
img = ImageTk.PhotoImage(img_file)
label = ttk.Label(image_frame, image=img)
label.pack(expand=True)


previous_button = ttk.Button(tool_frame, text="Previous", command=on_previous)
next_button = ttk.Button(tool_frame, text="Next", command=on_next)
previous_button.grid(row=0, column=0, sticky=tk.W)
next_button.grid(row=0, column=1, sticky=tk.E)
tool_frame.columnconfigure(0, weight=1)
tool_frame.columnconfigure(1, weight=1)

for child in mainframe.winfo_children():
	child.grid_configure(padx=10, pady=10)

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)

root.mainloop()