import tkinter as tk
import tkinter.ttk as ttk
import statistics
import customtkinter

from standard_deviation import *
from mode import *
from median import *
from mean import *
from variance import *


# Theme for Tkinter
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Create the main window
window = customtkinter.CTk()
window.title("SIGMA SOLVER")
window.configure(bg="white")

# Make the window non-resizable
window.resizable(False, False)

# Set the window icon
window.iconbitmap("C:\\Users\\enoobis\\Desktop\\project\\icon\\icon.ico")

# Create the Notebook widget
notebook = ttk.Notebook(window, width=900, height=500)
notebook.pack(pady=10)

# Create a style for the Notebook widget
style = ttk.Style()
style.configure("Custom.TNotebook", background="white")
notebook.configure(style="Custom.TNotebook")

# Create a frame for the first tab
tab1_frame = customtkinter.CTkFrame(notebook)
notebook.add(tab1_frame, text="Descriptive Statistics")


# Function to calculate the standard deviation
def calculate_standard_deviation_command():
    calculate_standard_deviation(entry, result_label, calculation_label)

def calculate_mode_command():
    calculate_mode(entry, result_label, calculation_label)

def calculate_median_command():
    calculate_median(entry, result_label, calculation_label)

def calculate_mean_command():
    calculate_mean(entry, result_label, calculation_label)

def calculate_variance_command():
    calculate_variance(entry, result_label, calculation_label)


# Create the input label
input_label = customtkinter.CTkLabel(tab1_frame, text="Enter values (comma-separated):")
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Create the entry field
entry = customtkinter.CTkEntry(tab1_frame, width=150)
entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

# Create the mode button
mode_button = customtkinter.CTkButton(tab1_frame, text="Mode", command=calculate_mode_command)
mode_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create the median button
median_button = customtkinter.CTkButton(tab1_frame, text="Median", command=calculate_median_command)
median_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Create the mean button
mean_button = customtkinter.CTkButton(tab1_frame, text="Mean", command=calculate_mean_command)
mean_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# Create the variance button
variance_button = customtkinter.CTkButton(tab1_frame, text="Variance", command=calculate_variance_command)
variance_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

# Create the standard deviation button
std_deviation_button = customtkinter.CTkButton(tab1_frame, text="Standard Deviation",
                                               command=calculate_standard_deviation_command)
std_deviation_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")

######################################
# Create a frame for the result and calculation labels
result_frame = tk.Frame(tab1_frame, bg="white")
result_frame.place(relx=0.3, rely=0.00, relwidth=0.65, relheight=1)

# Create the result label
result_label = tk.Label(result_frame, text="", bg="white")
result_label.pack()

# Create the calculation label
calculation_label = tk.Label(result_frame, text="", bg="white")
calculation_label.pack()
######################################


# Start the main event loop
window.mainloop()





