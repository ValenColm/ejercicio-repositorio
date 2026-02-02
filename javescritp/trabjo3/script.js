let tareas = []; 
let indiceEditando = null;
const listaTareas = document.getElementById('listaTareas');
const nuevaTareaInput = document.getElementById('nuevaTareaInput');
const agregarTareaBtn = document.getElementById('agregarTareaBtn');
const agregarVariasTareasBtn = document.getElementById('agregarVariasTareasBtn');


function renderizartareas() {
    listaTareas.innerHTML = '';
    tareas.forEach((tarea, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
        <span class="tarea-texto ${tarea.completada? 'completada' : ''}">${tarea.texto}</span>
        <button onclick="marcarComoCompletada(${index})">${tarea.completada? 'Desmarcar':'Completar'}</button>
        <button onclick="borrarTarea(${index})">Borrar</button>
        <button onclick="editarTarea(${index})">Editar</button>
        `;
        listaTareas.appendChild(li);
    })
}

//crear(add)
agregarTareaBtn.addEventListener('click', () => {
    const textoTarea = nuevaTareaInput.value.trim();

    if (!textoTarea) return;

    if (indiceEditando === null) {
        // CREAR
        tareas.push({ texto: textoTarea, completada: false });
    } else {
        // EDITAR
        tareas[indiceEditando].texto = textoTarea;
        indiceEditando = null;
        agregarTareaBtn.textContent = "Agregar tarea";
    }

    nuevaTareaInput.value = '';
    renderizartareas();
});





// actualizar (update - marcar como completada/desmarcar)
function marcarComoCompletada(index) {
    tareas[index].completada= !tareas[index].completada;
    renderizartareas();
}
function borrarTarea(index) {
    tareas.splice(index, 1); // elimina 1 tarea desde la posición index
    renderizartareas();      // vuelve a imprimir la lista
}

//EDITAR TAREA  
function editarTarea(index) {
    nuevaTareaInput.value = tareas[index].texto
    indiceEditando = index;
    agregarTareaBtn.textContent = "Guardar";

}
