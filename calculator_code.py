# Importing the tkinter module
import tkinter as tk

# Defining global constants for fonts and colors used in the calculator GUI

LARGE_FONT_STYLE = ("Comic Sans MS", 40, "bold")
SMALL_FONT_STYLE = ("Comic Sans MS", 16)
DIGITS_FONT_STYLE = ("Comic Sans MS", 24, "bold")
DEFAULT_FONT_STYLE = ("Comic Sans MS", 20)
WHITE = "#FFFFFF"
BLACK = "#000000"
DARK_GREEN = "#006400"
LABEL_COLOR = WHITE


# Defining a Calculator class with all the necessary methods to create and run a calculator GUI
class Calculator:

    def __init__(self):
        # Creating a new Tkinter window instance
        self.window = tk.Tk()

        # Configuring window size, resizability, and title
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        # Initializing instance variables for calculator expressions and display frame
        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        # Creating and packing display labels for total and current expressions
        self.total_label, self.label = self.create_display_labels()

        # Defining a dictionary of digits and their respective locations on the calculator GUI
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        # Defining a dictionary of mathematical operations and their corresponding symbols
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        # Creating and packing buttons frame for the calculator GUI
        self.buttons_frame = self.create_buttons_frame()

        # Configuring button frame rows and columns to expand with window
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        # Creating digit buttons and packing them onto the buttons frame
        self.create_digit_buttons()

        # Creating operator buttons and packing them onto the buttons frame
        self.create_operator_buttons()

        # Creating special buttons and packing them onto the buttons frame
        self.create_special_buttons()

        # Binding keys to the calculator GUI
        self.bind_keys()


        self.waiting_for_power_input = False



    def bind_keys(self):
        """Binds keys to methods of the calculator object.

        Binds the Enter key to evaluate() method, digit keys to add_to_expression() method,
        and operator keys to append_operator() method.
        """
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        """Creates and displays special buttons on the calculator interface.

        This method creates four special buttons, including the clear, equals, square, and square root buttons, and displays them on the calculator interface.
        """
        self.create_clear_button()
        self.create_equals_button()
        self.create_raise_to_power_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        """Creates and displays labels on the calculator interface.

        This method creates two labels on the calculator interface, including the total expression label and the current expression label. It sets the text, anchor, background, foreground, padding, font size, and fill properties of each label, and displays them on the calculator interface.

        Returns:
        total_label (Label): The total expression label widget.
        label (Label): The current expression label widget.
        """
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=BLACK,
                           fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=BLACK,
                     fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_display_frame(self):
        """
        Create a display frame using tkinter and return it.
    
        This method creates a tkinter Frame with the specified height and background color, then packs it
        to expand and fill both directions (vertically and horizontally). The created frame is returned.
    
        Returns:
            frame (tk.Frame): The created tkinter Frame with specified height and background color.
        """
        frame = tk.Frame(self.window, height=221, bg=BLACK)  # Create a Frame with height 221 and background color BLACK
        frame.pack(expand=True, fill="both")  # Pack the frame to expand and fill both directions
        return frame

    def add_to_expression(self, value):
        """
        Add a value to the current expression and update the label.
        
        This method appends the input value (digit, decimal point, or exponent) to the current expression,
        then updates the display label accordingly. If the calculator is waiting for power input, the total
        expression is also updated with the input value.
        """
        self.current_expression += str(value)  # Append the input value to the current expression
        if self.waiting_for_power_input:
            self.total_expression += str(value)  # Append the input value to the total expression if waiting for power input
            self.update_total_label()  # Update the total label if waiting for power input
        self.update_label()  # Update the current label

    def create_digit_buttons(self):
        """
        Create digit buttons and add them to the buttons_frame.
    
        This method iterates through the digits dictionary, creating a tkinter Button for each digit
        with specified attributes (background color, highlight background color, foreground color, font style,
        and border width). The buttons are then added to the grid layout of the buttons_frame.
        """
        # Iterate through the digits dictionary and create digit buttons
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=DARK_GREEN, highlightbackground=DARK_GREEN, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            # Add the button to the grid layout of the buttons_frame
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        """
        Append the given operator to the current expression and update labels.
    
        This method appends the given operator to the current expression, adds the current expression
        to the total expression, and resets the current expression. It then updates both the total and
        current labels to reflect the changes in the GUI.
    
        Args:
            operator (str): The operator to be appended to the current expression.
            """
        self.current_expression += operator  # Append the operator to the current expression
        self.total_expression += self.current_expression  # Add the current expression to the total expression
        self.current_expression = ""  # Reset the current expression
        self.update_total_label()  # Update the total label
        self.update_label()  # Update the current label

    def create_operator_buttons(self):
        """
        Create operator buttons and add them to the buttons_frame.
    
        This method iterates through the operations dictionary, creating a tkinter Button for each operator
        with specified attributes (background color, highlight background color, foreground color, and font style).
        The buttons are then added to the grid layout of the buttons_frame in the 4th column.
        """
        i = 0  # Initialize row index
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=DARK_GREEN, highlightbackground=DARK_GREEN, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)  # Add the button to the grid layout of the buttons_frame
            i += 1  # Increment the row index

    def clear(self):
        """
        Clear the current and total expressions, and update the labels.
    
        This method resets both the current and total expressions and updates the respective labels
        to reflect the changes in the GUI.
        """
        self.current_expression = ""  # Reset the current expression
        self.total_expression = ""  # Reset the total expression
        self.update_label()  # Update the current label
        self.update_total_label()  # Update the total label

    def create_clear_button(self):
        """
        Create a clear button and add it to the buttons_frame.
        
        This method creates a tkinter Button with specified attributes (background color, highlight background color,
                                                                        foreground color, and font style) and a command to clear the expressions when clicked. The button is then added
        to the grid layout of the buttons_frame.
        """
        button = tk.Button(self.buttons_frame, text="C", bg=DARK_GREEN, highlightbackground=DARK_GREEN, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)  # Add the clear button to the grid layout of the buttons_frame

    def raise_to_power(self):
        """
        Prepare the calculator to raise the current expression to an input power.
        
        This method sets a flag indicating that the calculator is waiting for a power input,
        stores the current expression as the base, and clears the current expression. It also
        updates the total_label with the base expression and the power symbol.
        """
        self.waiting_for_power_input = True  # Set a flag to indicate waiting for power input
        self.base_expression = self.current_expression  # Store the current expression as the base
        self.current_expression = ""  # Clear the current expression
        self.total_expression = f"{self.base_expression}^"  # Update the total expression with base and power symbol
        self.update_total_label()  # Update the total label
        self.update_label()  # Update the current label

    def create_raise_to_power_button(self):
        """
        Create a raise to power button and add it to the buttons_frame.
        
        This method creates a tkinter Button with specified attributes (background color, foreground color,
                                                                        font style, and border width), a label with a power symbol, and a command to prepare the calculator
        for raising the current expression to an input power when clicked. The button is then added to the
        grid layout of the buttons_frame.
        """
        button = tk.Button(self.buttons_frame, text="x^y", bg=DARK_GREEN, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, highlightbackground=DARK_GREEN, command=self.raise_to_power)
        button.grid(row=0, column=2, sticky=tk.NSEW)  # Add the raise to power button to the grid layout of the buttons_frame


    def sqrt(self):
        """
        Calculate the square root of the current expression and update the label.
        
        This method evaluates the square root of the current expression using the eval function,
        converts the result to a string, and updates the current expression. It then calls
        the update_label method to reflect the changes in the GUI.
        """
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))  # Calculate the square root of the current expression
        self.update_label()  # Update the current label

    def create_sqrt_button(self):
        """
        Create a square root button and add it to the buttons_frame.
        
        This method creates a tkinter Button with specified attributes (background color, foreground color,
                                                                        font style, and border width), a label with a square root symbol, and a command to calculate the square
        root of the current expression when clicked. The button is then added to the grid layout of the buttons_frame.
        """
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=DARK_GREEN, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, highlightbackground=DARK_GREEN, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)  # Add the square root button to the grid layout of the buttons_frame



    def evaluate(self):
        if self.waiting_for_power_input:
            try:
                self.current_expression = str(eval(f"{self.base_expression}**{self.current_expression}"))
                self.waiting_for_power_input = False  # Reset the waiting flag
            except Exception as e:
                self.current_expression = "Error"
        else:
            self.total_expression += self.current_expression
            self.update_total_label()
            try:
                self.current_expression = str(eval(self.total_expression))
                self.total_expression = ""
            except Exception as e:
                self.current_expression = "Error"
        self.update_label()

    def create_equals_button(self):
        """
        Create an equals button and add it to the buttons_frame.
        
        This method creates a tkinter Button with specified attributes (background color, foreground color,
                                                                        font style, and border width), a label with an equals symbol, and a command to evaluate the expression
        when clicked. The button is then added to the grid layout of the buttons_frame with a columnspan of 2.
        """
        button = tk.Button(self.buttons_frame, text="=", bg=DARK_GREEN, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, highlightbackground=DARK_GREEN, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)  # Add the equals button to the grid layout of the buttons_frame

    def create_buttons_frame(self):
        """
        Create a buttons frame using tkinter and return it.
        
        This method creates a tkinter Frame and packs it to expand and fill both directions (vertically
        and horizontally). The created frame is returned.
    
        Returns:
            frame (tk.Frame): The created tkinter Frame.
        """
        frame = tk.Frame(self.window)  # Create a Frame
        frame.pack(expand=True, fill="both")  # Pack the frame to expand and fill both directions
        return frame


    def update_total_label(self):
        """
        Update the total label with the current total expression.
        
        This method replaces the operator symbols in the total expression with their corresponding
        symbols from the operations dictionary and adds spaces around them for better readability.
        It then updates the total_label with the modified expression.
        """
        expression = self.total_expression  # Get the current total expression
        # Replace the operator symbols with their corresponding symbols from the operations dictionary
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
            self.total_label.config(text=expression)  # Update the total_label with the modified expression

    def update_label(self):
        """
        Update the current label with the current expression.
        
        This method updates the label with the current expression, displaying up to 11 characters.
        """
        self.label.config(text=self.current_expression[:11])  # Update the label with the current expression (up to 11 characters)
        
    def run(self):
        """
        Run the calculator's main loop.
        
        This method starts the tkinter main loop, which processes events and updates the GUI.
        """
        self.window.mainloop()  # Start the tkinter main loop
        
if __name__ == "__main__":
    # Instantiate the Calculator class and run the main loop
    calc = Calculator()
    calc.run()

