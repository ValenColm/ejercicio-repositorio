
// con comentarios


// Se importan las funciones necesarias desde el archivo weather.js
import { searchCities, getWeatherByCoords, setThemeByWeather } from "./weather.js";

// Se obtiene el botón de búsqueda por su id
const submit = document.getElementById("submit");

// Se obtiene el input donde el usuario escribe la ciudad
const celda = document.getElementById("celda");

// Se obtiene la lista donde se mostrarán las ciudades encontradas
const citiesList = document.getElementById("cities");

// Se obtiene el contenedor donde se mostrará el resultado del clima
const result = document.getElementById("result");

// Función que normaliza el texto eliminando tildes y espacios extra
const normalize = (t) =>
  // Convierte caracteres con tilde en caracteres separados
  t.normalize("NFD")
    // Elimina los signos diacríticos (tildes)
    .replace(/[\u0300-\u036f]/g, "")
    // Elimina espacios al inicio y al final
    .trim();

// Se agrega un evento al botón para cuando el usuario haga click
submit.addEventListener("click", async () => {
  // Se obtiene el valor del input y se normaliza
  const city = normalize(celda.value);

  // Si el input está vacío, se detiene la ejecución
  if (!city) return;

  // Se limpia la lista de ciudades anteriores
  citiesList.innerHTML = "";

  // Se limpia el resultado anterior del clima
  result.innerHTML = "";

  try {
    // Se buscan las ciudades usando la API
    const cities = await searchCities(city);

    // Si no se encontraron ciudades, se muestra un mensaje
    if (cities.length === 0) {
      citiesList.innerHTML = `<li class="empty">No se encontraron ciudades</li>`;
      return;
    }

    citiesList.setAttribute("role", "listbox");

    // Se recorre cada ciudad encontrada
    cities.forEach((c) => {
      // Se crea un elemento li para cada ciudad
      const li = document.createElement("li");

      // Se muestra el nombre de la ciudad y el país
      li.textContent = `${c.name}, ${c.country}`;
       // Se define el rol para accesibilidad
      li.setAttribute("role", "option");


      // Se permite que el elemento sea accesible con el teclado
      li.setAttribute("tabindex", index === 0? "0" : "-1");

     
      // Evento para seleccionar la ciudad con el mouse
      li.addEventListener("click", () => {
        showWeather(c.lat, c.lon, c.name, c.country);
      });

      // Evento para manejar el teclado cuando el li tiene foco
      li.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
      showWeather(c.lat, c.lon, c.name, c.country);
    }

    if (e.key === "ArrowDown") {
      e.preventDefault();
      const next = li.nextElementSibling;
      if (next) {
        li.setAttribute("tabindex", "-1");
        next.setAttribute("tabindex", "0");
        next.focus();
      }
    }

    if (e.key === "ArrowUp") {
      e.preventDefault();
      const prev = li.previousElementSibling;
      if (prev) {
        li.setAttribute("tabindex", "-1");
        prev.setAttribute("tabindex", "0");
        prev.focus();
      }
    }
  });
      // Se agrega el li a la lista de ciudades
      citiesList.appendChild(li);
    });
  citiesList.firstElementChild?.focus();
  } catch (error) {
    // Si ocurre un error en la búsqueda, se muestra un mensaje
    citiesList.innerHTML = `<li class="empty">Error al buscar ciudades</li>`;
  }
});

// Evento para detectar cuando el usuario presiona una tecla en el input
celda.addEventListener("keydown", (e) => {
  // Si la tecla es Enter, se simula el click del botón
  if (e.key === "Enter") {
    submit.click();
  }

  if (e.key === "ArrowDown") {
    citiesList.firstElementChild?.focus();
  }

});

// Función que obtiene y muestra el clima de la ciudad seleccionada
const showWeather = async (lat, lon, name, country) => {
  try {
    // Se obtiene la información del clima usando las coordenadas
    const data = await getWeatherByCoords(lat, lon);

    // Se obtiene el tipo de clima principal
    const weatherType = data.weather[0].main.toLowerCase();

    // Se eliminan clases anteriores del body
    document.body.className = "";

    // Se agrega una clase según el tipo de clima
    document.body.classList.add(`weather-${weatherType}`);

    // Se ajusta el tema visual según el clima
    setThemeByWeather(weatherType);

    // Se muestra la información del clima en el HTML
    result.innerHTML = `
      <h3>${name}, ${country}</h3>
      <p>Temperatura: ${data.main.temp} °C</p>
      <p>Sensación térmica: ${data.main.feels_like} °C</p>
      <p>Humedad: ${data.main.humidity}%</p>
      <p>Viento: ${data.wind.speed} m/s</p>
      <p>${data.weather[0].description}</p>
      <img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png">
    `;
  } catch (error) {
    // Si ocurre un error al obtener el clima, se muestra un mensaje
    result.textContent = "Error al obtener el clima";
  }
};
