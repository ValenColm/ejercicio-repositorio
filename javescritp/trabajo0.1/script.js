// let name = prompt("whats is your name?")
// let city = prompt("whats is your city?")
// let age = prompt("whats is your age")
// menssage = ""
// if (age >=18)
 //   {menssage="eres mayor de edad, y estas permitido"}
 // else 
//{menssage="eres menor de edad"
//}

//alert(` hola, te llamas ${name} eres de ${city} y tu edad es ${age} `); 



// Seleccionamos el body
const body = document.body;

// Preguntamos cuántas notas va a ingresar el usuario
let cantidadNotas = Number(prompt("¿Cuántas notas vas a ingresar?"));

// Validación de la cantidad de notas
if (isNaN(cantidadNotas) || cantidadNotas <= 0) {
    alert("Debes ingresar un número válido mayor que 0");
} else {

    // Arreglo para guardar los inputs
    const notas = [];

    // Creamos los inputs según la cantidad ingresada
    for (let i = 0; i < cantidadNotas; i++) {
        const input = document.createElement("input");
        input.type = "number";
        input.placeholder = `Nota ${i + 1}`;
        body.appendChild(input);
        notas.push(input);
    }

    // Creamos el botón
    const boton = document.createElement("button");
    boton.textContent = "Calcular Promedio";
    body.appendChild(boton);

    // Creamos el párrafo del resultado
    const resultado = document.createElement("p");
    body.appendChild(resultado);

    // Evento del botón
    boton.addEventListener("click", calcularPromedio);

    // Función para calcular el promedio
    function calcularPromedio() {

        let suma = 0;

        // Recorremos las notas
        for (let i = 0; i < notas.length; i++) {

            let valor = Number(notas[i].value);

            // Validación: solo números
            if (notas[i].value === "" || isNaN(valor)) {
                resultado.textContent = " Ingresa solo números en todas las notas";
                return;
            }

            suma += valor;
        }

        let promedio = suma / notas.length;
        promedio = promedio.toFixed(2);

        // Condicional
        if (promedio >= 3.0) {
            resultado.textContent = `Promedio: ${promedio} -  Aprobó`;
        } else {
            resultado.textContent = `Promedio: ${promedio} -  Reprobó`;
        }
    }
}
