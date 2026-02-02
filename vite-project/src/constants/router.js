//router.js

//Controla navegación ,Protege rutas según rol ,Carga vistas dinámicamente ,Carga scripts por vista

import { auth } from "../services/auth.js";

const app = document.getElementById("app");


// Cada ruta apunta a un archivo HTML
 export const routes = {
  login: "public/views/login.html",
  user: "public/views/user.html",
  admin: "public/views/admin.html",
  profile: "public/views/profile.html"
};

    export const navigateTo = async (route) => {
        const user = auth.getCurrentUser();

        // proteccion de rutas

    // No logueado → solo login
  if (!user && route !== "login") {
    route = "login";
  }

  // Logueado intentando ir a login
  if (user && route === "login") {
    route = user.role === "admin" ? "admin" : "user";
  }

  // User no entra a admin
  if (user && user.role === "user" && route === "admin") {
    route = "user";
  }

  // Admin no entra a user
  if (user && user.role === "admin" && route === "user") {
    route = "admin";
  }

  // ===== CARGA DEL HTML =====
  const response = await fetch(routes[route]);
  const html = await response.text();

  app.innerHTML = html;
  updateNavbar();

  // ===== CARGA DEL JS + INIT =====
  if (route === "login") {
    const module = await import("../scripts/login.js");
    module.initLogin?.();
  }

  if (route === "user") {
    const module = await import("../scripts/user.js");
    module.onUserEnter();
  }

  if (route === "admin") {
    const module = await import("../scripts/admin.js");
    module.onAdminEnter?.();
  }

  if (route === "profile") {
    const module = await import("../scripts/profile.js");
    module.onProfileEnter();
  }
};

// ===== NAVBAR =====
const updateNavbar = () => {
  const navbar = document.getElementById("navbar");
  const user = auth.getCurrentUser();

  const adminLink = document.querySelector('[data-route="admin"]');
  const userLink = document.querySelector('[data-route="user"]');
  const profileLink = document.querySelector('[data-route="profile"]');

  // Sin sesión → no navbar
  if (!user) {
    navbar.style.display = "none";
    return;
  }

  navbar.style.display = "block";
  profileLink.style.display = "inline";

  if (user.role === "admin") {
    adminLink.style.display = "inline";
    userLink.style.display = "none";
  } else {
    adminLink.style.display = "none";
    userLink.style.display = "inline";
  }
};