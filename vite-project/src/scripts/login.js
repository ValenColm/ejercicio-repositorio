import { auth } from "../services/auth.js";
import { navigateTo } from "../constants/router.js";

const loginForm = document.getElementById("loginForm");
// Uso el id del botón para controlar el estado, por ejemplo deshabilitarlo mientras se valida el login.
const btnLogin = document.getElementById("btnlogin");

// El botón tiene tipo submit, por lo tanto no se maneja directamente el click, sino el evento submit del formulario, que es la forma correcta de manejar formularios en HTML
// Evento submit del formulario
loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const roleSelected = document.getElementById("role").value;

  // Desactivamos el botón para evitar doble envío
    btnLogin.disabled = true;

    try{
        const user = await auth.login(email, password)
        if(user.role !== roleSelected){
            throw new Error("Rol incorrecto");
        }

        if (user.role === "admin"){
            navigateTo("admin");
        }else{
                navigateTo("user")
            }
        } catch (error){
            alert(error.message);
        } finally {
            btnLogin.disabled = false;
        }
        });
    
