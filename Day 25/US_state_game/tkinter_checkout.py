import tkinter as tk
res = tk.Tk()
res.title('Incrementing the Process')
button = tk.Button(res, text='Pause', width=30, command=res.destroy)
button.pack()
res.mainloop()