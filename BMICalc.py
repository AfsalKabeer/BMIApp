from tkinter import *

# Initialize display window and title
root = Tk()
root.title("BMI Calculator")
root.configure(width=100, height=100)
root.configure(bg="black")

# calc() function to determine BMI Value and display status accordingly
def calc():
    BMI = BMI_Val(mass.get(), height.get())
    bmi_Val.set(format(BMI, ".2f"))
    Stat = getStatus()
    stat.set(Stat)


def BMI_Val(mass, height):            # Function to calculate BMI Value
    return mass / height ** 2


def getHeight():
    return height


def res():            # Function to clear All value fields
    stat.set('')
    bmi_Val.set('0.0')
    mas.delete(0, 'end')
    heigh.delete(0, 'end')


def get_Width():
    return mass


def getStatus():           # Function to output status
    if (bmi_Val.get() > 40):
        return "You are Obese Class 3"
    elif (35 < bmi_Val.get() <= 40):
        return " You are Obese Class 2"
    elif (30 < bmi_Val.get() <= 35):
        return " You are Obese Class 1"
    elif (25 < bmi_Val.get() <= 30):
        return " You are Overweight"
    elif (18.5 < bmi_Val.get() <= 25):
        return " You are Normal weight"
    elif (17 < bmi_Val.get() <= 18.5):
        return " You are Mild Thin"
    else:
        return "You are moderately thin"

# To create height field and design
height = DoubleVar()
h_label = Label(root, text="Height", fg="red", bg="black", font=("Calibri 14 bold"), pady=5, padx=8)
heigh = Entry(root, textvariable=height)
h_label.grid(row=2)
heigh.grid(row=2, column=1, columnspan=2, padx=5)

# To create mass field and design
mass = DoubleVar()
w_label = Label(root, text="Mass", fg="red", bg="black", font=("Calibri 14 bold"), pady=10, padx=2)
mas = Entry(root, textvariable=mass)
w_label.grid(row=4)
mas.grid(row=4, column=1)

bmi_Val = DoubleVar()
stat = StringVar()
bmi = Label(root, text="BMI: ", fg="blue", bg="black", font=("Calibri 14 bold"), padx=2, pady=10, justify=LEFT)
status = Label(root, text="Status", fg="blue", font=("Calibri 14 bold"), pady=10, padx=2)
status_msg = Label(root, textvariable=stat, fg="white", bg="black", font=("Calibri 14 bold"), padx=2, pady=10)

# To create BMI Value and status display field
BMI_total = Label(root, textvariable=bmi_Val, fg="white", bg="black", font=("Calibri 14 bold"), padx=2, pady=10)
bmi.grid(row=6)
status.grid(row=7)
BMI_total.grid(row=6, column=1)
status_msg.grid(row=7, column=1)

# Create calculate and reset button
calculate = Button(root, text="Calculate", command=calc, fg="black", bg="white", font=("Calibri 14 bold"))
clear = Button(root, text="Reset", command=res, fg="black", bg="white", font=("Calibri 14 bold"))
calculate.grid(row=8)
clear.grid(row=8, column=3)
label1 = Label(root, text="Height in M and Weight in KG", fg="black", bg="white", font=("Calibri 14 bold"))
label1.grid(row=0, column=1)

root.mainloop()
