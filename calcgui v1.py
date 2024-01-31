import math
import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [sg.Text("Welcome to oprifine's calculator! Some answers will be estimated, be careful!")],
    [sg.Text("What math operation would you like to use?"), sg.InputCombo(['+','-','/','*','**','//','π','√','log','%','θ'], key='mathop')],
    [sg.Text("What's your first number?"), sg.Input(key='num1')],
    [sg.Text("What's your second number?"), sg.Input(key='num2')],
    [sg.Button('Solve'), sg.Button('Exit App')],
    [sg.Text("The result of this would be:"), sg.Text(size=(15,1), key='result')]
]

# Create the window object
window = sg.Window("oprifine's school python calculator", layout)

# Create the event loop
while True:
    event, values = window.read()  # Read the events and values of the GUI elements
    if event == sg.WINDOW_CLOSED or event == 'Exit App':  # If the user closes the window or clicks Exit, break the loop
        break
    elif event == 'Solve':  # If the user clicks Solve, perform the math operation
        mathop = values['mathop']  # Get the math operation from the input combo
        try:
            num1 = float(values['num1'])  # Get the first number from the input field and convert it to float
            num2 = float(values['num2'])  # Get the second number from the input field and convert it to float
        except ValueError:  # If the input is not a valid number, show an error message and continue the loop
            window['result'].update('Your answer')
            window['result'].update('Invalid input. Please enter valid numbers.')
            continue
        if mathop == '+':
            result = num1 + num2
        elif mathop == '-':
            result = num1 - num2
        elif mathop == '{\displaystyle \div }':
            result = num1 / num2
        elif mathop == '*':
            result = num1 * num2
        elif mathop == '**':
            result = num1 ** num2
        elif mathop == '//':
            result = num1 // num2
        elif mathop == 'π':
            result = 3.141592653589793
        elif mathop == '√':
            result = math.sqrt(num1)
        elif mathop == 'log':
            result = math.log(num1 + num2)
        elif mathop == '%':
            result = int(num1) % int(num2)
        elif mathop == 'θ':
            result = math.sin(num1+num2)
        elif mathop == 'cos':
            result = math.cos(num1+num2)
        window['result'].update(f"{result:.2f}")  # Update the result text with the formatted calculated value

# Close the window
window.close()