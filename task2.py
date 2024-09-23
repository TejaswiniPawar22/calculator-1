import tkinter as tk
from tkinter import messagebox

# Create a new tkinter window
master = tk.Tk()
master.title("MARKSHEET")
master.geometry("700x300")

# Entry objects for student details and grades
e1, e3 = tk.Entry(master), tk.Entry(master)  # Name and Roll No
grades_entries = [tk.Entry(master) for _ in range(4)]

# Mapping grades to credits
grade_credits = {
    "A": 4, "B": 3, "C": 2, "D": 1, "P": 0, "F": 0
}


def get_overall_grade(total_grades):
    # Define overall grade based on total grades
    if total_grades == 16:  # 4 subjects with grade A
        return "A"
    elif total_grades >= 12:  # 4 subjects with grade B or combination
        return "B"
    elif total_grades >= 8:  # 4 subjects with grade C or combination
        return "C"
    elif total_grades >= 4:  # 4 subjects with grade D or combination
        return "D"
    else:
        return "F"  # If total grades are below 4


def display():
    total_credits = 0
    valid_input = True
    total_grades = 0

    for entry in grades_entries:
        grade = entry.get().strip().upper()
        credits = grade_credits.get(grade, None)
        if credits is not None:
            total_credits += credits
            tk.Label(master, text=str(credits)).grid(row=grades_entries.index(entry) + 3, column=4)
        else:
            valid_input = False
            break

    if valid_input:
        tk.Label(master, text=str(total_credits)).grid(row=7, column=4)  # Total credits

        # Overall grade based on total grades
        overall_grade = get_overall_grade(total_credits)
        tk.Label(master, text=overall_grade).grid(row=9, column=4)  # Overall grade

        # Pass/Fail status
        status = "Pass" if total_credits > 7 else "Fail"
        tk.Label(master, text=status).grid(row=10, column=4)  # Status
    else:
        messagebox.showerror("Invalid Input", "Please enter valid grades (A, B, C, D, P, F).")


# Create UI elements
labels = [
    ("Name", 0, 0), ("Roll.No", 1, 0),
    ("Sr.No", 2, 0), ("Subject", 2, 1), ("Grade", 2, 2),
    ("Sub Credit", 2, 3), ("Credit obtained", 2, 4)
]

for text, r, c in labels:
    tk.Label(master, text=text).grid(row=r, column=c)

subjects = ["English", "Science", "Mathematics", "Language"]
for i, subject in enumerate(subjects):
    tk.Label(master, text=str(i + 1)).grid(row=3 + i, column=0)
    tk.Label(master, text=subject).grid(row=3 + i, column=1)
    tk.Label(master, text="4" if i != 2 else "3").grid(row=3 + i, column=3)

# Organize input fields
e1.grid(row=0, column=1)
e3.grid(row=1, column=1)
for i, entry in enumerate(grades_entries):
    entry.grid(row=3 + i, column=2)

# Submit button
tk.Button(master, text="Submit", bg="green", command=display).grid(row=8, column=1)

# Labels for total credits, total grades, overall grade, and status
tk.Label(master, text="Total credit").grid(row=7, column=3)
tk.Label(master, text="Overall Grade").grid(row=9, column=3)
tk.Label(master, text="Status").grid(row=10, column=3)

master.mainloop()

