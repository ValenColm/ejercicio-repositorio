// export  const getWeather = async (city) => {
// const api_key = "b94c796760eb613aff26759ecf5f4f9f"
// const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api_key}&units=metric`
// const response = await fetch(url)
// const data =  response.json()
// console.log (data)
// }




// export  const getWeather = async (city) => {
// const api_key = "b94c796760eb613aff26759ecf5f4f9f"
// const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api_key}&units=metric`

// const response = await fetch(url)

// if (!response.ok){
//     throw new Error("ciudad no encontrada")
// }

// const data = await response.json()
// console.log("DATA API:", data) // consola
// return data
// }




// const API_KEY = "b94c796760eb613aff26759ecf5f4f9f"

// //  Buscar ciudades
// export const searchCities = async (city) => {
//     const url = `https://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=5&appid=${API_KEY}`
//     const response = await fetch(url)

//     if (!response.ok) {
// throw new Error("Error buscando ciudades")
//     }

//     return await response.json()
// }

// // Clima por coordenadas
// export const getWeatherByCoords = async (lat, lon) => {
//     const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric&lang=es`
//     const response = await fetch(url)

//     if (!response.ok) {
//         throw new Error("Error obteniendo clima")
//     }

//     return await response.json()
// }

// export const setThemeByWeather = (weather) => {
//   const root = document.documentElement;

//   if (weather.includes("rain")) {
//     root.style.setProperty("--accent", "#38BDF8");
//   } else if (weather.includes("cloud")) {
//     root.style.setProperty("--accent", "#94A3B8");
//   } else {
//     root.style.setProperty("--accent", "#FACC15");
//   }
// };













// sin comentar


// const API_KEY = "b94c796760eb613aff26759ecf5f4f9f";

// export const searchCities = async (city) => {
//   const res = await fetch(
//     `https://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=5&appid=${API_KEY}`
//   );
//   return await res.json();
// };

// export const getWeatherByCoords = async (lat, lon) => {
//   const res = await fetch(
//     `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&lang=es&appid=${API_KEY}`
//   );
//   return await res.json();
// };

// export const setThemeByWeather = (weather) => {
//   const root = document.documentElement;

//   if (weather.includes("rain")) {
//     root.style.setProperty("--accent", "#38BDF8");
//   } else if (weather.includes("cloud")) {
//     root.style.setProperty("--accent", "#94A3B8");
//   } else {
//     root.style.setProperty("--accent", "#FACC15");
//   }
// };






// comentada

// Se define la API KEY que permite autenticarse con OpenWeatherMap
const API_KEY = "b94c796760eb613aff26759ecf5f4f9f";

// Función asíncrona que busca ciudades por nombre
export const searchCities = async (city) => {
  // Se hace una petición a la API de geolocalización de OpenWeatherMap
  const res = await fetch(
    // Se envía el nombre de la ciudad, se limita a 5 resultados y se incluye la API KEY
    `https://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=5&appid=${API_KEY}`
  );

  // Se convierte la respuesta en formato JSON y se retorna
  return await res.json();
};

// Función asíncrona que obtiene el clima usando latitud y longitud
export const getWeatherByCoords = async (lat, lon) => {
  // Se hace una petición a la API del clima actual
  const res = await fetch(
    // Se envían las coordenadas, unidades en Celsius, idioma español y la API KEY
    `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&lang=es&appid=${API_KEY}`
  );

  // Se convierte la respuesta en JSON y se retorna
  return await res.json();
};

// Función que cambia el tema visual según el tipo de clima
export const setThemeByWeather = (weather) => {
  // Se obtiene el elemento raíz del documento (html)
  const root = document.documentElement;

  // Si el clima contiene la palabra "rain"
  if (weather.includes("rain")) {
    // Se cambia la variable CSS --accent a un color azul
    root.style.setProperty("--accent", "#38BDF8");

  // Si el clima contiene la palabra "cloud"
  } else if (weather.includes("cloud")) {
    // Se cambia la variable CSS --accent a un color gris
    root.style.setProperty("--accent", "#94A3B8");

  // Para cualquier otro tipo de clima
  } else {
    // Se cambia la variable CSS --accent a un color amarillo
    root.style.setProperty("--accent", "#FACC15");
  }
};
