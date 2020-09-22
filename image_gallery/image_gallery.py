import tkinter as tk
import tkinter.ttk as ttk



root = tk.Tk()
root.title("Image Gallery")

mainframe = ttk.Frame(root, padding=10)
image_frame = ttk.Frame(mainframe, relief=tk.SOLID)
tool_frame = ttk.Frame(mainframe, relief=tk.GROOVE)
mainframe.pack(expand=True, fill=tk.BOTH)
image_frame.grid(sticky=(tk.E, tk.W, tk.S, tk.N))
tool_frame.grid(row=1, column=0, sticky=(tk.E, tk.W))

img1 = tk.PhotoImage(file='python_logo.gif')
img_label1 = ttk.Label(image_frame, image=img1)
img_label1.pack()

next_button = ttk.Button(tool_frame)
previous_button = ttk.Button(tool_frame)
next_button.grid()
previous_button.grid()

for child in mainframe.winfo_children():
	child.grid_configure(padx=10, pady=10)

root.mainloop()