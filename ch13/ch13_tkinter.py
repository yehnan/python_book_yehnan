

from tkinter import *

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        
        self.entry_n = Entry(self, width=10)
        self.entry_n.pack()

        self.fn = StringVar()
        self.label_fn = Label(self, textvariable=self.fn, 
                              width=50)
        self.fn.set('result')
        self.label_fn.pack()
        
        self.btn_cal = Button(self, text="Calculate", 
                              command=self.cal_fib)
        self.btn_cal.pack()

        self.btn_quit = Button(self, text="Quit", fg="red",
                              command=root.destroy)
        self.btn_quit.pack(side=BOTTOM)
        
    def cal_fib(self):
        try:
            n = int(self.entry_n.get())
            self.fn.set(str(fib(n)))
        except Exception:
            self.fn.set('Invalid input')
        
root = Tk()
app = App(root)
app.mainloop()








