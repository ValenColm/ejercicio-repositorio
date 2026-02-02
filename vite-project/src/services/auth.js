// auth.js

//Maneja sesión ,Usa localStorage ,No toca DOM ,Centraliza autenticación

import { API_URL } from "../constants/config.js";

const SESSION_KEY = "SESSION_KEY"

export const auth = {
  
  // 1. LOGIN: Verificar credenciales
  // Esta función:
  // - recibe email y password
  // - consulta los usuarios en db.json
  // - verifica si existe un usuario con esas credenciales
  // - guarda la sesión en localStorage
  // - retorna el usuario o null
  login: async (email, password) => {

  // 1. hacemos una peticion get a users
    const response = await fetch(`${API_URL}/users`);
    const users = await response.json();

    // 2. Buscamos un usuario que coincida
    // se usa find porque espera un solo resultado
    const user = users.find(
        u => u.email === email && u.password === password
    );

    // 3. Si no existe, retornamos null
    if (!user) {
      throw new Error("Credenciales incorrectas");
    }


    // Guardar sesión (sin contraseña por seguridad)
    const sessionUser = {
      id: user.id,
      name: user.name,
      email: user.email,
      role: user.role
    };

    // 4. Guardamos sesión
    // Se convierte a string porque localStorage solo guarda texto
    localStorage.setItem("SESSION_KEY", JSON.stringify(sessionUser));

    return sessionUser;
},
    
  
  // 2. LOGOUT: Cerrar sesión
  logout: () => {
    // Elimina datos de localStorage
    localStorage.removeItem(SESSION_KEY);
  },
  
  // 3. GET CURRENT USER: Usuario actual
  //   Esta función:
  // - obtiene el usuario guardado en localStorage
  // - lo convierte de string a objeto
  // - retorna el usuario o null
  getCurrentUser: () => {
    // Lee de localStorage
    const user = localStorage.getItem(SESSION_KEY);
    // Retorna el usuario logueado
    return user ? JSON.parse(user) : null;
  },
  
  // 4. IS AUTHENTICATED: ¿Hay sesión?
  isAuthenticated: () => {
    // Verifica si existe usuario en localStorage
    return localStorage.getItem(SESSION_KEY) !== null;
    // Retorna true/false
  },
  
  // 5. IS ADMIN: ¿Es administrador?
  isAdmin: () => {
    // Verifica si el rol del usuario
    const user = auth.getCurrentUser();
    return user?.role === "admin";
    // Retorna true/false
  }
};