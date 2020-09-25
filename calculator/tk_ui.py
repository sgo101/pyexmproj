import tkinter as tk

from tkinter import ttk


def clear_one():
	pass

def clear_all():
	pass

def power():
	pass

def div():
	pass



root = tk.Tk()
root.title("Tkinter Calculator")
mainframe = ttk.Frame(root, padding=10)
mainframe.pack(expand=True, fill=tk.BOTH)

output = ttk.Entry(mainframe)
output.grid(row=0, column=0, columnspan=4)

col = 0
for item in ['C', 'CC', '^', '/']:
	ttk.Button(mainframe, text=item).grid(row=1, column=col)
	col += 1

row = 2
col = 0
for num in range(9, 0, -1):
	if col >= 3:
		row += 1
		col = 0
	ttk.Button(mainframe, text=num).grid(row=row, column=col)
	col += 1

row = 2
for item in ['*', '-', '+']:
	ttk.Button(mainframe, text=item).grid(row=row, column=3)
	row += 1


col = 0
for item in ['0', '.', '=']:
	if item == '=':
		ttk.Button(mainframe, text=item).grid(row=5, column=col, columnspan=2, sticky=(tk.W, tk.E))
	else:
		ttk.Button(mainframe, text=item).grid(row=5, column=col)
	col += 1


root.mainloop()
