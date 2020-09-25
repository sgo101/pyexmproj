import tkinter as tk

from tkinter import ttk



def calculate():
	equation.set(eval(equation.get()))

def set_key(event=None):
	# callect all text inside the entry and make the equation
	equ = equation.get() + str(event.widget["text"])
	equation.set(equ)

def clear_one():
	equation.set(equation.get()[:-1])

def clear_all():
	equation.set('')


root = tk.Tk()
root.title("Tkinter Calculator")
mainframe = ttk.Frame(root, padding=10)
mainframe.pack(expand=True, fill=tk.BOTH)

equation = tk.StringVar()
output = ttk.Entry(mainframe, textvariable=equation)
output.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.S, tk.N), pady=5)

d = {'C': clear_one, 'CC': clear_all}
col = 0
for item, func in d.items():
	ttk.Button(mainframe, text=item, command=func).grid(
				row=1, column=col, sticky=(tk.W, tk.E, tk.S, tk.N))
	col += 1

col = 2
for item in ["**", '/']:
	b = ttk.Button(mainframe, text=item)
	b.grid(row=1, column=col, sticky=(tk.W, tk.E, tk.S, tk.N))
	b.bind("<Button-1>", set_key)
	col += 1

row = 2
col = 0
for num in range(9, 0, -1):
	if col >= 3:
		row += 1
		col = 0
	b = ttk.Button(mainframe, text=num)
	b.grid(row=row, column=col, sticky=(tk.W, tk.E, tk.S, tk.N))
	b.bind("<Button-1>", set_key)
	col += 1

row = 2
for item in ['*', '-', '+']:
	b = ttk.Button(mainframe, text=item)
	b.grid(row=row, column=3, sticky=(tk.W, tk.E, tk.S, tk.N))
	b.bind("<Button-1>", set_key)
	row += 1


col = 0
for item in ['0', '.', '=']:
	if item == '=':
		ttk.Button(mainframe, text=item, command=calculate).grid(
					row=5, column=col, columnspan=2, sticky=(tk.W, tk.E, tk.S, tk.N))
	else:
		b = ttk.Button(mainframe, text=item)
		b.grid(row=5, column=col, sticky=(tk.W, tk.E, tk.S, tk.N))
		b.bind("<Button-1>", set_key)
	col += 1

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=4)
mainframe.rowconfigure(2, weight=4)
mainframe.rowconfigure(3, weight=4)
mainframe.rowconfigure(4, weight=4)
mainframe.rowconfigure(5, weight=4)
root.mainloop()
