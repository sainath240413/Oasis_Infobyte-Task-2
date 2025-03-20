def calculate_bmi(weight, height):
    """Calculate BMI based on weight (kg) and height (m)."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# User input
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
    else:
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        # Display result
        print(f"\nYour BMI: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Invalid input. Please enter numeric values for weight and height.")
