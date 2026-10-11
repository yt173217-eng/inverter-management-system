#====================================
# Inventory Management System 
#====================================
import json

from tabulate import tabulate


class Product:
    def __init__(self,product_id,name,category,price,quantity,supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def show_details(self):
        print(f"Product ID = {self.product_id}")
        print(f"Name = {self.name}")
        print(f"Product Category = {self.category}")
        print(f"Product Price = {self.price}")
        print(f"Product Quantity = {self.quantity}")
        print(f"Product Supplier = {self.supplier}")

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category":self.category,
            "price":self.price,
            "quantity":self.quantity,
            "supplier":self.supplier
        }
class Inventory:
    def __init__(self):
        self.products = []
        self.load_from_json()
#==========================================================================
    def add_product(self,product):
        self.products.append(product)
        self.save_to_json()
#==========================================================================
    def create_product(self):
        while True:
            new_ID = input("Enter new product id = ").strip().lower()
            if not(new_ID.isdigit() and len(new_ID)== 4):
                print("❌ ID not valid Please enter eaxtly 4 digit")
                continue
            new_ID = int(new_ID)
            found = False

            for p in self.products:
                if (new_ID == p.product_id):
                    print(f"❌ Product id also exists {new_ID}....")
                    found =True
                    break

            if found:
                continue
            print("✅ Product id available...")
            
                        
            print("============================================================")
            while True:
                try:
                    new_name = input("Enter product name = ").strip().lower()
                    found = False
                    for p in self.products:
                        if(new_name.lower() == p.name.lower()):
                            print("❌ Product name is not available...")
                            found = True
                            break      
                    if not found:
                        print("✅ Product name is  available..")
                        
                        break
                    
                except ValueError:
                    ("❌ Invalid input ! Please enter a valid input..")

            print("============================================================")
           
            while True:
                try:
                    new_category = input("Enter product category = ").strip()
                    if not (new_category):
                        print("Do not leave empty")
                    if not(new_category.isalpha()):
                        print("❌ Invalid input. Please add only letters/words")
                        continue
                    print(f"✅ Category add successfulyy {new_category}")
                    
                    break
                except ValueError:
                    raise ValueError("❌ Invalid input Enter a valid input")

            print("============================================================")

            while True:
                try:
                    new_product_price = int(input("Enter new product price = "))
                    if (new_product_price <= 0):
                        print(f"❌ You can not add {new_product_price}")
                        print("❌ Product price must be greater 0 [1,23,45,67]")
                        continue
                    else:
                        print(f"✅ Product new price {new_product_price} added successfully!")
                        
                        break
                except ValueError:
                    print("❌ Invalid input Enter a numberic number")

            print("============================================================")

            while True:
                try:
                    new_product_quantity = int(input("Enter new product quantity = "))
                    if (new_product_quantity <= 0):
                        print(f"❌ You can not add {new_product_quantity} quantity.")
                    else:
                        print(f"✅ Product quantity add {new_product_quantity} successfully!")
                        
                        break
                except ValueError:
                    print("Invalid input enter a valid input")

            print("============================================================")

            while True:
                try:
                    new_supplier = input("Enter new supplier = ").strip().lower()
                      # 1. Check if the input is completely empty
                    if not new_supplier:
                        raise ValueError("❌ Input cannot be empty.")
                    if not new_supplier.isalpha():
                        raise ValueError("❌ Invalid input. Please add only letters/words.")
                    
                    print(f"✅ New supplier added successfully! {new_supplier}")
                    
                    break
                except ValueError as e:
                    print(e)
            
            product = Product(
                new_ID,
                new_name,
                new_category,
                new_product_price,
                new_product_quantity,
                new_supplier
            )
            return product
     
                        





#==========================================================================
    def view_all_product(self):
        table_data = []
        for product in (self.products):
            table_data.append([
                product.product_id,
                product.name,
                product.category,
                product.price,
                product.quantity,
                product.supplier,
            ])
        headers = ["Product_id","Name","Category","Price","Quantity","Supplier"]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))  
        print(f"\nTotal Products: {len(self.products)}")
