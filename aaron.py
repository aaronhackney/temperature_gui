import tkinter as tk
from tkinter import ttk


def f_to_c(*args):
    try:
        celsius.set(round((fahrenheit.get() - 32) * .5556, 1))
    except ValueError:
        print("ERROR")
        pass


def c_to_f(*args):
    try:
        fahrenheit.set((celsius.get() * 1.8) + 32)
        pass
    except ValueError:
        print("ERROR")
        pass


def clear_on_click(*args):
    pass


root = tk.Tk()
root.title(" Fahrenheit <--> Celsius")                  # window title

fahrenheit = tk.DoubleVar()                                     # Can't define until tk.Tk() is instantiated
fahrenheit.set(32)                                              # Set default value to 32.0 degrees

celsius = tk.DoubleVar()

window = ttk.Frame(root, padding="12 12 12 12")                 # window setup
window.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))   # Define the grid
window.columnconfigure(0, weight=1)                             # adjust window size
window.rowconfigure(0, weight=1)                                # automatically

ttk.Label(window, text="Temperature in degrees Fahrenheit").grid(row=1, column=1, sticky=(tk.W, tk.E))
f_input = ttk.Entry(window, width=5,textvariable=fahrenheit).grid(row=1, column=2)    # fahrenheit input & display data

ttk.Label(window, text="Temperature in degrees Celsius").grid(row=2, column=1, sticky=(tk.W, tk.E))
c_input = ttk.Entry(window, width=5,textvariable=celsius).grid(row=2, column=2)    # celsius input & display data

# test
ttk.Button(window, text="Convert", command=f_to_c).grid(row=3, column=1, columnspan=2) # ttk Button widget calls f_to_c function

root.mainloop()                                                 # Run the GUI with real time event processing



