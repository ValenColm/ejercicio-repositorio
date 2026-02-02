    //pedir datos como edad y nombre
let name = prompt("whats is your name?");
let age = prompt("whats is your age");
    // validar que se ingrese un numero
  const agenumber = Number(age);
  if (isNaN(agenumber)) {
    console.error("Error: Please enter a valid age in numbers.");
  } else {
    // mensajes dinamicos
    if (age >= 18) {
        console.log(`Hello ${name}, You are of legal age. Get ready for great opportunities in the world of programming!`)
    } else  {
        console.log(`hello ${name}, You are under 18. Keep learning and enjoying coding! `)
    }
  }