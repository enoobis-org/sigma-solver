import statistics
from tkinter import *

def calculate_statistics():
    data = [int(i) for i in entry.get().split(',')]
    mean = statistics.mean(data)
    median = statistics.median(data)
    try:
        mode = statistics.mode(data)
    except:
        mode = "No unique mode found"
        
    mean_label.config(text=f"Mean: {mean}")
    median_label.config(text=f"Median: {median}")
    mode_label.config(text=f"Mode: {mode}")

root = Tk()
root.title("sigma-solver")
root.geometry("400x400")

instructions = Label(root, text="Enter a list of numbers separated by commas:")
instructions.pack()

entry = Entry(root)
entry.pack()

calculate_button = Button(root, text="Calculate Statistics", command=calculate_statistics)
calculate_button.pack()

mean_label = Label(root, text="")
mean_label.pack()

median_label = Label(root, text="")
median_label.pack()

mode_label = Label(root, text="")
mode_label.pack()

root.mainloop()