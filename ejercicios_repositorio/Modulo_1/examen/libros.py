book = []
sales = []

# Preloaded inventory with book information
inventory = [
  {
    "title": "Harry Potter and the Philosopher's Stone",
    "price": 10.0,
    "quantity": 10,
    "category": "trama",
    "author": "J. K. Rowling"
  },
  {
    "title": "Harry Potter and the Chamber of Secrets",
    "price": 15.0,
    "quantity": 5,
    "category": "trama",
    "author": "J. K. Rowling"
  },
  {
    "title": "Harry Potter and the Prisoner of Azkaban",
    "price": 20.0,
    "quantity": 3,
    "category": "trama",
    "author": "J. K. Rowling"
  },
  {
    "title": "Harry Potter and the Goblet of Fire",
    "price": 25.0,
    "quantity": 10,
    "category": "trama",
    "author": "J. K. Rowling"
  },
  {
    "title": "Harry Potter and the Order of the Phoenix",
    "price": 30.0,
    "quantity": 5,
    "category": "trama",
    "author": "J. K. Rowling" 
  } 
]


# -------------------------------------------
# Show all books registered in inventory
# -------------------------------------------
def show_inventory(inventory):
    if not inventory:
        print("No books registered.")
        return
    print("\n--- BOOKS ---")
    for book in inventory:
        print(f"title: {book['title']} | price: ${book['price']} | quantity: {book['quantity']} | category: {book['category']} | author: {book['author']}")


# -------------------------------------------
# Add new books to inventory
# -------------------------------------------
def add_books(inventory):

    print("\n--- REGISTER BOOK ---")

    # Internal function to request all values
    def pedir_valores(message=""):
        while True:
            exit_input = input(message).strip()
            if exit_input == "":
                return  # Exit if user presses ENTER

            # Request book details
            title = input("Enter book title: ")
            category = input("Enter category: ")
            author = input("Enter author: ")

            # Request price and quantity with validation
            try:
                price = float(input("Unit price: "))
                quantity = int(input("Stock quantity: "))
            except ValueError:
                print("⚠ Enter a valid price or quantity.")
                return

            if price < 0 or quantity < 0:
                print("Price and quantity must be positive.")
                return

            if not title or not category or not author:
                print("You cannot leave any field empty.")
                return

            # Add book to inventory
            inventory.append({
                "title": title,
                "price": price,
                "category": category,
                "quantity": quantity,
                "author": author
            })

            print("Book successfully added.")

    message = "Press ENTER to exit: "
    pedir_valores(message)



# -------------------------------------------
# Select and display a book by title
# -------------------------------------------
def select_book(inventory):
    show_inventory(inventory)
    title = input("Enter the book title you want to find: ")

    for book in inventory:
        if book["title"].lower() == title.lower():
            print(f"Book found: title: {book['title']} price: {book['price']} quantity: {book['quantity']} category: {book['category']} author: {book['author']}")
            return book

    print("Book not found.")
    return None



# -------------------------------------------
# Update a book's information
# -------------------------------------------
def actuality_book(inventory):
    show_inventory(inventory)
    title = input("Enter the title of the book you want to update: ")

    for book in inventory:
        if book["title"].lower() == title.lower():

            # Request new data
            new_title = input("New title: ")
            new_category = input("New category: ")
            try:
                new_price = float(input("New price: "))
                new_quantity = int(input("New quantity: "))
            except ValueError:
                print("Enter valid numerical values.")
                return

            if new_price < 0 or new_quantity < 0:
                print("Price and quantity must be positive.")
                return

            # Update values
            book["title"] = new_title
            book["category"] = new_category
            book["price"] = new_price
            book["quantity"] = new_quantity

            print("Book successfully updated.\n")
            return

    print("Book not found.")



# -------------------------------------------
# Delete a book from inventory
# -------------------------------------------
def delete_book(inventory):
    title = input("Enter the title of the book to delete: ")

    for book in inventory:
        if book["title"].lower() == title.lower():
            inventory.remove(book)
            print("Book deleted successfully.")
            return
    print("Book not found.")



