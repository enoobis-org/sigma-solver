import statistics
from collections import Counter
from tkinter import *
from tkinter import ttk

# Set dark mode colors
BG_COLOR = "#24292e"
FG_COLOR = "#f0f6fc"
ENTRY_BG_COLOR = "#1e2227"
ENTRY_FG_COLOR = "#c9d1d9"
BUTTON_BG_COLOR = "#2ea44f"
BUTTON_FG_COLOR = "#f0f6fc"
LABEL_BG_COLOR = "#1e2227"
LABEL_FG_COLOR = "#c9d1d9"

def calculate_statistics():
    data_str = entry.get().strip()
    if not data_str:
        mean_label.config(text="Please enter at least one number")
        median_label.config(text="")
        mode_label.config(text="")
        return
    
    # Convert input string to list of integers
    data = [int(i) for i in data_str.split(',')]
    n = len(data)
    
    # Calculate mean
    mean = sum(data) / n
    mean_process = f"Mean = (Sum of all numbers) / (Number of numbers) = ({' + '.join(map(str, data))}) / {n} = {mean}"
    
    # Calculate median
    data_sorted = sorted(data)
    if n % 2 == 0:
        median = (data_sorted[n//2-1] + data_sorted[n//2]) / 2
    else:
        median = data_sorted[n//2]
    median_process = "Median = "
    if n % 2 == 0:
        median_process += f"({data_sorted[n//2-1]} + {data_sorted[n//2]}) / 2 = {median}"
    else:
        median_process += f"{data_sorted[n//2]}"

    # Calculate mode
    count = Counter(data)
    mode_count = max(count.values())
    mode = [k for k, v in count.items() if v == mode_count]
    if len(mode) == len(data) or len(mode) == 0:
        mode = []
    elif len(mode) > 1:
        mode = "Multiple modes found: " + " ".join(map(str, mode))
    else:
        mode = mode[0]
    mode_process = "Mode = "
    if len(mode) == 0:
        mode_process += "No mode found"
    elif isinstance(mode, str):
        mode_process += mode
    else:
        mode_process += f"{mode[0]}"
        
    # Update output labels with results and process
    mean_label.config(text=f"Mean: {mean}\n\n{mean_process}", fg=FG_COLOR, bg=LABEL_BG_COLOR)
    median_label.config(text=f"Median: {median}\n\n{median_process}", fg=FG_COLOR, bg=LABEL_BG_COLOR)
    mode_label.config(text=f"Mode: {mode}\n\n{mode_process}", fg=FG_COLOR, bg=LABEL_BG_COLOR)
root = Tk()
root.title("sigma-solver v1.2")
root.geometry("820x820")
root.configure(background=BG_COLOR)

# Create a Notebook widget with three tabs
notebook = ttk.Notebook(root, width=800, height=800, padding=(30, 10, 30, 10), style="dark.TNotebook")
notebook.pack(fill=BOTH, expand=True)

mean_tab = ttk.Frame(notebook, style="dark.TFrame")
median_tab = ttk.Frame(notebook, style="dark.TFrame")
mode_tab = ttk.Frame(notebook, style="dark.TFrame")

notebook.add(mean_tab, text="Mean")
notebook.add(median_tab, text="Median")
notebook.add(mode_tab, text="Mode")

# Add input and calculate button to each tab
for tab in [mean_tab, median_tab, mode_tab]:
    instructions = Label(tab, text="Enter a list of numbers separated by commas:", fg=FG_COLOR, bg=BG_COLOR)
    instructions.pack()

    entry = Entry(tab, bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR)
    entry.pack()

    calculate_button = ttk.Button(tab, text="Calculate Statistics", command=calculate_statistics, style="dark.TButton", cursor="hand2")
    calculate_button.pack()

# Add output labels to each tab
mean_label = Label(mean_tab, text="", fg=FG_COLOR, bg=LABEL_BG_COLOR)
mean_label.pack()

median_label = Label(median_tab, text="", fg=FG_COLOR, bg=LABEL_BG_COLOR)
median_label.pack()

mode_label = Label(mode_tab, text="", fg=FG_COLOR, bg=LABEL_BG_COLOR)
mode_label.pack()

ampt = Label(root, text="")
ampt.pack()

# Define dark mode styles
style = ttk.Style()
style.theme_use("clam")
style.configure("dark.TNotebook", background=BG_COLOR)
style.configure("dark.TFrame", background=BG_COLOR)
style.configure("dark.TButton", background=BUTTON_BG_COLOR, foreground=BUTTON_FG_COLOR, bordercolor=BG_COLOR, focuscolor=BG_COLOR, lightcolor=BG_COLOR, padding=5)
style.map("dark.TButton", background=[("active", "#238636")])

# Set label colors
style.configure("dark.TLabel", foreground=FG_COLOR, background=LABEL_BG_COLOR)

# Set entry colors
style.map("TEntry", background=[("disabled", BG_COLOR), ("active", ENTRY_BG_COLOR)])
style.configure("TEntry", fieldbackground=ENTRY_BG_COLOR, foreground=ENTRY_FG_COLOR, bordercolor=BG_COLOR, selectbackground=FG_COLOR, selectforeground=ENTRY_BG_COLOR)

root.mainloop()