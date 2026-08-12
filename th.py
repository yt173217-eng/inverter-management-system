import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Inventory Management System")
root.geometry("1000x700")


# ---------- TITLE ----------

title = tk.Label(
    root,
    text="INVENTORY MANAGEMENT SYSTEM",
    font=("Arial", 28, "bold")
)

title.pack(pady=20)


# ---------- MAIN AREA ----------

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)


# ---------- LEFT SIDE ----------

form_frame = tk.Frame(main_frame)
form_frame.pack(side="left", padx=30, pady=20)


# ---------- RIGHT SIDE ----------

display_frame = tk.Frame(main_frame)
display_frame.pack(side="right", padx=30, pady=20)


# ---------- LEFT FRAME TITLE ----------

form_title = tk.Label(
    form_frame,
    text="Add Product",
    font=("Arial", 20, "bold")
)

form_title.grid(row=0, column=0, columnspan=2, pady=15)


root.mainloop()