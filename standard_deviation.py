import statistics
import math

def calculate_standard_deviation(entry, result_label, calculation_label):
    # Get user input
    values = entry.get().split(',')

    # Convert input values to floats
    values = [float(val.strip()) for val in values]

    # Calculate the mean
    mean = statistics.mean(values)

    # Calculate the squared differences from the mean
    squared_diffs = [(val - mean) ** 2 for val in values]

    # Calculate the variance
    variance = sum(squared_diffs) / (len(values) - 1)

    # Calculate the standard deviation
    standard_deviation = math.sqrt(variance)

    # Prepare the calculation explanation
    calculation_explanation = "Calculation Explanation:\n\n"
    calculation_explanation += f"1. Mean Calculation:\n"
    calculation_explanation += f"   - Sum of values: {sum(values)}\n"
    calculation_explanation += f"   - Number of values: {len(values)}\n"
    calculation_explanation += f"   - Mean = Sum of values / Number of values\n"
    calculation_explanation += f"   - Mean = {sum(values)} / {len(values)}\n"
    calculation_explanation += f"   - Mean = {mean:.2f}\n\n"

    calculation_explanation += f"2. Squared Differences Calculation:\n"
    calculation_explanation += f"   - Squared Difference = (Value - Mean) ^ 2\n"
    for i, val in enumerate(values):
        calculation_explanation += f"   - Squared Difference {i + 1} = ({val:.2f} - {mean:.2f}) ^ 2 = {((val - mean) ** 2):.2f}\n"
    calculation_explanation += f"\n"

    calculation_explanation += f"3. Variance Calculation:\n"
    calculation_explanation += f"   - Variance = Sum of Squared Differences / (Number of values - 1)\n"
    calculation_explanation += f"   - Variance = {sum(squared_diffs):.2f} / ({len(values)} - 1)\n"
    calculation_explanation += f"   - Variance = {variance:.2f}\n\n"

    calculation_explanation += f"4. Standard Deviation Calculation:\n"
    calculation_explanation += f"   - Standard Deviation = Square Root of Variance\n"
    calculation_explanation += f"   - Standard Deviation = Square Root of {variance:.2f}\n"
    calculation_explanation += f"   - Standard Deviation = {standard_deviation:.2f}\n"

    # Display the result
    result_label.configure(text=f"Standard Deviation: {standard_deviation:.2f}")
    calculation_label.configure(text=calculation_explanation)