import tkinter as tk
from tkinter import messagebox

# Define the question and answer choices
question = "Where is California located in the USA?"
choices = ["A. East Coast", "B. West Coast", "C. Midwest", "D. South"]

# Define the correct answer
correct_answer = "B. West Coast"


# Function to check the selected answer
def check_answer():
    if var.get() == correct_answer:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", "Incorrect. The correct answer is: " + correct_answer)


# Create the main window
root = tk.Tk()
root.title("U.S. State Geography Quiz")

# Create a label for the question
question_label = tk.Label(root, text=question)
question_label.pack()

# Create radio buttons for answer choices
var = tk.StringVar()
for choice in choices:
    radio_button = tk.Radiobutton(root, text=choice, variable=var, value=choice)
    radio_button.pack(anchor=tk.W)

# Create a submit button to check the answer
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack()

# Start the main event loop
root.mainloop()