#==========================================================================
    def search_product(self):
        while True:
            try:
                product_id = input("Enter Product ID(4 digit) or (Q) to eixt = ")
                # Allow user to exit search
                if (product_id.lower() == "q"):
                    print("Exiting search...")
                    break 
                # Validate input: must be exactly 4 digits
                if not(product_id.isdigit() and len(product_id) == 4):
                    print("Invalid input ! ID must exactly 4 digit")
                    continue
                product_id = int(product_id)
                
                found = False
                for p in self.products:
                    if(product_id == p.product_id):
                        total = [[p.product_id,p.name]]
                        i = ["Product","Name"]
                        print(tabulate(total,headers=i,tablefmt='grid'))
                        print("========================")
                        found = True
                        break
                if not found:
                    print(f"Product with ID {product_id} not found")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")    
#==========================================================================
    def valid_id(self):
        while True:
            try:
                product_id = input("Enter Product ID or Q to exit = ")
                if (product_id.lower() == "q"):
                    print("You Exit....")
                    break
                product_id = int(product_id)
                found = False
                for p in self.products:
                    if(product_id == p.product_id):
                        print(f"{p.product_id} Product ID Found...")
                        found = True
                        return p
                if not found:
                    print("❌ Product not found")
                    break
            except ValueError:
                print("Invalid input ! Please enter a (4 digit) number...")
#==========================================================================          
    def update_product_details(self):
                    
        while True:
            print("1. Name")
            print("2. Catogory")
            print("3. Price")
            print("4. Quantity")
            print("5. Supplier")
            print("6. New Details")
            print("7. Save Details")
            print("8. Exit")
            choice = input("Enter you choise: ").strip()
            
            if choice == "8":
                print("✅ GoodBye ✅")
                break

            if choice in ["1","2","3","4","5","6"]:
                product = self.valid_id()
                if not product:
                    continue

                elif (choice == "1"):
                    name = input("Enter a new name: ")
                    product.name = name
                    print("Name Update Succesfully!")
                    self.save_to_json()

                elif (choice == "2"):
                   category = input("Enter Categorey to Change: ")
                   product.category = category
                   print(f"Catogory Update Succesfully{product.name}")
                   self.save_to_json()

                elif (choice == "3"):
                    while True:
                        try:
                            print("==================")
                            new_price = int(input("Enter Product New Price: "))
                            if new_price <= 0:
                                print(f"You can not add price {new_price}")
                                continue
                            print("==================")
                            product.price = new_price
                            print(f"Price Update Succesfully!!")
                            print(f"New Price: {product.price}")
                            self.save_to_json()
                            break
                        except ValueError:
                            print("Invalid Price ! Please enter a number")

                elif (choice == "4"):
                    while True:
                        try:
                            quantity = int(input("Enter Product New Quantity: "))
                            if quantity <= 0:
                                print(f"You can not add quantity {quantity}")
                                continue
                            product.quantity = quantity
                            print(f"{product.quantity} - Product New Quantity Update Succesfully!!")
                            self.save_to_json()
                            break
                        except ValueError:
                            print("Invalid quantity ! Enter a valid quantity")

                elif (choice == "5"):
                    while True:

                        new_supplier = input("Enter New Supplier: ")
                        if (new_supplier.strip()):   
                            product.supplier = new_supplier
                            print("New Supplier Update Succesfully!!✅")
                            self.save_to_json()
                            break

                elif (choice == "6"):
                    for p in self.products:
                        details = [[p.product_id,p.name,p.category,p.price,p.quantity,p.supplier]]
                    print()
                    header = ['ID',"Name","Category","Price","Quantity","Supplier"]
                    print(tabulate(details,headers=header,tablefmt="preety"))
                    print()

                elif(choice =="7"):
                    self.save_to_json()
                    print("Details save successfully!")
                    
            
                else:
                    print("Invalid input ! Please enter a valid input")
