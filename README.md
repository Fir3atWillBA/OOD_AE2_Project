# OOD_AE2 Project: Simple tkinter Calculator GUI

<img width="487" alt="Screenshot 2023-04-02 at 7 17 46 PM" src="https://user-images.githubusercontent.com/122615154/229371315-99a51e04-d44b-4cd7-8535-c9de921d4d54.png">

## Introduction:

The purpose of this project is to develop a basic calculator using object-oriented programming principles in Python. The calculator will make use of a Graphical User Interface (GUI) created with tkinter, and be able to perform standard arithmetic tasks such as the standard real number field operations (viz. "+", "-", etc.), taking a base to a specified exponent, and calculating square roots.

### Instructions

Use of the calculator is self-explanatory; use any binary operation button (e.g., "+") between desired real numbers and press the equals button to produce the result of the desired calculation, as you would with any normal calculator.

## Design Brief:

The project follows the *Waterfall* Systems Development Life Cycle, a linear approach to software development that completes important components in successive stages. As will be evident upon examining the code, the object-oriented design is modeled after a Model-View-Control architecture. 

The Calculator class can be considered as the "Model" which handles the logic and state of the calculator. The create_display_labels, create_display_frame, create_digit_buttons, create_operator_buttons, create_special_buttons, and create_buttons_frame methods are responsible for creating the "View" of the calculator, that is, the graphical user interface (GUI) elements.

The add_to_expression, append_operator, clear, power, sqrt, evaluate, and update_label methods act as the "Controller" of the calculator, which handle the interaction between the Model and the View, such as updating the state of the calculator when buttons are pressed or when the user inputs a mathematical expression.

The logic and state of the application are separated from the GUI elements and the interaction between them is handled by the controller methods.

## Implementation:

The project proceeded by use of GitHub and VS Code. The use of such version control programs is advantageous because it allows for the tracking of changes, which are useful for debugging, updating the project, and helping pinpoint at which stage faulty code may have entered the system. 

### Prerequisites:

To run the program, you need to have Python 3.6 and Tkinter installed on your system. Click [here](https://www.python.org/downloads/).

### Download the Project Files

1. Clone the repository or download the ZIP file of the project from GitHub.
2. Extract the files to a folder of your choice.

### Run the Calculator App

1. Open a terminal (Command Prompt or PowerShell on Windows, Terminal on macOS or Linux).
2. Navigate to the folder where the project files are located using the cd command.
3. Run the calculator app by executing the following command: 

python calculator_code.py

## Testing:

For this calculator app, it makes sense to implement unit testing to ensure that the basic functionality of the calculator is working as expected. This includes testing that the calculator runs without crashing with a smoke test and testing that buttons perform as they are supposed to, without errors.

To run the tests, open a new terminal session and run:

python -m unittest unit_tests.py

or simply,

python unit_tests.py

## Evaluation:

This calculator project successfully implements a simple graphical user interface using the tkinter library in Python. The calculator performs basic arithmetic operations (addition, subtraction, multiplication, and division), along with special functions like raising to power and square root. The code is *modular* and easy to read. The use of object-oriented programming and design patterns makes the code flexible and extendable.

The calculator has been tested with unit tests, and it has passed all tests provided. However, there are a number of complex test scenarios that can be added to ensure the reliability and accuracy of the calculations.

There are numerous opportunities for improvement. One area for improvement could be the addition of error handling for invalid inputs, such as dividing by zero (which I have accounted for in the calculator_code.py file) or entering invalid characters. Additionally, the interface could be made more visually appealing and user-friendly with the addition of more graphics and design elements. The colors of the calculator were chosen purposefully to be reminiscent of schoolhouse chalkboard colors, with white chalk for the characters used.

In the end, this calculator project is a good example of how to implement a graphical user interface using the tkinter library in Python, and can serve as a starting point for further development and customization. As an object-oriented project, it will lend itself to future additions of complex mathematical operations, such as trigonometric functions. In the future, more advanced features will be added; being able to handle multiple calculations simultaneously that follow the standard order of operations and parentheses and brackets are next on the to-do list.

## User evaluation:

"I felt like I was using a calculator that looked like a chalkboard! It was very user-friendly. I just wish that the calculator was able to carry out multiple operations simultaneously, while adhering to the order of operations. Also, I wish it had parentheses and maybe other operations. It also felt like the square root button was superfluous because you can use decimals with the power function, so you can calculate the square root by simply raising a number to the power of 0.5. But in spite of all that, solid job!"

 - Anonymous user.

