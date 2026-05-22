import tkinter as tk
from tkinter import messagebox
import csv
from datetime import date

# Save data function
def save_data():
    today = date.today()

    symptoms = symptom_entry.get()
    water = water_entry.get()
    sleep = sleep_entry.get()
    mood = mood_entry.get()

    if symptoms == "" or water == "" or sleep == "" or mood == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, symptoms, water, sleep, mood])

    messagebox.showinfo("Saved", "Data saved successfully!")

    symptom_entry.delete(0, tk.END)
    water_entry.delete(0, tk.END)
    sleep_entry.delete(0, tk.END)
    mood_entry.delete(0, tk.END)

# View records function
def view_records():
    record_window = tk.Toplevel(root)
    record_window.title("Health Records")
    record_window.geometry("600x400")

    text_area = tk.Text(record_window)
    text_area.pack(fill=tk.BOTH, expand=True)

    try:
        with open("data.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                line = (
                    f"Date: {row[0]} | "
                    f"Symptoms: {row[1]} | "
                    f"Water: {row[2]}L | "
                    f"Sleep: {row[3]} hrs | "
                    f"Mood: {row[4]}\n"
                )

                text_area.insert(tk.END, line)

    except FileNotFoundError:
        text_area.insert(tk.END, "No records found!")

# Main window
root = tk.Tk()
root.title("PCOS Health Tracker")
root.geometry("400x450")
root.config(bg="#f5d9e8")

title = tk.Label(
    root,
    text="PCOS Health Tracker",
    font=("Arial", 18, "bold"),
    bg="#f5d9e8"
)
title.pack(pady=10)

tk.Label(root, text="Symptoms", bg="#f5d9e8").pack()
symptom_entry = tk.Entry(root, width=40)
symptom_entry.pack(pady=5)

tk.Label(root, text="Water Intake (Litres)", bg="#f5d9e8").pack()
water_entry = tk.Entry(root, width=40)
water_entry.pack(pady=5)

tk.Label(root, text="Sleep Hours", bg="#f5d9e8").pack()
sleep_entry = tk.Entry(root, width=40)
sleep_entry.pack(pady=5)

tk.Label(root, text="Mood", bg="#f5d9e8").pack()
mood_entry = tk.Entry(root, width=40)
mood_entry.pack(pady=5)

save_btn = tk.Button(
    root,
    text="Save Data",
    command=save_data,
    bg="#d63384",
    fg="white",
    width=20
)
save_btn.pack(pady=15)

view_btn = tk.Button(
    root,
    text="View Records",
    command=view_records,
    bg="#6f42c1",
    fg="white",
    width=20
)
view_btn.pack()

root.mainloop()