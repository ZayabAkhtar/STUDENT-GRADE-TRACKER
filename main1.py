import tkinter as tk
from tkinter import messagebox, font

class GradeTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Grade Tracker")
        master.geometry("400x400")
        master.configure(bg="#f0f8ff")  # Light background color

        self.grades = {}
        self.subject_count = 0
        self.max_subjects = 5

        # Title Label
        self.title_label = tk.Label(master, text="Student Grade Tracker", bg="#f0f8ff", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Subject Entry
        self.subject_label = tk.Label(master, text="Enter Subject:", bg="#f0f8ff", font=("Helvetica", 12))
        self.subject_label.pack(pady=5)

        self.subject_entry = tk.Entry(master, font=("Helvetica", 12))
        self.subject_entry.pack(pady=5)

        # Grade Entry
        self.grade_label = tk.Label(master, text="Enter Grade:", bg="#f0f8ff", font=("Helvetica", 12))
        self.grade_label.pack(pady=5)

        self.grade_entry = tk.Entry(master, font=("Helvetica", 12))
        self.grade_entry.pack(pady=5)

        # Buttons
        self.submit_button = tk.Button(master, text="Add Grade", command=self.add_grade, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        self.submit_button.pack(pady=10)

        self.summary_button = tk.Button(master, text="Show Summary", command=self.show_summary, bg="#2196F3", fg="white", font=("Helvetica", 12))
        self.summary_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="#f44336", fg="white", font=("Helvetica", 12))
        self.quit_button.pack(pady=10)

        # Footer
        self.footer_label = tk.Label(master, text="© Zayab Akhtar", bg="#f0f8ff", font=("Helvetica", 10))
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def add_grade(self):
        if self.subject_count < self.max_subjects:
            subject = self.subject_entry.get()
            try:
                grade = float(self.grade_entry.get())
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid numeric grade.")
                return

            if subject in self.grades:
                self.grades[subject].append(grade)
            else:
                self.grades[subject] = [grade]
                self.subject_count += 1

            self.subject_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Grade added for {subject}.")
        else:
            messagebox.showwarning("Limit Reached", "You can only enter grades for up to 5 subjects.")

    def show_summary(self):
        if not self.grades:
            messagebox.showinfo("Summary", "No grades entered.")
            return

        summary = "Grade Summary:\n"
        total_grades = 0
        total_subjects = 0

        for subject, subject_grades in self.grades.items():
            subject_average = sum(subject_grades) / len(subject_grades)
            total_grades += sum(subject_grades)
            total_subjects += len(subject_grades)
            summary += f"{subject}: Grades = {subject_grades}, Average = {subject_average:.2f}\n"

        if total_subjects > 0:
            overall_average = total_grades / total_subjects
            summary += f"\nOverall Average: {overall_average:.2f}"

        messagebox.showinfo("Summary", summary)

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeTrackerApp(root)
    root.mainloop()