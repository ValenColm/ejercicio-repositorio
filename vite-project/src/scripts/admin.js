// Importa la constante API_URL desde el archivo de configuración.
// Esta variable contiene la URL base del backend (ej: http://localhost:3000)
import { API_URL } from "../constants/config.js";

// Importa el módulo de autenticación.
// auth permite saber quién está logueado y cerrar sesión.
import { auth } from "../services/auth.js";

// Importa la función para cambiar de vista/página dentro de la app.
import { navigateTo } from "../constants/router.js";

/* ======================
   VARIABLES
====================== */

// Variable que guardará el contenedor HTML donde se renderizan los pedidos
let ordersContainer;

// Variable que guarda el select para filtrar pedidos por estado
let statusFilter;

// Variable que referencia el botón de cerrar sesión
let logoutBtn;

// Variable que referencia el formulario para crear platos del menú
let menuForm;

// Variable que referencia la lista donde se muestran los platos del menú
let menuList;

/* ======================
   MENÚ (CRUD)
====================== */

// FUNCIÓN PARA OBTENER EL MENÚ (READ)
// Función asincrónica porque usa fetch
const getMenu = async () => {

  // Hace una petición HTTP GET al endpoint /menu
  const response = await fetch(`${API_URL}/menu`);

  // Convierte la respuesta en JSON y la devuelve
  return await response.json();
};

// FUNCIÓN PARA CREAR UN PLATO (CREATE)
// Recibe un objeto item con name, price y category
const createMenuItem = async (item) => {

  // Hace una petición POST al backend
  await fetch(`${API_URL}/menu`, {

    // Indica que es una creación
    method: "POST",

    // Define que se enviará JSON
    headers: { "Content-Type": "application/json" },

    // Convierte el objeto JS en texto JSON
    body: JSON.stringify(item)
  });
};

// FUNCIÓN PARA ELIMINAR UN PLATO (DELETE)
// Recibe el id del plato
const deleteMenuItem = async (id) => {

  // Hace una petición DELETE al endpoint del plato específico
  await fetch(`${API_URL}/menu/${id}`, {

    // Método DELETE elimina el recurso
    method: "DELETE"
  });
};

// FUNCIÓN PARA ACTUALIZAR UN PLATO (UPDATE)
// Recibe el id y el objeto actualizado
const updateMenuItem = async (id, item) => {

  // Hace una petición PUT para reemplazar los datos
  await fetch(`${API_URL}/menu/${id}`, {

    // PUT indica actualización completa
    method: "PUT",

    // Define el tipo de contenido
    headers: { "Content-Type": "application/json" },

    // Convierte el objeto actualizado en JSON
    body: JSON.stringify(item)
  });
};

// FUNCIÓN PARA MOSTRAR EL MENÚ EN EL DOM
// Recibe un arreglo de platos
const renderMenu = (menu) => {

  // Limpia la lista antes de volver a renderizar
  menuList.innerHTML = "";

  // Recorre cada plato del menú
  menu.forEach(item => {

    // Crea un elemento <li>
    const li = document.createElement("li");

    // Inserta inputs y botones dentro del <li>
    li.innerHTML = `
      <input class="menu-name" data-id="${item.id}" value="${item.name}">
      <input class="menu-price" data-id="${item.id}" type="number" value="${item.price}">
      <input class="menu-category" data-id="${item.id}" value="${item.category}">

      <button class="save-menu" data-id="${item.id}">Guardar</button>
      <button class="delete-menu" data-id="${item.id}">Eliminar</button>
    `;

    // Agrega el <li> a la lista del menú
    menuList.appendChild(li);
  });

  // Llama a la función que agrega los eventos a los botones
  addMenuListeners();
};

// FUNCIÓN QUE AGREGA LOS EVENTOS DEL MENÚ
const addMenuListeners = () => {

  // Selecciona todos los botones de eliminar
  document.querySelectorAll(".delete-menu").forEach(btn => {

    // Escucha el evento click
    btn.addEventListener("click", async e => {

      // Elimina el plato usando su id
      await deleteMenuItem(e.target.dataset.id);

      // Vuelve a renderizar el menú actualizado
      renderMenu(await getMenu());
    });
  });

  // Selecciona todos los botones de guardar
  document.querySelectorAll(".save-menu").forEach(btn => {

    // Escucha el evento click
    btn.addEventListener("click", async e => {

      // Obtiene el id del plato
      const id = e.target.dataset.id;

      // Obtiene el nombre actualizado del input
      const name =
        document.querySelector(`.menu-name[data-id="${id}"]`).value;

      // Obtiene el precio actualizado y lo convierte a número
      const price = Number(
        document.querySelector(`.menu-price[data-id="${id}"]`).value
      );

      // Obtiene la categoría actualizada
      const category =
        document.querySelector(`.menu-category[data-id="${id}"]`).value;

      // Envía los datos actualizados al backend
      await updateMenuItem(id, { name, price, category });

      // Refresca el menú en pantalla
      renderMenu(await getMenu());
    });
  });
};

