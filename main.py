import statistics
from collections import Counter
from tkinter import *
from tkinter import ttk

def calculate_statistics():
    data = [int(i) for i in entry.get().split(',')]
    mean = statistics.mean(data)
    median = statistics.median(data)
    count = Counter(data)
    mode = [k for k, v in count.items() if v == max(list(count.values()))]
    if len(mode) == len(data):
        mode = "None"
    elif len(mode) > 1:
        mode = "Multiple modes found: " + " ".join(map(str, mode))
    else:
        mode = mode[0]
        
    mean_label.config(text=f"Mean: {mean}")
    median_label.config(text=f"Median: {median}")
    mode_label.config(text=f"Mode: {mode}")

root = Tk()
root.title("sigma-solver v1.2")
root.geometry("820x820")

root.configure(bg="#2b2b2b")
root.option_add("*Font", "TkDefaultFont 11")
root.option_add("*Background", "#2b2b2b")
root.option_add("*Foreground", "white")
root.option_add("*Button.Background", "#4c4c4c")
root.option_add("*Button.Foreground", "white")
root.option_add("*Button.activeBackground", "#3d3d3d")
root.option_add("*Entry.Background", "#4c4c4c")
root.option_add("*Entry.Foreground", "white")
root.option_add("*Label.Background", "#2b2b2b")
root.option_add("*Label.Foreground", "white")

style = ttk.Style()
style.theme_use("clam")

instructions = Label(root, text="Enter a list of numbers separated by commas:")
instructions.pack()

entry = Entry(root)
entry.pack()

style.configure("discord.TButton", background="#7289da", foreground="white")

calculate_button = ttk.Button(root, text="Calculate Statistics", style="discord.TButton", command=calculate_statistics)
calculate_button.pack()



mean_label = Label(root, text="")
mean_label.pack()

median_label = Label(root, text="")
median_label.pack()

mode_label = Label(root, text="")
mode_label.pack()

thanks1 = Label(root, text="Big thanks : 4orage")
thanks1.pack()
thanks2 = Label(root, text="Thank you so much for pointing out the 'mode' mistake")
thanks2.pack()

root.mainloop()