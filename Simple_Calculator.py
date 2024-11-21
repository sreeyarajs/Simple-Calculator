from tkinter import *
from tkinter import messagebox

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Evaluate the expression in the screen
            value = eval(screen.get())
            scvalue.set(value)
        except Exception as e:
            # Handle any error and display 'Error' message
            scvalue.set("Error")
        screen.update()
                
    elif text == "C":
        # Clear the screen
        scvalue.set("")
        screen.update()
    
    else:
        # Append the button text to the screen value
        if scvalue.get() == "Error":
            scvalue.set("")  # Reset the screen if "Error" is present
        scvalue.set(scvalue.get() + text)
        screen.update()

# Create the main application window
root = Tk()
root.geometry("400x600")  # Adjusted size for better layout
root.title("Calculator")

# Screen for displaying the result
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold", justify=RIGHT, bd=8, relief=SUNKEN)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Function to create buttons dynamically
def create_button(frame, text, padx, pady, bg_color, fg_color):
    b = Button(frame, text=text, padx=padx, pady=pady, font="lucida 20 bold", relief=RAISED, 
               bg=bg_color, fg=fg_color, activebackground="#4CAF50", activeforeground="white")
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-1>", click)
    b.bind("<Enter>", lambda e: b.config(bg="#4CAF50"))  # Hover effect
    b.bind("<Leave>", lambda e: b.config(bg=bg_color))  # Reset color after hover
    return b

# Button color settings
button_colors = {
    "C": "#7393B3",  # Red for clear button
    "=": "#7393B3",  # Blue for equal button
    "+": "#7393B3",  # Green for addition
    "-": "#7393B3",  # Amber for subtraction
    "*": "#7393B3",  # Deep orange for multiplication
    "/": "#7393B3",  # Teal for division
    "%": "#7393B3",  # Purple for percentage
    ".": "#7393B3",  # Blue-grey for dot
    "0": "#6082B6",  # Cyan for zero
    "1": "#6082B6",  # Blue for number
    "2": "#6082B6",  # Blue for number
    "3": "#6082B6",  # Blue for number
    "4": "#6082B6",  # Blue for number
    "5": "#6082B6",  # Blue for number
    "6": "#6082B6",  # Blue for number
    "7": "#6082B6",  # Blue for number
    "8": "#6082B6",  # Blue for number
    "9": "#6082B6",  # Blue for number
    "00": "#6082B6"  # Blue for double zero
}

# Create button rows
button_texts = [
    ["9", "8", "7", "C"],
    ["6", "5", "4", "/"],
    ["3", "2", "1", "*"],
    ["0", ".", "00", "-"],
    ["%", "=", "+", ""]
]

# Create buttons with custom colors
for row in button_texts:
    f = Frame(root, bg="grey")
    for text in row:
        if text:  # Add only if text is not empty
            color = button_colors.get(text, "#4CAF50")  # Default to green
            create_button(f, text, 20, 20, color, "white")
    f.pack()

root.mainloop()