/* ======================
   PEDIDOS
====================== */

// FUNCIÓN PARA OBTENER PEDIDOS
const getOrders = async () => {

  // Petición GET al endpoint orders
  const response = await fetch(`${API_URL}/orders`);

  // Devuelve los pedidos en formato JSON
  return await response.json();
};

// FUNCIÓN PARA ACTUALIZAR EL ESTADO DEL PEDIDO
const updateOrderStatus = async (id, status) => {

  // Petición PATCH para cambiar solo el estado
  await fetch(`${API_URL}/orders/${id}`, {

    // PATCH modifica solo una parte del objeto
    method: "PATCH",

    // Define el tipo de contenido
    headers: { "Content-Type": "application/json" },

    // Envía el nuevo estado
    body: JSON.stringify({ status })
  });
};

// FUNCIÓN PARA ELIMINAR UN PEDIDO
const deleteOrder = async (id) => {

  // Petición DELETE al pedido específico
  await fetch(`${API_URL}/orders/${id}`, {
    method: "DELETE"
  });
};

// FUNCIÓN PARA RENDERIZAR PEDIDOS
const renderOrders = (orders) => {

  // Limpia el contenedor antes de renderizar
  ordersContainer.innerHTML = "";

  // Recorre todos los pedidos
  orders.forEach(order => {

    // Crea un div por pedido
    const div = document.createElement("div");

    // Inserta información del pedido
    div.innerHTML = `
      <p>ID: ${order.id}</p>
      <p>Total: $${order.total}</p>

      <select class="order-status" data-id="${order.id}">
        <option value="pendiente" ${order.status === "pendiente" ? "selected" : ""}>Pendiente</option>
        <option value="preparando" ${order.status === "preparando" ? "selected" : ""}>Preparando</option>
        <option value="listo" ${order.status === "listo" ? "selected" : ""}>Listo</option>
        <option value="entregado" ${order.status === "entregado" ? "selected" : ""}>Entregado</option>
      </select>

      <button class="delete-order" data-id="${order.id}">Eliminar</button>
      <hr>
    `;

    // Agrega el pedido al contenedor
    ordersContainer.appendChild(div);
  });

  // Activa los eventos de pedidos
  addOrderListeners();
};

// FUNCIÓN DE EVENTOS PARA PEDIDOS
const addOrderListeners = () => {

  // Escucha cambios en el select de estado
  document.querySelectorAll(".order-status").forEach(select => {
    select.addEventListener("change", async e => {

      // Actualiza el estado del pedido
      await updateOrderStatus(
        e.target.dataset.id,
        e.target.value
      );
    });
  });

  // Escucha el botón eliminar pedido
  document.querySelectorAll(".delete-order").forEach(btn => {
    btn.addEventListener("click", async e => {

      // Elimina el pedido
      await deleteOrder(e.target.dataset.id);

      // Refresca la lista de pedidos
      renderOrders(await getOrders());
    });
  });
};

/* ======================
   ADMIN ENTER
====================== */

// FUNCIÓN QUE SE EJECUTA AL ENTRAR A LA VISTA ADMIN
export const onAdminEnter = async () => {

  // Obtiene el usuario actualmente logueado
  const user = auth.getCurrentUser();

  // Verifica que exista y sea admin
  if (!user || user.role !== "admin") {

    // Si no es admin, redirige al login
    navigateTo("login");
    return;
  }

  // Referencias al DOM del menú
  menuForm = document.getElementById("menu-form");
  menuList = document.getElementById("menu-list");

  // Referencias al DOM de pedidos
  ordersContainer = document.getElementById("admin-orders");
  statusFilter = document.getElementById("status-filter");
  logoutBtn = document.getElementById("logout-admin");

  // Carga inicial del menú y pedidos
  renderMenu(await getMenu());
  renderOrders(await getOrders());

  // EVENTO SUBMIT DEL FORMULARIO MENÚ
  menuForm.addEventListener("submit", async e => {

    // Evita que la página se recargue
    e.preventDefault();

    // Crea un nuevo plato
    await createMenuItem({
      name: document.getElementById("menu-name").value,
      price: Number(document.getElementById("menu-price").value),
      category: document.getElementById("menu-category").value
    });

    // Limpia el formulario
    menuForm.reset();

    // Actualiza el menú
    renderMenu(await getMenu());
  });

  // EVENTO PARA FILTRAR PEDIDOS
  statusFilter.addEventListener("change", async () => {

    // Obtiene todos los pedidos
    const orders = await getOrders();

    // Muestra todos o filtra por estado
    statusFilter.value === "all"
      ? renderOrders(orders)
      : renderOrders(
          orders.filter(o => o.status === statusFilter.value)
        );
  });

  // EVENTO LOGOUT
  logoutBtn.addEventListener("click", () => {

    // Cierra sesión
    auth.logout();

    // Redirige al login
    navigateTo("login");
  });
};
