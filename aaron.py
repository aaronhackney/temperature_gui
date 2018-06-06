#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk


class ConvertTemp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.celsius = None
        self.fahrenheit = None
        self.window = None          # Main content Frame
        self.f_entry = None
        self.c_entry = None

    def _init_variables(self):
        self.fahrenheit = tk.DoubleVar()
        self.fahrenheit.set(32)
        self.celsius = tk.DoubleVar()
        self.f_to_c()

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
        self.tk_root.title("Temperature Conversion")
        self._init_variables()
        self.window = ttk.Frame(self.tk_root, padding="12 12 12 12")                 # window setup
        self.window.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))   # Define the grid
        self.window.columnconfigure(0, weight=1)                             # adjust window size
        self.window.rowconfigure(0, weight=1)                                # automatically
        self._add_widgets()

    def _add_widgets(self):
        # Add entry fields and associated labels

        vcmd = (self.register(self.onValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        ttk.Label(self.window, text="Temperature in degrees Fahrenheit").grid(row=1, column=1, sticky=(tk.W, tk.E))
        self.f_entry = ttk.Entry(self.window, width=5, textvariable=self.fahrenheit, validatecommand=vcmd).grid(row=1, column=2)
        ttk.Label(self.window, text="Temperature in degrees Celsius").grid(row=2, column=1, sticky=(tk.W, tk.E))
        self.c_entry = ttk.Entry(self.window, width=5, textvariable=self.celsius).grid(row=2, column=2)

        # Add buttons and wire them to functions
        ttk.Button(self.window, text="Convert Fº to Cº", command=lambda: self.f_to_c()).grid(row=3, column=1, columnspan=1)
        ttk.Button(self.window, text="Convert Cº to Fº", command=lambda: self.c_to_f()).grid(row=3, column=2, columnspan=1)

    def onValidate(self, d, i, P, s, S, v, V, W):
        print()
        pass

def main():
    convert_temp = ConvertTemp()
    convert_temp.build_gui_frame()
    convert_temp.tk_root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()

    # w = Frame ( root, option, ... )
    # root − This represents the parent window.
    # options − Here is the list of most commonly used options for this widget.
    # These options can be used as key-value pairs separated by commas.

    ConvertTemp(root).pack(fill="both", expand=True)

    root.mainloop()