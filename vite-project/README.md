RestorApp
System Description

RestorApp is a web application that simulates a restaurant ordering system.
It allows customers to view the menu, place orders, and check their profile information, while administrators can manage and control all orders in the system.

The application is built as a Single Page Application (SPA) with dynamic views, route protection, and data persistence using a simulated backend.

How to Run the Project

1. Clone or download the project.
2. Install json-server if it is not installed:
npm install -g json-server
3. json-server --watch data.json --port 3000
4.  Open the project using a local server (Live Server or similar).
5. Access the application in your browser.



Roles
User

* View menu
* Add products to cart
* Place orders
* View only their own orders
* View profile information

Admin

* View all orders
* Filter orders by status
* Change order status
* Manage restaurant order flow


Order Status

Orders can have the following statuses:

* Pending
* Preparing
* Ready
* Delivered

Statuses are updated dynamically from the admin panel.




Persistence

The system persists:

* Users
* Menu
* Orders (using json-server)
* Session (using localStorage)


Views

* Login
* User panel
* Admin panel
* Profile

Route protection is implemented according to user roles.

* Technical Features
* Central state management
* Dynamic DOM manipulation
* Event handling
* Forms with preventDefault
* Use of map, filter, find, some
* Modular file structure


Project Structure

/RestorApp
  index.html
  styles.css
  app.js
  data.json
  README.md
