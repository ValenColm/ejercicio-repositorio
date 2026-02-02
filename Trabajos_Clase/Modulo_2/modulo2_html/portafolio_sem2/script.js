// Mensaje de bienvenida
alert("Bienvenida a mi portafolio 💜");

// Cambiar texto de un párrafo
const parrafo = document.querySelector(".descripcion");
const botonTexto = document.createElement("button");

botonTexto.textContent = "Cambiar texto";

botonTexto.addEventListener("click", () => {
  parrafo.textContent = "Gracias por visitar mi portafolio ";});

parrafo.after(botonTexto);

// Mostrar / ocultar proyectos
const proyectos = document.querySelector(".lista_proyectos");
const botonToggle = document.createElement("button");

botonToggle.textContent = "Mostrar / Ocultar proyectos";

botonToggle.addEventListener("click", () => {
  proyectos.style.display =
    proyectos.style.display === "none" ? "grid" : "none";});

proyectos.before(botonToggle);