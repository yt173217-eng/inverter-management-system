import tkinter as tk 
from tkinter import messagebox
root = tk.Tk() # create a main window

root.title("Inventory Management System")
root.geometry("1000x700")# set the windows size:
#=========Title =========================

label1 = tk.Label(root,text="Welcome Rehan",font=("Arial", 15, "bold"))

label2 = tk.Label(root,text="Inventory Management System",font=("Arial", 30,'bold'))
  
label1.pack(pady=5)
label2.pack(pady=5)
#======================Product ID============================
id_label = tk.Label(root,text="Product ID")
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack(pady=50)

#=================== Product Name===============================
name_label = tk.Label(root,text="Product Name")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

#===================== Category ====================================
category_label = tk.Label(root,text="Category")
category_label.pack()

category_entry = tk.Entry(root)
category_entry.pack(padx=5)

#===============================Price==================================
price_label = tk.Label(root,text="Price")
price_label.pack()

price_entry = tk.Entry(root)
price_entry.pack(pady=5)

#======================Quantity===========================================
quantity_label = tk.Label(root,text="Quantity")
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack(pady=5)
#===========================================================================
supplier_label = tk.Label(root,text="Supplier")
supplier_label.pack()

supplier_entry = tk.Entry(root)
supplier_entry.pack(pady=5)
#===========================Add Product============================================

def add_product():
    product_id = id_entry.get()
    name = name_entry.get()
    category = category_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    supplier = supplier_entry.get()

    messagebox.showinfo(
        "Product Information",
        f"ID: {product_id}\n"
        f"Name:{name}\n"
        f"Category: {category}\n"
        f"Price:{price}\n"
        f"quantity: {quantity}\n"
        f"supplier: {supplier}\n"
    )
add_button = tk.Button(root,text="Add Product",command=add_product)
add_button.pack(pady=20)

root.mainloop()