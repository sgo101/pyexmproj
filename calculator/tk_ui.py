import tkinter as tk

from tkinter import ttk



root = tk.Tk()
root.title('Calculator')

output_pad = ttk.Frame(root)
num_pad = ttk.Frame(root)

output = ttk.Entry(output_pad)
output.grid(row=0, column=0, sticky='wesn')

# buttons
col_num = 0
row_num = 0
for num in range(10):
    ttk.Button(num_pad, text=num).grid(row=row_num, column=col_num)
    if col_num % 3 == 0:
        col_num = 0
        row_num += 1
    col_num += 1
    
        





output_pad.grid(row=0, column=0, sticky='nesw')
num_pad.grid(row=1, column=0)

root.mainloop()