# -------------------------------------------
# Register a sale and update inventory
# -------------------------------------------
def register_sale(inventory, sales):

    title = input("Sold book title: ").strip()

    # Find book
    book = next((b for b in inventory if b["title"].lower() == title.lower()), None)

    if not book:
        print("Book not found.")
        return

    if book["quantity"] <= 0:
        print("No stock available.")
        return

    # Request sold quantity
    try:
        quantity = int(input("Quantity sold: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if quantity > book["quantity"]:
            print("Not enough stock.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    # Request discount
    try:
        discount = float(input("Discount (%): "))
        if not 0 <= discount <= 100:
            print("Discount must be between 0% and 100%.")
            return
    except ValueError:
        print("Invalid discount.")
        return

    # Calculate final price
    unit_price = book["price"]
    total_bruto = unit_price * quantity
    total_neto = total_bruto * (1 - discount / 100)

    # Save sale
    sales.append({
        "libro": book["title"],
        "author": book["author"],
        "quantity": quantity,
        "unit_price": unit_price,
        "discount": discount,
        "total_paid": total_neto
    })

    # Update stock
    book["quantity"] -= quantity

    print("Sale successfully registered.")



# -------------------------------------------
# Top 3 best-selling books
# -------------------------------------------
def top_best_selling_books(sales):
    count = {}

    for sale in sales:
        title = sale["libro"]
        count[title] = count.get(title, 0) + sale["quantity"]

    return sorted(count.items(), key=lambda x: x[1], reverse=True)[:3]


# -------------------------------------------
# Group sales by author
# -------------------------------------------
def sales_by_autor(sales):
    grouped = {}

    for sale in sales:
        author = sale["author"]
        grouped[author] = grouped.get(author, 0) + sale["quantity"]

    return grouped


# -------------------------------------------
# Calculate gross and net revenue
# -------------------------------------------
def calculate_revenue(sales):
    gross = sum(v["quantity"] * v["unit_price"] for v in sales)
    net = sum(v["total_paid"] for v in sales)
    return gross, net



# -------------------------------------------
# Performance of each book (percentage sold)
# -------------------------------------------
def inventory_performance(inventory, sales):
    result = []

    for book in inventory:
        sold = sum(s["quantity"] for s in sales if s["libro"] == book["title"])
        initial = book["quantity"] + sold

        percent = (sold / initial * 100) if initial > 0 else 0

        result.append({
            "book": book["title"],
            "sold": sold,
            "initial_inventory": initial,
            "performance": round(percent, 2)
        })

    return result



# -------------------------------------------
# Generate full sales and inventory report
# -------------------------------------------
def generate_reports(inventory, sales):

    # Top selling books
    top = top_best_selling_books(sales)
    print("\n--- Top 3 Best-Selling Books ---")
    if top:
        for title, qty in top:
            print(f"{title}: {qty} units")
    else:
        print("No sales recorded.")

    # Sales by author
    print("\n--- Sales by Author ---")
    author_sales = sales_by_autor(sales)
    if author_sales:
        for author, qty in author_sales.items():
            print(f"{author}: {qty} units")
    else:
        print("No sales recorded.")

    # Income report
    print("\n--- Revenue ---")
    gross, net = calculate_revenue(sales)
    print(f"Gross revenue: ${gross}")
    print(f"Net revenue:   ${net}")

    # Inventory performance
    print("\n--- Inventory Performance ---")
    perf = inventory_performance(inventory, sales)
    for r in perf:
        print(f"{r['book']} | Sold: {r['sold']} | Initial: {r['initial_inventory']} | Performance: {r['performance']}%")

    print("\n==============================")


# -------------------------------------------
# Main menu (user interaction)
# -------------------------------------------
def menu():
    while True:
        print("MAIN MENU")
        print("1. Show inventory")
        print("2. Add books")
        print("3. Select book")
        print("4. Update book")
        print("5. Delete book")
        print("6. Top best-selling books")
        print("7. Revenue")
        print("8. Sales by author")
        print("9. Inventory performance")
        print("10. Generate full report")
        print("11. Register sale")
        print("12. Exit")

        try:
            option = int(input("Select an option (1–12): "))
        except ValueError:
            print("ERROR: invalid number.")
            return

        if option == 1:
            show_inventory(inventory)
        elif option == 2:
            add_books(inventory)
        elif option == 3:
            select_book(inventory)
        elif option == 4:
            actuality_book(inventory)
        elif option == 5:
            delete_book(inventory)
        elif option == 6:
            print(top_best_selling_books(sales))
        elif option == 7:
            print(calculate_revenue(sales))
        elif option == 8:
            print(sales_by_autor(sales))
        elif option == 9:
            print(inventory_performance(inventory, sales))
        elif option == 10:
            generate_reports(inventory, sales)
        elif option == 11:
            register_sale(inventory, sales)
        elif option == 12:
            print("Exiting program...")
            break
        else:
            print("Invalid option, choose between 1 and 12.")

menu()

            

                
            