#==========================================================================
    def remove_product(self):
        while True:
            product = self.valid_id()
            if product:
                while True:
                    remove_p = input("Are you sure? (Y/N) ")
                    if remove_p.lower() == "y":#cancel
                       self.products.remove(product)
                       print(f" Product deleted successfully. ✅")
                       self.save_to_json()
                       break
                    if remove_p.lower() == "n":
                       print("You Exit....")
                       break
                    else:
                      print("Please enter Y or N.")
                      
            
            break
#==========================================================================
    def restock_product(self):
        try:
            product = self.valid_id()
            if not product:
                print("Product not found")
                return
            
            table =  [[product.quantity]]
            headers = ["Available Quantity"]
            print(tabulate(table,headers=headers,tablefmt="grid"))
            added_quantity = int(input("How many items do you want to add? "))

            if (added_quantity <= 0):
                print(f"❌ You cannot update with {added_quantity}. Please enter a positive number.")
                return
            
            # new quantity
            product.quantity += added_quantity
            add = [[added_quantity,product.quantity]]# old quantity with out update
            header = ["Add Quantity","Total quantity"]
            print(tabulate(add , headers=header, tablefmt="grid"))
            self.save_to_json()
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer")
#==========================================================================                
    def sell_product(self):
            while True:
                
                    
                product = input("Enter Product ID or Q to quit: ")
                if(product.lower() == "q".lower()):
                    print("You Exit...")
                    break

                    # if input empty it's continue
                if(not product):
                    print("You can not leave empyt list")
                    continue


                product = int(product)
                found = False
                for p in self.products:
                    if(product == p.product_id):
                        print("ID Found it...")
                        found =True
                if not found:
                    print("ID not found invalid ID")
                    continue

                while True:
                    try:        
                        sell_product = input("How many item you want to sell (q to quit): ")
                        if(sell_product == "q"):
                            print("You exist.")
                            break 
                        else:
                        
                            sell_product = int(sell_product)
                    except ValueError:
                        print("INVALID INPUT")
                        continue

                    if sell_product <= 0:
                        print(f"You cannot update with {sell_product}. Please enter a postive number")
                        continue
                     # it's check before subtracting Is sell quantity greater than available quantity?
                    
                    if (sell_product > p.quantity):
                        print("❌ Not enough stock available.")
                        print(f"Enter quantity between 1 and {p.quantity}:  ")
                    # save old quantity
                    old_quantity = p.quantity 
                    p.quantity -= sell_product
                    sell_price = sell_product * p.price
                    
                    table = [[p.price,old_quantity,p.quantity]]
                    header = ["Price","Old_Quantity","New_Quantity"]
                    print(tabulate(table,headers=header,tablefmt='pretty'))

                    
                    
                    
                    print(f"✅ Product sold successfully. Total price. {sell_price}")
                    self.save_to_json()
            
            
            
#==========================================================================                    
    def low_stock_alert(self):
        """Prints a low stock alert for products with quantity < 5."""
        low_stock_items = [p for p in self.products if (p.quantity <5)]
        if low_stock_items:
            print("⚠️  Low Stock Alert!")

            stock_details = []
            for p in low_stock_items:
                stock_details.append([p.name,p.quantity])
            headers = ["Name","Quantity"]
            print(tabulate(stock_details, headers=headers, tablefmt="pretty"))
                
                
        else:
            print("✅ All products have sufficient stock.")
#==========================================================================            
    def calculate_total_inventory_value(self):
        #print total value of everythig in inventory
        
        total_value = 0
        for p in self.products:
            total_value += p.price * p.quantity
        # prepare data for tabulate (single row, single column)    
        add_data = [[total_value]]  

        print(f"✅ Total inventory value ")
        print("=======================")
        herder = ["Total Value ($)"]
        print(tabulate(add_data,herder,tablefmt="grid"))

    

        
#==========================================================================
    def sort_by_name(self):
        self.products.sort(key=lambda p: p.name) # Sort the list. lambda p: p.name → "For each Product object (p), use its
        total_sort = []
        print("✅ =================")
        print("Sort by name...")
        print("✅ =================")
        for p in self.products:#key= → "What should I compare?"
            total_sort.append([p.name])
        header = ["Name"]
        print(tabulate(total_sort, headers=header, tablefmt="grid"))
            
