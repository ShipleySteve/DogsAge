import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("Label Test")

# Heading
label_heading = tkinter.Label(window, text = "Dogs Age Calculator", font=('calibre',24,'normal'))

# Get Dogs age
age_var = tkinter.StringVar()
age_lab = tkinter.Label(window, text = "Age :")
age_entry = tkinter.Entry(window, textvariable = age_var)

# button
def calc():
    human_age = int(age_var.get()) * 7
    tkinter.messagebox.showinfo('title', f"Your dog is {human_age} years old in human years")

calc_button = tkinter.Button(window, text ="Calculate", command = calc)

# layout widgets
label_heading.grid(row = 0, column = 0)
age_lab.grid(row = 3, column = 0)
age_entry.grid(row=3,column=1)
calc_button.grid(row=5, column=1)

# main loop
window.mainloop()
