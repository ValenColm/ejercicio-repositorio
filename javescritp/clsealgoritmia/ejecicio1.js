// dado un array de numeros enteros encuentra dos numeros que sumen un valor adjetivo y retornalos, si no retorna false


function encontrarSuma(nums, objetivo) {
    const mapa = {}; // Almacena los números vistos y sus índices

    for (let i = 0; i < nums.length; i++) {
        const complemento = objetivo - nums[i];

        // Si el complemento ya existe en nuestro "registro", encontramos el par
        if (complemento in mapa) {
            return [complemento, nums[i]];
        }

        // Si no, guardamos el número actual en el registro
        mapa[nums[i]] = i;
    }

    return false; // Si termina el ciclo sin encontrar nada
}

// Ejemplo de uso:
const numeros = [5, 8, 10, 1, 14];
const valorObjetivo = 9;
console.log(encontrarSuma(numeros, valorObjetivo)); // Resultado: [8, 1]
