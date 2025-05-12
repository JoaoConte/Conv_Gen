import tkinter as tk
import tkinter.ttk as ttk

def fixed_map(option):
    return [elm for elm in style.map("Treeview", query_opt=option) if elm[:2] != ("!disabled", "!selected")]

root = tk.Tk()
style = ttk.Style()
style.map("Treeview", foreground=fixed_map("foreground"), background=fixed_map("background"))

w = tk.Label(root, text="Hello, world!")
w.pack()

lb= ttk.Treeview(root, columns=['number', 'text'], show="headings", height =20)
lb.tag_configure('odd', background='green')
lb.tag_configure('even', background='lightgreen')

lb.column("number", anchor="center", width=10)
lb.insert('', tk.END, values = ["1","testtext1"], tags=('odd',))
lb.insert('', tk.END, values = ["2","testtext2"], tags=('even',))
lb.insert('', tk.END, values = ["3","testtext3"], tags=('odd',))
lb.insert('', tk.END, values = ["4","testtext4"], tags=('even',))

lb.pack()

root.mainloop()