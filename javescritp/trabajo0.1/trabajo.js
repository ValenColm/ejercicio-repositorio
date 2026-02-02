


const val = document.getElementById('val')
const mensaje= document.getElementById('mensaje')

function valentinita(){
    const fullData = new Date;
    const dateString = fullData.toString()
    const day = dateString.slice(0,4)
    const fecha = dateString.slice(4,15)
    const hour = dateString.slice(16,24)

    console.log (`la hora es ${hour} la fecha es ${fecha} y el dia es ${day}`)
    const salida = `la hora es ${hour} la fecha es ${fecha} y el dia es ${day}`
    if(mensaje) mensaje.textContent = salida
}
    val.addEventListener('click', valentinita)


// Métodos comunes

//     toFixed(): Formatea el número con una cantidad específica de decimales
//     toPrecision(): Formatea el número a una longitud total específica
//     toString(): Convierte el número a string (puede especificar la base)
//     toExponential(): Convierte el número a notación exponencial
//     Number.isInteger(): Verifica si es un número entero
//     Number.isNaN(): Verifica si el valor es NaN
//     Number.parseFloat(): Convierte un string a número decimal
//     Number.parseInt(): Convierte un string a número entero
//     Number.isFinite(): Verifica si es un número finito
//     Math.round(): Redondea al entero más cercano
//     Math.floor(): Redondea hacia abajo
//     Math.ceil(): Redondea hacia arriba
//     Math.abs(): Devuelve el valor absoluto
//     Math.max(): Devuelve el mayor de los números dados
//     Math.min(): Devuelve el menor de los números dados
//     Math.random(): Genera un número aleatorio entre 0 y 1



    let num = 123.456;
console.log(num.toFixed(2)); // '123.46'
console.log(num.toPrecision(4)); // '123.5'
console.log(num.toString()); // '123.456'

let price = 99.99;
console.log(Math.round(price)); // 100
console.log(Math.floor(price)); // 99
console.log(Math.ceil(price)); // 100

console.log(Number.isInteger(42)); // true
console.log(Number.isInteger(42.5)); // false

let str = '42.5';
console.log(Number.parseFloat(str)); // 42.5
console.log(Number.parseInt(str)); // 42

console.log(Math.max(10, 20, 5, 30)); // 30
console.log(Math.min(10, 20, 5, 30)); // 5
console.log(Math.abs(-15)); // 15

// Número aleatorio entre 1 y 10
let random = Math.floor(Math.random() * 10) + 1;
console.log(random);







// Métodos comunes

//     toUpperCase(): Convierte el texto a mayúsculas
//     toLowerCase(): Convierte el texto a minúsculas
//     trim(): Elimina espacios en blanco al inicio y al final
//     split(): Divide el string en un array según un separador
//     slice(): Extrae una parte del string
//     substring(): Similar a slice, extrae caracteres entre dos índices
//     replace(): Reemplaza la primera coincidencia de un texto
//     replaceAll(): Reemplaza todas las coincidencias de un texto
//     includes(): Verifica si contiene un texto específico
//     startsWith(): Verifica si comienza con un texto específico
//     endsWith(): Verifica si termina con un texto específico
//     indexOf(): Devuelve la posición de la primera coincidencia
//     charAt(): Devuelve el carácter en una posición específica
//     repeat(): Repite el string n veces
//     padStart(): Rellena el inicio hasta alcanzar una longitud
//     padEnd(): Rellena el final hasta alcanzar una longitud


    //let mensaje = "hola mundo";

// //toUpperCase()
console.log(messagge.toUpperCase())
//toLowerCase()
console.log(messagge.toLowerCase())
//trim()
console.log(messagge.trim())
//split()
console.log(messagge.split())
//slice()
console.log(messagge.slice())
//subtring()
console.log(messagge.substring(3,11))
//replace()
console.log(messagge.replace("a","T"))
//replaceAll()
console.log(messagge.replaceAll("s","Q"))
//includes()
console.log(messagge.includes())
//startsWith
console.log(messagge.startsWith)
//endsWith
console.log(messagge.endsWith)
//indexOf
console.log(messagge.indexOf("t"))
//charAt
console.log(messagge.charAt(2))



// Manipulación con JavaScript (DOM)
// Puedes crear y gestionar estas listas usando métodos del DOM:

//     Crear elementos: document.createElement('ul') o document.createElement('li').
//     Añadir texto: document.createTextNode('Hola') o elemento.textContent = 'Hola'.
//     Insertar texto en el <li>: li.appendChild(texto).
//     Añadir <li> al <ul>: ul.appendChild(li).
//     Insertar el <ul> en el HTML: document.body.appendChild(ul). 





// <!DOCTYPE html>
// <html lang="es">
// <head>
//     <meta charset="UTF-8">
//     <title>Manipulación de Atributos</title>
// </head>
// <body>

//     <button id="miBoton" data-estado="activo">Haz clic</button>

//     <script>
//         // 1. Obtener el elemento
//         const boton = document.getElementById('miBoton');

//         // 2. setAttribute(): Agregar o modificar un atributo
//         // Si 'data-estado' existe, se actualiza; si no, se crea.
//         boton.setAttribute('data-estado', 'inactivo');
//         console.log('Atributo modificado:', boton.getAttribute('data-estado')); // Salida: inactivo

//         // 3. getAttribute(): Recuperar el valor de un atributo
//         const estadoActual = boton.getAttribute('data-estado');
//         console.log('Estado actual:', estadoActual); // Salida: inactivo

//         // 4. setAttribute() para añadir un atributo nuevo
//         boton.setAttribute('title', '¡Este botón ha cambiado!');
//         console.log('Título agregado:', boton.getAttribute('title')); // Salida: ¡Este botón ha cambiado!

//         // 5. removeAttribute(): Eliminar un atributo
//         boton.removeAttribute('data-estado');
//         console.log('Atributo data-estado existe ahora?:', boton.hasAttribute('data-estado')); // Salida: false

//     </script>
// </body>
// </html>




// atributo (ej. href, src, id, class, data-xyz).
