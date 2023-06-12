import statistics

def calculate_mode(entry, result_label, calculation_label):
    # Get user input
    values = entry.get().split(',')

    # Convert input values to floats
    values = [float(val.strip()) for val in values]

    # Calculate the mode
    try:
        mode = statistics.mode(values)
        mode_count = values.count(mode)

        calculation_explanation = "Calculation Explanation:\n\n"
        calculation_explanation += f"1. Mode Calculation:\n"
        calculation_explanation += f"   - Values: {values}\n"
        calculation_explanation += f"   - Mode: {mode}\n"
        calculation_explanation += f"   - Frequency: {mode_count}\n"
    except statistics.StatisticsError:
        mode = None
        calculation_explanation = "Calculation Explanation:\n\n"
        calculation_explanation += "There is no mode. All values are unique."

    # Display the result
    if mode is not None and mode_count > 1:
        result_label.configure(text=f"Mode: {mode}")
    else:
        result_label.configure(text="No mode found")
    calculation_label.configure(text=calculation_explanation)