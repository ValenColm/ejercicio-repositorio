
const celda = document.querySelector("#celda");
console.log(celda);
const submit = document.getElementById("submit");
console.log(submit);
const listaNotas = document.getElementById("listaNotas");
console.log(listaNotas);

// Arreglo en memoria que almacenará todas las notas
let notas = [];

// Obtiene las notas guardadas en Local Storage (si existen)
const notasGuardadas = localStorage.getItem("notas");

// Verifica si hay notas guardadas previamente
if (notasGuardadas) {

  // Convierte el string JSON a un arreglo de JavaScript
  notas = JSON.parse(notasGuardadas);
  renderizarNotas();
  // Muestra en consola cuántas notas se cargaron
  console.log(`se cargaron ${notas.length} notas`);
  
}
  
  function renderizarNotas() {
  listaNotas.innerHTML = ""; 
  notas.forEach(nota => {
    // Por cada nota, la renderiza en el DOM
    crearNota(nota);
  });
  }

// Función que se encarga de crear una nota en el DOM
function crearNota(textoNota){

  // Crea un elemento <li>
  const li = document.createElement("li");
  // Agrega un espacio para separar el texto del botón
  li.textContent = textoNota + " ";
  
  // Crea el botón de eliminar
  const btnEliminar = document.createElement("button");
  // Asigna el texto al botón
  btnEliminar.textContent = "Eliminar";

  // Agrega el botón dentro del <li>
  li.appendChild(btnEliminar);

  // Agrega el <li> dentro de la lista <ul>
  listaNotas.appendChild(li);

  // Evento que se ejecuta al hacer click en "Eliminar"
  btnEliminar.addEventListener("click", () => {

    // Elimina el <li> específico del DOM
    listaNotas.removeChild(li);

    // Elimina la nota del arreglo en memoria
    notas = notas.filter(nota => nota !== textoNota);

    // Guarda el arreglo actualizado en Local Storage
    guardarNotas();
    
    // Mensaje en consola para evidenciar la acción
    console.log("Nota eliminada");
  });
}

// Evento que se ejecuta al hacer click en el botón "Agregar"
submit.addEventListener("click", () => {

  // Obtiene el valor escrito en el input
  const textoNota = celda.value;

  // Valida que el input no esté vacío
  if (textoNota == "") {
    console.log("el campo esta vacio");
    return;
  }

  // Agrega la nueva nota al arreglo en memoria
  notas.push(textoNota);

  // Guarda el arreglo actualizado en Local Storage
  guardarNotas();

  // Crea la nota visualmente en el DOM
  crearNota(textoNota);

  // Limpia el input
  celda.value = "";

  // Devuelve el foco al input
  celda.focus();

  // Mensaje en consola confirmando que la nota fue agregada
  console.log("nota agregada correctamente");


});

// Función que guarda las notas en Local Storage
function guardarNotas(){

  // Convierte el arreglo de notas a JSON y lo guarda
  localStorage.setItem("notas", JSON.stringify(notas));

  // Mensaje en consola para evidenciar el guardado
  console.log("notas guardadas en local Storage");
}




