import streamlit as st

# Define calculator functions
def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return None  # Use None to indicate an error

def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    return num1 - num2

# Streamlit app
def main():
    st.title("Hammad Amjad's Calculator")

    # Create a selectbox for the operation
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Get user input
    num1 = st.number_input("Enter first number", format="%.2f")
    num2 = st.number_input("Enter second number", format="%.2f")

    # Display the result based on the selected operation
    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
            if result is None:
                result = "Error: Division by zero"
        else:
            result = "Invalid operation"

        # Show result
        st.write(f"Result: {result}")

# Execute the app
if __name__ == "__main__":
    main()
