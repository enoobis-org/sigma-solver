import statistics

def calculate_mean(entry, result_label, calculation_label):
    # Get user input
    values = entry.get().split(',')

    # Convert input values to floats
    values = [float(val.strip()) for val in values]

    # Calculate the mean
    mean = statistics.mean(values)

    # Prepare the calculation explanation
    calculation_explanation = "Calculation Explanation:\n\n"
    calculation_explanation += f"1. Mean Calculation:\n"
    calculation_explanation += f"   - Sum of values: {sum(values)}\n"
    calculation_explanation += f"   - Number of values: {len(values)}\n"
    calculation_explanation += f"   - Mean = Sum of values / Number of values\n"
    calculation_explanation += f"   - Mean = {sum(values)} / {len(values)}\n"
    calculation_explanation += f"   - Mean = {mean:.2f}\n"

    # Display the result
    result_label.configure(text=f"Mean: {mean:.2f}")
    calculation_label.configure(text=calculation_explanation)