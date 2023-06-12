import statistics

def calculate_median(entry, result_label, calculation_label):
    # Get user input
    values = entry.get().split(',')

    # Convert input values to floats
    values = [float(val.strip()) for val in values]

    # Sort the values
    sorted_values = sorted(values)

    # Calculate the median
    n = len(sorted_values)
    if n % 2 == 0:
        # If the number of values is even
        middle_value_1 = sorted_values[n // 2 - 1]
        middle_value_2 = sorted_values[n // 2]
        median = (middle_value_1 + middle_value_2) / 2
        median_formula = f"Median = ({middle_value_1} + {middle_value_2}) / 2"
    else:
        # If the number of values is odd
        middle_value = sorted_values[n // 2]
        median = middle_value
        median_formula = f"Median = {middle_value}"

    # Prepare the calculation explanation
    calculation_explanation = "Calculation Explanation:\n\n"
    calculation_explanation += f"1. Median Calculation:\n"
    calculation_explanation += f"   - Sorted Values: {sorted_values}\n"
    calculation_explanation += f"   - Number of values: {n}\n"
    calculation_explanation += f"   - Median = "
    calculation_explanation += median_formula + "\n"

    # Display the result
    result_label.configure(text=f"Median: {median:.2f}")
    calculation_label.configure(text=calculation_explanation)