#==========================================================================
    def sort_by_pricr(self):
        self.products.sort(key=lambda x: x.price)
        sort_price = []
        print("✅ =================")
        print("Sort by name...")
        print("✅ =================")
        for index,p in enumerate(self.products,start=1):
            sort_price.append([index,p.name,p.price,p.quantity])
        headers = ["Index","Name","Price","Quantity"]
        print(tabulate(sort_price, headers=headers, tablefmt="grid"))

            
            
#==========================================================================
    def sort_by_quantity(self):
        self.products.sort(key=lambda x:x.quantity)
        print("✅ =================")
        print("Sort by price...")
        print("✅ =================")
        for p in self.products:
            print()
            print("===================")
            p.show_details()
            
#==========================================================================                
    def filter_by_category(self):
        while True:
            category = input("Enter a product to filter or (q to quit): ").strip()

            if category.lower() =="q":
                print("You Exit....")
                break
            if not category:
                print("❌ No categories provided")
                continue

            categories = [c.strip() for c in category.split(",") if c.strip()]
            found = False
            print("\n🔎 Searching...\n")
            #print header once
            print("✅ ======================")
            print(f"Showing products in category: {category}")
            print("======================")
            total_catgory = []
            
            found = False
            for index, p in enumerate(self.products,start=1):
                for c in categories:
                    if (c.lower() in p.category.lower()):
                        total_catgory.append([index,p.product_id,p.name,p.category,p.price,p.supplier]) 
                        found = True
                        break              
            if not found:
                #Collect all unique categories from products
                available = sorted(set([p.category for p in self.products]))
                print("❌ No categories match your input....")
                print("📌 Available category are:")
                for cat in available:
                    print("-",cat)
            if total_catgory:
                headers = ["Index","ID","Name","Category","Price","Supplier"]
                print(tabulate(total_catgory,headers=headers,tablefmt="fancy_grid"))
                print(f"Total Category:{len(total_catgory)}") 
#==========================================================================
    def supplier(self):
        #sort products by name supplier name
        self.products.sort(key=lambda x: x.supplier)
        # collect unique suppliers
        unique_suppliers = sorted({p.supplier for p in self.products})
        # Print unique suppliers once

        print("===========================")
        print("📌 Unique Suppliers")
        print("===========================")
        i = 0
        for supplier in unique_suppliers:
            i+=1
            print(f"{i}. {supplier} ")
            print("=============")
        
          
        self.products.sort(key=lambda x : x.quantity)
        detail = []
        print("\n🔎 Product sorted by supplier: \n")
        for index,p in enumerate(self.products,start=1):
            detail.append([index,p.supplier,p.name,p.quantity])
        header = ["Index","Supplier","Name","Quantity"]
        print(tabulate(detail, headers=header, tablefmt="grid"))


        
    
            
#==========================================================================                                       
    def save_to_json(self):
        data = [] # it's just Temporary list.
        for product in self.products:
            data.append(product.to_dict())
        with open("inventory.json", "w") as file:
            json.dump(data,file,indent=4)
        print("Data save successfully!")                    
#==========================================================================
    def load_from_json(self):
        try:
            self.products.clear()
            with open("inventory.json","r") as file:
                data = json.load(file)
                for prod_uct in data:
                    product = Product(
                    prod_uct["product_id"],
                    prod_uct["name"],
                    prod_uct["category"],
                    prod_uct["price"],
                    prod_uct["quantity"],
                    prod_uct["supplier"]
                )
                    self.products.append(product)
                    #print(len(self.products))
            print("✅ Data loaded successfully!")
        except FileNotFoundError:
            print("Invalid File Please enter a valid name:")           
