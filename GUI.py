#IMPORTS

from tkinter import *
from tkinter import ttk



#SETUP FUNCTION
def manage_action():
    a = side1_value.get()
    b = side2_value.get()
    c = hypotenuse_value.get()

    if c == 0:
        squared = (a ** 2) + (b ** 2)
        answer = squared ** 0.5
        answer_string.set("The answer is {:.2f}".format(answer))
    elif a == 0:
        squared = (c ** 2) - (b ** 2)
        answer = squared ** 0.5
        answer_string.set("The answer is {:.2f}".format(answer))
    elif b == 0:
        squared = (c ** 2) - (a **2)
        answer = squared ** 0.5
        answer_string.set("The answer is {:.2f}".format(answer))


#SETUP GUI
root = Tk()
root.title("Right Angled Triangle - Length Calculator")
#Create TOP frame
top_frame = ttk.LabelFrame(root, text="GREETINGS!")
top_frame.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

#Create Greeting text with a Label
greeting_label = ttk.Label(top_frame, text="Hello! Today we will be calculating the unknown length of a right-angled triangle.")
greeting_label.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

#Create MIDDLE frame
middle_frame = ttk.LabelFrame(root, text="OPTIONS")
middle_frame.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

#Create Label to describe the Combobox
description_label = ttk.Label(middle_frame, text="Which length do you want to calculate?:")
description_label.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

#Create Combo Box
options = ["Side", "Hypotenuse"]
options_var = StringVar()
options_var.set(options[0])

options_combobox = ttk.Combobox(middle_frame, textvariable=options_var, state="readonly")
options_combobox["values"]=options
options_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

#Create label to give instructions
entry_help_label = ttk.Label(middle_frame, text="Enter the length of the known sides, enter '0' for the unknown length")
entry_help_label.grid(row=2, column=1, padx=10, pady=10)


# Create a label for the hypotenuse field and pack it into the GUI
hypotenuse_entry_label = ttk.Label(middle_frame, text="Hypotenuse:")
hypotenuse_entry_label.grid(row=3, column=0, padx=10, pady=10)


#Create a variable to store hypotenuse
hypotenuse_value =IntVar()


#Create Entry for the hypotenuse
hypotenuse_entry = ttk.Entry(middle_frame, textvariable=hypotenuse_value)
hypotenuse_entry.grid(row=3, column=1, padx=10, pady=10, sticky="WE")

# Create a label for side1 field and pack it into the GUI
side1_entry_label = ttk.Label(middle_frame, text="Side 1:")
side1_entry_label.grid(row=4, column=0, padx=10, pady=10)


#Create a variable to store side1
side1_value =IntVar()

#Create Entry for the side1
side1_entry = ttk.Entry(middle_frame, textvariable=side1_value)
side1_entry.grid(row=4, column=1, padx=10, pady=10, sticky="WE")

# Create a label for side2 field and pack it into the GUI
side2_entry_label = ttk.Label(middle_frame, text="Side 2:")
side2_entry_label.grid(row=5, column=0, padx=10, pady=10)


#Create a variable to store side2
side2_value = IntVar()


#Create Entry for the side2
side2_entry = ttk.Entry(middle_frame, textvariable=side2_value)
side2_entry.grid(row=5, column=1, padx=10, pady=10, sticky="WE")

#Create Answer string
answer_string = StringVar()
answer_string.set("")

#Create Submit Button for the entry fields
submit_button = ttk.Button(middle_frame, text="Submit", command=manage_action)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

#Create BOTTOM frame
bottom_frame = ttk.LabelFrame(root, text="ANSWER")
bottom_frame.grid(row=2, column=1, padx=10, pady=10, sticky="NSEW")

#Create answer label
answer_label = ttk.Label(bottom_frame, textvariable=answer_string)
answer_label.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

root.mainloop()


