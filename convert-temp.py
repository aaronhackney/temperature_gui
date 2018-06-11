#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk


class ConvertTemp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.celsius = tk.DoubleVar()
        self.celsius.set(0.0)
        self.fahrenheit = tk.DoubleVar()
        self.fahrenheit.set(32.0)
        self.window = None          # Main content Frame
        self.f_entry = None
        self.f_btn = None
        self.c_entry = None
        self.c_btn = None
        self.selection = tk.StringVar()
        #self.build_gui_frame()
        self._add_widgets()

    def f_to_c(self):
        try:
            self.celsius.set(round((self.fahrenheit.get() - 32) * .5556, 1))
        except ValueError:
            print("ERROR")

    def c_to_f(self):
        try:
            self.fahrenheit.set((self.celsius.get() * 1.8) + 32)
        except ValueError:
            print("ERROR")

    def build_gui_frame(self):
        # self.tk_root.title("Temperature Conversion")
        # self._init_variables()
        # self.window = ttk.Frame(self.tk_root, padding="12 12 12 12")                 # window setup
        self.window.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))   # Define the grid
        self.window.columnconfigure(0, weight=1)                             # adjust window size
        self.window.rowconfigure(0, weight=1)                                # automatically
        self._add_widgets()

    def clear_widget(self, event):
        event.widget.delete(0, tk.END)

    def radio_select(self):
        print(self.selection.get())
        if self.selection.get() == "1":
            self.c_btn.grid_remove()
            self.f_btn.grid()
            self.f_entry['state'] = tk.NORMAL
            self.c_entry['state'] = tk.DISABLED
            self.celsius.set("0.0")
            self.fahrenheit.set("32.0")
            self.f_to_c()
        elif self.selection.get() == "2":
            self.c_btn.grid()
            self.f_btn.grid_remove()
            self.f_entry['state'] = tk.DISABLED
            self.c_entry['state'] = tk.NORMAL
            self.fahrenheit.set("32.0")
            self.celsius.set("0.0")
            self.c_to_f()

    def _add_widgets(self):
        # This point to the input validation method
        vcmd = (self.register(self.onValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.radio1 = ttk.Radiobutton(root, text="F\xb0 to C\xb0", variable=self.selection, value=1, command=self.radio_select)
        self.radio1.grid(row=0, column=0)
        self.radio2 = ttk.Radiobutton(root, text="C\xb0 to F\xb0", variable=self.selection, value=2, command=self.radio_select)
        self.radio2.grid(row=1, column=0)

        # Create the input fields and wire the associated events
        ttk.Label(self.window, text="Fahrenheit\xb0").grid(row=0, column=1, sticky=tk.E, padx=5)
        self.f_entry = ttk.Entry(self.window, width=5, validate="all", textvariable=self.fahrenheit, validatecommand=vcmd)
        self.f_entry.bind("<FocusIn>", self.clear_widget)
        self.f_entry.grid(row=0, column=2, sticky=tk.W)

        ttk.Label(self.window, text="Celsius\xb0").grid(row=1, column=1, sticky=tk.E, padx=5)
        self.c_entry = ttk.Entry(self.window, width=5, textvariable=self.celsius)
        self.c_entry.bind("<FocusIn>", self.clear_widget)
        self.c_entry.grid(row=1, column=2, sticky=tk.W)

        # Add buttons and wire them to functions
        self.f_btn = tk.Button(self.window, text="Convert Fº to Cº", command=lambda: self.f_to_c())
        self.f_btn.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

        self.c_btn = tk.Button(self.window, text="Convert Cº to Fº", command=lambda: self.c_to_f())
        self.c_btn.grid(row=2, column=0, columnspan=3, sticky=tk.W + tk.E)

        # Select F-->C First!
        self.selection.set(1)
        self.radio_select()

    def onValidate(self, d, i, P, s, S, v, V, W):
        if self._is_number(S):
            return True
        else:
            self.bell()
            return False

    def _is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    root = tk.Tk()
    elements = ConvertTemp(root)
    root.mainloop()