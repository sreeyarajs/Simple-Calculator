from tkinter import *
import math

# Function to handle button clicks
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Replace custom operators with Python-compatible ones
            expression = screen.get().replace("^", "**").replace("π", str(math.pi)).replace("e", str(math.e))
            value = eval(expression)
            scvalue.set(value)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text == "x²":
        try:
            value = float(screen.get())
            scvalue.set(value**2)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    elif text == "x³":
        try:
            value = float(screen.get())
            scvalue.set(value**3)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    elif text == "1/x":
        try:
            value = float(screen.get())
            scvalue.set(1 / value)
        except Exception as e:
            scvalue.set("Error")
        screen.update()
    else:
        if scvalue.get() == "Error":
            scvalue.set("")
        scvalue.set(scvalue.get() + text)
        screen.update()

# Function to handle scientific operations
def scientific_operation(op):
    try:
        expression = screen.get()
        if expression == "":
            scvalue.set("Error")
        else:
            value = float(expression)
            if op == "sin":
                scvalue.set(math.sin(math.radians(value)))
            elif op == "cos":
                scvalue.set(math.cos(math.radians(value)))
            elif op == "tan":
                scvalue.set(math.tan(math.radians(value)))
            elif op == "sinh":
                scvalue.set(math.sinh(value))
            elif op == "cosh":
                scvalue.set(math.cosh(value))
            elif op == "tanh":
                scvalue.set(math.tanh(value))
            elif op == "asinh":
                scvalue.set(math.asinh(value))
            elif op == "acosh":
                scvalue.set(math.acosh(value))
            elif op == "atanh":
                scvalue.set(math.atanh(value))
            elif op == "sqrt":
                scvalue.set(math.sqrt(value))
            elif op == "log":
                scvalue.set(math.log10(value))
            elif op == "ln":
                scvalue.set(math.log(value))
            elif op == "floor":
                scvalue.set(math.floor(value))
            elif op == "ceil":
                scvalue.set(math.ceil(value))
        screen.update()
    except Exception as e:
        scvalue.set("Error")
        screen.update()

# Create the main application window
root = Tk()
root.geometry("400x650")
root.title("Sample Scientific Calculator")

# Style configuration for pastel blue and hover effect
button_bg = "#a1c6ea"  # Pastel blue color
button_fg = "#333"  # Dark text color
button_hover_bg = "#7bb7e2"  # Slightly darker blue for hover
button_hover_fg = "white"  # White text on hover
frame_bg = "#e0e0e0"

# Screen for displaying the result
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold", justify=RIGHT, bd=8, relief=RAISED)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Function to create buttons dynamically
def create_button(frame, text, bg_color, fg_color, hover_bg, hover_fg):
    b = Button(frame, text=text, font="lucida 12 bold", bg=bg_color, fg=fg_color, relief=RAISED, bd=3, padx=10, pady=5)
    b.pack(side=LEFT, padx=3, pady=3)
    b.bind("<Enter>", lambda e: b.config(bg=hover_bg, fg=hover_fg))
    b.bind("<Leave>", lambda e: b.config(bg=bg_color, fg=fg_color))
    if text in ["sin", "cos", "tan", "sinh", "cosh", "tanh", "asinh", "acosh", "atanh", "sqrt", "log", "ln", "floor", "ceil"]:
        b.config(command=lambda op=text: scientific_operation(op))
    else:
        b.bind("<Button-1>", click)
    return b

# Button groups and colors
button_texts = [
    ["C", "sin", "cos", "tan"],
    ["sinh", "cosh", "tanh", "sqrt"],
    ["asinh", "acosh", "atanh", "log"],
    ["ln", "floor", "ceil", "x²"],
    ["x³", "1/x", "π", "e"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["^", "="]
]

# Create buttons
for row in button_texts:
    f = Frame(root, bg=frame_bg)
    for text in row:
        create_button(f, text, button_bg, button_fg, button_hover_bg, button_hover_fg)
    f.pack()

root.mainloop()
