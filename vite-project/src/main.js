
// Importamos el router para poder navegar entre vistas
import { navigateTo } from "./constants/router.js";

// Importamos auth para saber si hay sesión activa
import { auth } from "./services/auth.js";

const navbar = document.getElementById("navbar");

// 1. ESCUCHAR CLICKS EN LINKS DE NAVEGACIÓN
document.addEventListener("click", (e) => {
  // Verifica si el elemento clickeado tiene data-route
  if (e.target.matches("[data-route]")) {
    e.preventDefault(); // evita recargar la página
    navigateTo(e.target.dataset.route);

  }
});


// ======================================================
// FUNCIÓN PRINCIPAL DE ARRANQUE
// ======================================================

// Esta función se ejecuta UNA SOLA VEZ
// cuando la aplicación carga por primera vez
const startApp = () => {
  const user = auth.getCurrentUser();


  // 2. Si NO hay usuario logueado
  if (!user) {
    navbar.style.display = "none"; // ocultamos nabvar
    navigateTo("login");
    return;
  }

  // si hay sesion
  navbar.style.display = "block"; // mostramos navbar

   
  if (user.role === "admin") {
   navigateTo("admin");
  }else{
    navigateTo("user")
  }
};
// Se ejecuta automáticamente al cargar la app
startApp();