#==========================================================================
           
    def export_to_csv(self):
        with open("inventory.csv", "w") as file:#Open a file in write mode:
            file.write("product_id,name,category,price,quantity,supplier\n")#Write a header
            for product in self.products:#loop through object
                file.write( #access object attributes
                    f"{product.product_id},"
                    f"{product.name},"
                    f"{product.category},"
                    f"{product.price},"
                    f"{product.quantity},"
                    f"{product.supplier}\n"#Create CSV rows with f-strings.
                )
            print("✅ CSV Export successful!")

            
#===============================================\

    def import_from_csv(self):
        try:
            with open("inventory.csv","r") as file:
                file.readline()#skip header
            #👉 Python reads the first line (the header) and moves the file pointer to the next line.
                self.products.clear()  
                for line in file:
                    parts = line.strip().split(",")
                    product = Product(
                        int(parts[0]),#product_id
                        parts[1],#name
                        parts[2],#category
                        int(parts[3]),#price
                        int(parts[4]),#quantity
                        parts[5]#supplier
                    )    
                    self.products.append(product)
                    #print(len(self.products))
                print("✅ CSV Import successful!")
        except FileNotFoundError:
            print("❌ CSV file not found.")
#===============================================\
    def menu(self):
        options = {
            "1":lambda:self.add_product(self.create_product()),
            "2":self.view_all_product,
            "3":self.search_product,
            "4":self.update_product_details,
            "5": self.remove_product,
            "6":self.restock_product,
            "7":self.sell_product,
            "8":self.low_stock_alert,
            "9":self.calculate_total_inventory_value,
            "10":self.sort_by_name,
            "11":self.sort_by_pricr,
            "12":self.sort_by_quantity,
            "13":self.filter_by_category,
            "14":self.supplier,
            "15":self.save_to_json,
            "16":self.load_from_json,
            "17":self.export_to_csv,
            "18":self.import_from_csv,
        }
        while True:
            print("========== INVENTORY MANAGEMENT SYSTEM ==========")
            print("1. Add Product")
            print("2. View Products")
            print("3. Search Product")
            print("4. Update Product")
            print("5. Remove Product")
            print("6. Restock Product")
            print("7. Sell Product")
            print("8. Low Stock Alert")
            print("9. Calculate Inventory Value")
            print("10. Sort By Name")
            print("11. Sort By Price")
            print("12. Sort By Quantity")
            print("13. Filter By Category")
            print("14. Supplier Report")
            print("15. Save To JSON")
            print("16. Load From JSON")
            print("17. Export To CSV")
            print("18. Import from  CSV")
            print("19. Exit")
            print("===================================================")
            choice = input("Enter your choice: ").strip()
            if (choice =="19"):
                print("GoodBye")
                break
            elif choice in options:
                options[choice]()
            else:
                print("Invalid choice Please enter valid choice")
                
#=====================================================\   
 
inventory = Inventory()
inventory.menu()

#=====================================================\

'''class Supplier:
    def __init__(self,id,name,phone_number,company):
        self.id = id
        self.name = name
        self.phone = phone_number
        self.company = company


    def showdetails(self):
        print("Supplier_ID =",self.id)
        print("Supplier_Name =",self.name)
        print("Supplier_Number =",self.phone)
        print("Supplier_Company =",self.company)
        

class Suppliers:
    def __init__(self):
        self.suppliers = []

    def add_product(self,supplier):
        self.suppliers.append(supplier)

    def supplier_id(self):
        while True:
            id = input("Enter Supplier ID: ").strip()
            if not(id):
                print("You can not leave empty input")
                continue
            if (not id.isdigit()):
                print(F"{id} wrong input enter numeric number")
                continue
            if(len(id) != 4):
                print("Please Enter 4 Digit")
                continue
            id = int(id)

            found = False
            for s in self.suppliers:
                if(id == s.id):
                    print("ID not available..")
                    found = True
                    continue
            if not found:
                    print("ID available..")
                    break
                    
            

            

s = Supplier(1294,"Rehan","03187789323","ABC")
s = Supplier(1238,"Rehan","03187789323","ABC")
s = Supplier(1236,"Rehan","03187789323","ABC")
s = Supplier(1237,"Rehan","03187789323","ABC")

s.supplier_id()'''