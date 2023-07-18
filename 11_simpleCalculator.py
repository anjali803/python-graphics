import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid operation"

        label_result.config(text="Result: " + str(result))

    except ValueError:
        label_result.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields for numbers and operation
label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_operation = tk.Label(window, text="Operation (+, -, *, /):")
label_operation.pack()
entry_operation = tk.Entry(window)
entry_operation.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create a button to calculate the result
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

# Create a label to display the result
label_result = tk.Label(window)
label_result.pack()

# Start the main event loop
window.mainloop()
