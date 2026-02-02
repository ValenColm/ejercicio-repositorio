// API_URL es la URL base del backend (json-server)
// Ejemplo: http://localhost:3000
import { API_URL } from "../constants/config.js";

// auth controla la sesión
import { auth } from "../services/auth.js";

// navigateTo permite cambiar de vista sin recargar la página
import { navigateTo } from "../constants/router.js";

// ESTADO
let cart = [];
// ======================
// REFERENCIAS AL DOM
// (se asignan en initUser)
// ======================

let menuContainer;
let orderSummary;
let myOrdersContainer;
let confirmOrderBtn;
let logoutBtn;
let goProfileBtn;


// ======================
// USUARIO ACTUAL
// ======================



const saveCart = () => {
  localStorage.setItem(
    `cart_${currentUser.id}`,
    JSON.stringify(cart)
  );
};

const loadCart = () => {
  const storedCart = localStorage.getItem(`cart_${currentUser.id}`);
  cart = storedCart ? JSON.parse(storedCart) : [];
};


const currentUser = auth.getCurrentUser();

if (!currentUser) {
  navigateTo("login");
  throw new Error("Usuario no logueado");
}


// ======================
// CARGAR MENÚ
// ======================

const loadMenu = async () => {
  const response = await fetch(`${API_URL}/menu`);
  const menu = await response.json();

  menuContainer.innerHTML = menu.map(product => `
    <li>
      <h4>${product.name}</h4>
      <p>Precio: $${product.price}</p>
      <p>Categoría: ${product.category}</p>
      <button data-id="${product.id}">Agregar al carrito</button>
    </li>
  `).join("");

  const buttons = menuContainer.querySelectorAll("button");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      addToCart(button.dataset.id, menu);
    });
  });
};


// ======================
// AGREGAR AL CARRITO
// ======================

const addToCart = (productId, menu) => {
  const product = menu.find(p => p.id == productId);

  const exists = cart.some(item => item.id == productId);

  if (exists) {
    cart = cart.map(item =>
      item.id == productId
        ? { ...item, quantity: item.quantity + 1 }
        : item
    );
  } else {
    cart.push({
      id: product.id,
      name: product.name,
      price: product.price,
      quantity: 1
    });
  }
  saveCart();
  renderCart();
};

// RENDER CARRITO

const renderCart = () => {
  if (cart.length === 0) {
    orderSummary.innerHTML = "<li>Carrito vacío</li>";
    confirmOrderBtn.hidden = true;
    return;
  }

  confirmOrderBtn.hidden = false;

  const total = cart.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );

  orderSummary.innerHTML = `
    ${cart.map(item => `
      <li class="cart-item">
        <span>${item.name}</span>

        <div class="qty-controls">
        <button type="button" class="decrease" data-id="${item.id}">➖</button>
        <span>${item.quantity}</span>
        <button type="button" class="increase" data-id="${item.id}">➕</button>
      </div>

      <span>$${item.price * item.quantity}</span>
    </li>
  `).join("")}

  <li><strong>Total: $${total}</strong></li>
  `;
};

// CONFIRMAR PEDIDO

const confirmOrder = async () => {
  if (cart.length === 0) {
    alert("El carrito está vacío");
    return;
  }

  const total = cart.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );

  const newOrder = {
    userId: currentUser.id,
    items: cart,
    total,
    status: "pendiente",
    createdAt: new Date().toISOString()
  };

  await fetch(`${API_URL}/orders`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newOrder)
  });

  cart = [];
  saveCart();
  renderCart();
  loadMyOrders();
};


// ======================
// MIS PEDIDOS
// ======================

const loadMyOrders = async () => {
  const response = await fetch(`${API_URL}/orders`);
  const orders = await response.json();

  const myOrders = orders.filter(
    order => order.userId === currentUser.id
  );

  myOrdersContainer.innerHTML = myOrders.map(order => `
    <li>
      <p>ID: ${order.id}</p>
      <p>Total: $${order.total}</p>
      <p>Estado: ${order.status}</p>
    </li>
  `).join("");
};


// ======================
// INICIALIZACIÓN (CLAVE)
// ======================

const initUser = () => {

  menuContainer = document.getElementById("menuContainer");
  orderSummary = document.getElementById("orderSummary");
  myOrdersContainer = document.getElementById("myOrders");
  confirmOrderBtn = document.getElementById("confirmOrder");
  logoutBtn = document.getElementById("logoutBtn");
  goProfileBtn = document.getElementById("goProfile");

  cart = [];
  loadCart();
  renderCart();
  loadMenu();
  loadMyOrders();


  confirmOrderBtn.addEventListener("click", confirmOrder);


  // Quitar productos del carrito (CLICK AUTOMÁTICO)

  orderSummary.addEventListener("click", (e) => {
  const btn = e.target.closest("button");
  if (!btn) return;

  const id = btn.dataset.id;


  if (btn.classList.contains("increase")) {
    cart = cart.map(item =>
      item.id === id
        ? { ...item, quantity: item.quantity + 1 }
        : item
    );
  }

  if (btn.classList.contains("decrease")) {
    cart = cart
      .map(item =>
        item.id === id
          ? { ...item, quantity: item.quantity - 1 }
          : item
      )
      .filter(item => item.quantity > 0);
  }
  saveCart();
  renderCart();
});





  logoutBtn.addEventListener("click", () => {
    auth.logout();
    navigateTo("login");
  });

  goProfileBtn.addEventListener("click", () => {
    navigateTo("profile");
  });
};
export const onUserEnter = () => {
  initUser();
};
