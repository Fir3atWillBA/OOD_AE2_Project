# OOD_AE2 Project

## Introduction:

The purpose of this project is to develop a basic calculator using object-oriented programming principles in Python. The calculator will make use of a Graphical User Interface (GUI) created with tkinter, and be able to perform standard arithmetic tasks such as the standard real number field operations (viz. "+", "-", "*", and "/"), taking a base to a specified exponent, and calculating square roots.

## Design Brief:
The project follows the Waterfall Systems Development Life Cycle, a linear approach to software development that completes important components in successive stages. As will be evident upon examining the code, the object-oriented design is modeled after a Model-View-Control architecture. 

The Calculator class can be considered as the "Model" which handles the logic and state of the calculator. The create_display_labels, create_display_frame, create_digit_buttons, create_operator_buttons, create_special_buttons, and create_buttons_frame methods are responsible for creating the "View" of the calculator, i.e., the graphical user interface (GUI) elements.
The add_to_expression, append_operator, clear, square, sqrt, evaluate, and update_label methods act as the "Controller" of the calculator, which handle the interaction between the Model and the View, such as updating the state of the calculator when buttons are pressed or when the user inputs a mathematical expression.

The logic and state of the application are separated from the GUI elements and the interaction between them is handled by the controller methods.

## Implementation:

The project proceeded by use of GitHub and VS Code. The use of version control program is advantageous because it allows for the tracking of changes, which are useful for debugging and updating the project. 

To run the program, you need to have Python 3.x and Tkinter installed on your system. 

## Testing:

For this calculator app, it makes sense to implement unit testing to ensure that the basic functionality of the calculator is working as expected. This includes testing the basic arithmetic operations (addition, subtraction, multiplication, division) and also testing more complex operations such as exponents, square roots, and order of operations.

## Evaluation:

This calculator project successfully implements a simple graphical user interface using the tkinter library in Python. The calculator performs basic arithmetic operations (addition, subtraction, multiplication, and division), along with special functions like square and square root.
The code is modular and easy to read. The use of object-oriented programming and design patterns makes the code flexible and extendable.

The calculator has been tested with unit tests, and there are a number of complex test scenarios that can be added to ensure the reliability and accuracy of the calculations.
One area for improvement could be the addition of error handling for invalid inputs, such as dividing by zero or entering invalid characters. Additionally, the interface could be made more visually appealing and user-friendly with the addition of more graphics and design elements.
Overall, this calculator project is a good example of how to implement a graphical user interface using the tkinter library in Python, and can serve as a starting point for further development and customization. As an object-oriented project, it will lend itself to future additions of complex mathematical operations, such as trigonometric functions.

## Deployment:


