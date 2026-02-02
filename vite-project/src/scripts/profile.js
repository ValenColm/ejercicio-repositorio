// URL base del backend (json-server)
import { API_URL } from "../constants/config.js";

// auth gestiona la sesión del usuario
import { auth } from "../services/auth.js";

// navigateTo permite cambiar de vista sin recargar
import { navigateTo } from "../constants/router.js";

export const onProfileEnter = async () => {
  const currentUser = auth.getCurrentUser();

  // PROTECCIÓN
  if (!currentUser) {
    navigateTo("login");
    return;
  }

  // ELEMENTOS (YA EXISTEN)
  const profileName = document.getElementById("profileName");
  const profileEmail = document.getElementById("profileEmail");
  const profileRole = document.getElementById("profileRole");
  const profileOrders = document.getElementById("profileOrders");
  const backUserBtn = document.getElementById("backUser");

  // INFO USUARIO (SIEMPRE)
  profileName.textContent = currentUser.name || "Sin nombre";
  profileEmail.textContent = currentUser.email;
  profileRole.textContent = currentUser.role;

  // PEDIDOS
  try {
    const response = await fetch(`${API_URL}/orders`);
    const orders = await response.json();

    const myOrders = orders.filter(
      order => order.userId === currentUser.id
    );

    profileOrders.textContent = myOrders.length;
  } catch (error) {
    console.error("Error cargando pedidos", error);
    profileOrders.textContent = "0";
  }

  // BOTÓN VOLVER
  backUserBtn.addEventListener("click", () => {
    navigateTo(currentUser.role === "admin" ? "admin" : "user");
  });
};