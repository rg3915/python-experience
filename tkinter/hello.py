from Tkinter import *
import tkMessageBox


class MyApp:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.btn = Button(self.frame, text='OK')
        self.btn['command'] = self.my_function
        self.btn['width'] = '20'
        self.btn['height'] = '10'
        self.btn.pack()

    def my_function(self):
        tkMessageBox.showinfo('Python', 'Bem-vindo!')

tk = Tk()
MyApp(tk)
tk.mainloop()
