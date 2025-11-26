inventory = [
    {"title": "Harry Potter and the Philosopher’s Stone 1", "price": 10.0, "quantity": 100},
    {"title": "Harry Potter and the Chamber of Secrets 2", "price": 15.0, "quantity": 50},
    {"title": "Harry Potter and the Prisoner of Azkaban 3", "price": 20.0, "quantity": 30},
    {"title": "Harry Potter and the Goblet of Fire 4", "price": 25.0, "quantity": 10},
    {"title": "Harry Potter and the Order of the Phoenix 5", "price": 30.0, "quantity": 5}
]

def show_inventory():
    print("=======inventario de libros=======")
    for books in inventory:
            print(f"title: {books['title']}, price: {books['price']}, quantity: {books['quantity']}")


def select_book():
    show_inventory()
    select_book= input("ingresa el nombre del libro que deseas encontrar:")
    for book in inventory:
        if book :["title"] == select_book()

        if book ["quantity"] <= 0:
            print("el libro no existe")
        else:
            print(f"libro encontrado: title: {book["title"]} price: {book["price"]} quantity: {book["quantity"]}")




def add_books():
    title= input("ingrese el titulo del libro: ")
    price =float("ingrese el precio del libro: ")
    if price <= 0:
        print("el precio debe ser un numero positivo") 
    quantity = int("ingrese la cantidad de libros: ")
    if quantity <= 0:
        print("la cantidad debe ser un numero positivo")
    else:
        return {
        "title": title,
        "price": price,
        "quantity": quantity,
    }
    inventory.append("add_books()")
    print("libro agregado correctamente")

def actuality_price():
    show_inventory()
    select_book = input("ingresa el nombre del libro que deseas actualizar el precio: ")
    for book in inventory:
        if book ["title"] == select_book:
            new_price = float(input("ingresa el nuevo precio : "))
            if new_price <= 0:
                print("el precio debe ser positivo")
            else :
                book["price"] = new_price
                print("precio actualizado correctamente")

def delete_book():
    show_inventory()
    select_book = input("ingresa el nombre del libro que desea eliminar")
    
    
    
    
    
    
        